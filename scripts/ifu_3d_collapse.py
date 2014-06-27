from __future__ import print_function
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip
from ifu_math import *

def ifu_3d_collapse(array_in, sect=[0,0], method='sum', sigma=False):
    """
    Collapse a slice of a datacube, with a given mode, along the 
    wavelength slice.
    
    Keyword arguments:
    array_in -- The input datacube array.
    sect     -- The section of the datacube to collapse, in the 
                form of [a, b], where a is the 1st slice boundary,
                and b is the 2nd + 1 slice boundary.
    mode     -- The mode of collapse. Available are sum, mean,
                and median.
    """
    
    # Extract the desired slice...
    slice_array = array_in[sect[0]:sect[1], :, :]
        
    # ... and perform the desired operation, based on input mode.
    if method == 'sum':
        print('Sum of extracted slices:')
        collapsed_array = np.sum(slice_array, axis=0)
            
    elif method == 'mean':
        print('Mean of extracted slices:')
        collapsed_array = np.mean(slice_array, axis=0)
    
    elif method == 'median':
        print('Median of extracted slices:')
        collapsed_array = np.median(slice_array, axis=0)
    

    # Subtract the collapsed array from the input datacube
    subtracted_array = ifu_math(slice_array, collapsed_array, method='subtract')
    print()
    print('Subtracted array shape:', subtracted_array.shape)
    
    if sigma:
        # Perform sigma-clip on subtracted cube
        print('Clipping data...')
        clipped_array = sigma_clip(subtracted_array, sigma, iters=None, axis=0, copy=False)
        print()
        print('Array shape:', clipped_array.shape)
        
        if np.array_equal(clipped_array, subtracted_array): print('Damn, arrays are exactly the same!')
        
    else:
        # Test statement:
        clipped_array = subtracted_array
        print('Array shape:', clipped_array.shape)
    

    # Now that we have the sigma mask, recalculate the collapse...
    if method == 'sum':
        print('Sum of extracted slices, part 2:')
        collapsed_array = np.sum(clipped_array, axis=0)
            
    elif method == 'mean':
        print('Mean of extracted slices, part 2:')
        collapsed_array = np.mean(clipped_array, axis=0)
    
    elif method == 'median':
        print('Median of extracted slices, part 2:')
        collapsed_array = np.median(clipped_array, axis=0)


    
    # Return the collaped array
    #collapsed_array = clipped_array
    print()
    print('Shape of returned array:', collapsed_array.shape)
    return collapsed_array