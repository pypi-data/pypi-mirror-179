import itk
import numpy as np
from random import shuffle
import skimage.restoration
from skimage.morphology import dilation, disk

'''Collection of utility methods.  Note, this module is likely subject to API change.'''
def crop(npimg, crop, rgb=False):
    '''
    Crops the ndarray denoted by npimg according to rows and columns specified in crop.
    
    Parameters
    ----------
    npimg : ndarray
        [Tx]xMxNx[RGB]
    crop : ndarray
        [[topmost, bottommost], [lefmost, rightmost]]
    rgb : bool
        whether it is an rgb img
    '''
    if rgb:
        if len(npimg.shape) == 3:
            return npimg[crop[0,0]:(crop[0,1]+1), crop[1,0]:(crop[1,1]+1), :]
        else: # len(npimg.shape) == 4:
            return npimg[:, crop[0,0]:(crop[0,1]+1), crop[1,0]:(crop[1,1]+1),:]
    else: # len(npimg.shape) == 4:
        if len(npimg.shape) == 2:
            return npimg[crop[0,0]:(crop[0,1]+1), crop[1,0]:(crop[1,1]+1)]
        elif len(npimg.shape) == 3:
            return npimg[:, crop[0,0]:(crop[0,1]+1), crop[1,0]:(crop[1,1]+1)]
        else:
            assert('npimg must be 2 or 3 dims (rgb=False) or 3 or 4 dims (rgb=True)')

def inward_out_crop(nparr, center=None, bg_threshold=0, crop_threshold=(0.1, 0.1), row_first=True, pad=(0,0,0,0)):
    '''
    Calculates a crop of B-mode data by looking for a dark border.
    
    Starts at the center of an image and searches for the first columns/rows that fail to
    meet the threshold parameters.  Threshold defined by np.argwhere(col > bg_threshold) > col_size * crop_threshold
    
    That is, the number of pixels above a background value is sufficiently greater than some
    percentage of the image's size.
    
    Parameters
    ----------
    nparr : ndarray
        video or image, if image, H, W, RGB, if video, F, H, W, RGB.  Should be scaled to 0.0 to 1.0
    center : tuple of 2 ints
        (row,column) center index to start the inward_out crop, defaults to middle of nparr if None
    bg_threshold : float
        The threshold for values to be considered background
    crop_threshold : float
        What percentage of row/column of pixels should be non-zero to be considered valid B-mode
    row_first : bool
        If true, determine the crop by rows first, then crop within the rows.  For example, if you have
        a lot of noisy UI annotation on the sides of the image, it is likely best to start by determining
        the column boundaries first (row_first=False).
    pad : tuple of 4 ints
        Tuple of ints (pad-top, pad-bottom, pad-left, pad-right) that are correction factors to the calculated
        crop.  For example, if there is a horizontal bar 5 pixels above the B-mode that is included in the crop,
        use (-5,0,0,0) to manually remove it.  Negative values are shrinking, postive values are expanding.
        
    Returns
    -------
    ndarray
        2x2 array in format [[start_row, end_row], [start_column, end_column]]
    '''
    assert len(nparr.shape) in (2,3)
    
    npmean = nparr if len(nparr.shape) == 2 else np.mean(nparr, axis=0)
    
    # center of image
    cr, cc = (np.array(npmean.shape) / 2.0).astype('int') if center is None else center

    def crop_row(cr, sc=0, ec=npmean.shape[1]-1):
        '''
        Parameters
        ----------
        cr : int
            Row index to start inward-out
        sc : int
            Left-most column bound to count non-background pixels
        ec : int
            Right-most columnb bound to count non-background pixels
        Returns
        -------
        sr : int
            Starting row index (top)
        er : int
            Ending row index (bottom)
        '''
        sr = cr
        er = cr
        row_cutoff = (ec - sc + 1) * crop_threshold[0] # number of non-background pixels as cutoff between ec and sc

        while sr > 0 and len(np.argwhere(npmean[sr,sc:(ec+1)] > bg_threshold)) > row_cutoff:
            sr -= 1
        sr += -pad[0] # add user-specified correction
        sr = max(0, sr) # clamp valid index
        
        while er < npmean.shape[0]-1 and len(np.argwhere(npmean[er,sc:(ec+1)] > bg_threshold)) > row_cutoff:
            er += 1
        er += pad[1] # add user-specified correction
        er = min(er, npmean.shape[0]-1) # clamp to valid index
        
        return sr, er
    
    def crop_col(cc, sr=0, er=npmean.shape[0]-1):
        sc = cc
        ec = cc
        col_cutoff = (er - sr + 1) * crop_threshold[1]
        
        while sc > 0 and len(np.argwhere(npmean[sr:(er+1), sc] > bg_threshold)) > col_cutoff:
            sc -= 1
        sc += -pad[2]
        sc = max(0, sc)
        
        while ec < npmean.shape[1]-1 and len(np.argwhere(npmean[sr:er,ec]) > bg_threshold) > col_cutoff:
            ec += 1
        ec += pad[3]
        ec = min(ec, npmean.shape[1]-1)
        
        return sc, ec
     
    if row_first:
        sr, er = crop_row(cr)
        sc, ec = crop_col(cc, sr, er)
    else:
        sc, ec = crop_col(cc)
        sr, er = crop_row(cr, sc, ec)
    
    return np.array([[sr, er], [sc, ec]], dtype='int')
            
        
def extract_slice(img, slice_, axis=2):
    '''
    Returns a 2D frame from a 3D image (assumes itk.F pixels)
    
    Adds frame to the index of the largest possible region according to the selected axis.  Direction submatrix is maintained
    in returned frame image.
    
    Parameters
    ----------
    img : itk.Image[itk.F,3] 
        3D ITK image
    slice_ : int
        the frame/slice to get
    axis : ndarray
        a binary array of size dim specifing which index to slice along, the default assumes typical z-axis index
    '''
    
    region = img.GetLargestPossibleRegion()
    size = list(region.GetSize())
    size[axis] = 0
    region.SetSize(size)
    index = list(region.GetIndex())
    index[axis] += slice_
    region.SetIndex(index)
    extractor = itk.ExtractImageFilter[itk.Image[itk.F,3], itk.Image[itk.F,2]].New(Input=img, ExtractionRegion=region)
    extractor.SetDirectionCollapseToSubmatrix()
    extractor.Update()
    return extractor.GetOutput()

def polgyon_from_array(pts):
    '''
    Return a PolygonSpatialObject from a list of points defining a closed polygon.
    
    Parameters
    ----------
    pts : ndarray
        Nx2 open array of polygon points, x0 != xn
        
    Returns
    -------
    itk.PolygonSpatialObject[2]
    '''
    if pts is None:
        return None
    
    poly1=itk.PolygonSpatialObject[2].New(IsClosed=True)
    for i in range(pts.shape[0]):
        spt = itk.SpatialObjectPoint[2]()
        spt.SetPositionInObjectSpace(itk.Point[itk.D,2](pts[i,:]))
        poly1.AddPoint(spt)
    poly1.Update()
    return poly1

def image_from_array(array, spacing=None, direction=None, origin=None, reference_image=None):
    '''
    Augment ITK image_from_array so common parameters can be set in one line
    
    Parameters
    ----------
    array : ndarray
    spacing : ndarray, optional
    direction : ndarray, optional
    origin : ndarray, optional
    reference_image : ndarray, optional
        if specified, use its spacing, direction, origin
        
    Returns
    -------
    itk.Image
    '''
    if reference_image is not None:
        spacing = reference_image.GetSpacing()
        direction = reference_image.GetDirection()
        origin = reference_image.GetOrigin()
    
    img = itk.image_from_array(array)
    if spacing is not None:
        img.SetSpacing(spacing)
    if direction is not None:
        img.SetDirection(direction)
    if origin is not None:
        img.SetOrigin(origin)
    
    return img

def array_from_image(img, return_meta=False):
    '''
    Augment ITK array_from_image so that common parameters are also returned
    
    Returns
    -------
    img : itk.Image
    spacing : ndarray, optional
        if return_meta
    direction : ndarray, optional
        if return_meta
    origin : ndarray, optional
        if return_meta
    '''
    # return array, spacing, direction, origin
    if return_meta:
        return itk.array_from_image(img), img.GetSpacing(), img.GetDirection(), img.GetOrigin()
    else:
        return itk.array_from_image(img)


def operate(img1, img2, foo):
    '''
    Convenience function for applying a function foo between two images.  foo is written on numpy arrays.  This function will output
    ITK arrays or numpy arrays to match the input.
    
    Parameters
    ----------
    img1 : itk.Image or ndarray
    img2 : itk.Image or ndarray
    foo : function
        foo(img1, img2)
    
    Returns
    -------
    itk.Image or ndarray
    '''
    assert type(img1) == type(img2)
    tstr = str(type(img1))
    if tstr.contains('itkImage'):
        npimg1 = itk.array_from_image(img1)
        npimg2 = itk.array_from_image(img2)
    else:
        npimg1 = img1
        npimg2 = img2
        
    npimg3 = foo(npimg1, npimg2)
    if tstr.contains('itkImage'):
        ans = image_from_array(npimg3, img1.GetSpacing(), img1.GetDirection(), img1.GetOrigin())
    else:
        ans = npimg3
    
    return ans
        
def overwrite_mask(npimg1, npimg2, outside_value=0):
    '''
    Combine npimg1 and npimg2 while overwriting any overlap with npimg2's value.
    
    Parameters
    ----------
    npimg1 : ndarray
    npimg2 : ndarray
    outside_value : float or int, default=0
        elements in npimg2 with value == outside_value will not overwrite npimg1
        
    Returns
    -------
    ndarray
    '''
    ans = npimg1.copy()
    idx = npimg2 != outside_value
    ans[idx] = npimg2[idx]
    return ans
    
def union_mask(npimg1, npimg2, outside_value=0, inside_value=1):
    '''
    Combine npimg1 and npimg2 and set the union to inside_value
    
    Parameters
    ----------
    npimg1 : ndarray
    npimg2 : ndarray
    outside_value : float or int, default=0
        defines the background in the mask images
    inside_value : float or int, default=1
        defines the value of non-background union
        
    Returns
    -------
    ndarray
    '''
    ans = np.ones(npimg1.shape) * outside_value
    idx = np.logical_or(npimg1 != outside_value, npimg2 != outside_value)
    ans[idx] = inside_value
    return ans

def array_from_spatial(obj, size, inside_value=1, outside_value=0):
    '''
    Return a Numpy array image of an ITKSpatialOjbect
    
    obj : itk.SpatialObject or list of itk.SpatialObject 
        spatial object(s) to convert to mask image, should be in index (i.e. spacing = 1.0, origin = 0.0) coordinates
    size : ndarray 
        size in x and y (columns, rows)
    inside_value : float or list of float
        value to assign interior of each mask, if real, same value for each mask
    outside_value : float
        value to assign background
        
    Returns
    -------
    ndarray
    '''
    # the below is to allow obj to either be a single spatial object or a list
    # expand objects to lists
    if not type(obj) == list:
        obj = [obj]
    
    if not type(inside_value) == list:
        inside_value = [inside_value] * len(obj)
    
    npimg = np.ones(np.flip(size)) * outside_value
    for i in range(len(obj)):
        o = obj[i]
        if o is not None:
            filter = itk.SpatialObjectToImageFilter[itk.SpatialObject[2], itk.Image[itk.F,2]].New(Input=o, InsideValue=inside_value[i], OutsideValue=outside_value, Size=size.tolist())
            filter.Update()
            mask = filter.GetOutput()
            npimg = overwrite_mask(npimg, array_from_image(mask), outside_value=outside_value)

    return npimg

def image_from_spatial(obj, reference_image, inside_value=1, outside_value=0):
    '''
    Return a mask image from a single or list of ITKSpatialObjects.
    
    Parameters
    ----------
    obj : itk.SpatialObject or list of itk.SpatialObject
        spatial object(s) to convert to mask image, should be in index (i.e. spacing = 1.0, origin = 0.0) coordinates
    reference_image : itk.Image
        sets the spacing, direction, origin, and size of the output image
    inside_value : float or list of float
        value to assign interior of each mask, if real, same value for each mask
    outside_value : float
    
    Returns
    -------
    itk.Image
    '''
    npimg = array_from_spatial(obj, np.array(reference_image.GetLargestPossibleRegion().GetSize()), inside_value, outside_value)
    ans = image_from_array(npimg, reference_image.GetSpacing(), reference_image.GetDirection(), reference_image.GetOrigin())
    return ans

def get_framerate(meta_dict):
    '''
    Returns the framerate as a float from a meta_dict from ffprobe.
    
    Parameters
    ----------
    meta_dict : dict
    
    Returns
    -------
    float
    '''
    arr = meta_dict['video']['@avg_frame_rate'].split('/')
    return float(arr[1]) / float(arr[0])
    
def wrap_itk_index(x):
    '''
    DEPRECATED: see if this is necessary in newer ITK version
    '''
    idx = itk.Index[2]()
    idx.SetElement(0, int(x[0]))
    idx.SetElement(1, int(x[1]))
    return idx

def wrap_itk_point(x):
    '''
    DEPRECATED: see if this is necessary in newer ITK version
    '''
    # TODO, why itk.F?
    pt = itk.Point[itk.F,2]()
    pt.SetElement(0, x[0])
    pt.SetElement(1, x[1])
    return pt

def transform_to_physical(indices, image):
    '''
    Transform [y,x] indices to physical locations in an image.  Note, this is not the same as ITK's index scheme.
    
    Parameters
    ----------
    indices : ndarray
        Nx2 indices represented as [row,col], i.e., numpy indexing
    image : itk.Image
    
    Returns
    -------
    ndarray
        Nx2 physical points [x,y]
    '''
    start_index = np.asarray(image.GetLargestPossibleRegion().GetIndex())
    return np.apply_along_axis(lambda x: np.array(image.TransformIndexToPhysicalPoint(wrap_itk_index(x))), 1, np.fliplr(indices) + start_index[np.newaxis,:])

def transform_to_indices(pts, image):
    '''
    Transform ITK's physical locations to [y,x] indices.  Note, this is not the same as ITK's index scheme.
    
    Parameters
    ----------
    pts : ndarray
        Nx2 physical points [x,y]
    image : itk.Image
    
    Returns
    -------
    ndarray
        Nx2 indices in [row,col], i.e., numpy indexing
    '''
    start_index = np.asarray(image.GetLargestPossibleRegion().GetIndex())
    return np.fliplr(np.apply_along_axis(lambda x: np.array(image.TransformPhysicalPointToIndex(wrap_itk_point(x))), 1, pts) - start_index[np.newaxis,:])

def window_sample(x, spacing, num=None):
    '''
    Randomly sample an array of indices maintaining a minimum distance between samples.  For example, when wanting to take frames from a video that
    are sufficiently separated in time.
    
    Parameters
    ----------
    x : ndarray of int
        an array of indices such as from np.argwhere
    spacing : int
        distance maintained between return indices, i.e., or all x,y in result,  :math:`|x-y| > \text{spacing}`
    num : int
        number of samples to return, or as many as possible if None
    
    Returns
    -------
    ndarray : 
        subsample of x
    '''
    num = num if num is not None else len(x)
    y = x.copy()
    shuffle(y)
    ans = list()
    while len(y) > 0 and len(ans) < num:
        tmp = y[0]
        ans.append(tmp)
        y = [r for r in y[1:] if r < tmp - spacing or r > tmp + spacing]
    
    return ans

def inpaint(npimg, mask):
    '''
    Inpaint the locations in npimg corresponding to true values in mask.
    
    Parameters
    ----------
    npimg : ndarray
        MxN
    mask : ndarray
        MxN
        
    Returns
    -------
    ndarray
    '''
    return skimage.restoration.inpaint.inpaint_biharmonic(npimg, mask)

def get_overlay_mask(npimgrgb, version=None, threshold=250, dilation_radius=5):
    '''
    Identify the overlay and annotation elements by brightness (threshold) and color.
    
    Parameters
    ----------
    npimg : ndarray
        MxNx3
    version : None
        reserved for future use
    threshold : int
        brightness threshold for overlay elements, if too low, B-mode data may mistakenly masked
        
    Returns
    -------
    ndarray
        False is background and True is overlay
    '''
    mask = np.logical_not((npimgrgb[:,:,0] == npimgrgb[:,:,1]) & (npimgrgb[:,:,1] == npimgrgb[:,:,2])) | (npimgrgb[:,:,0] >= threshold)
    mask = dilation(mask, disk(dilation_radius))
    return mask