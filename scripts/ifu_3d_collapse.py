from __future__ import print_function
import numpy as np
from astropy.stats.funcs import sigma_clip

import sys
sys.path.append('./scripts/')
from ifu_math import *

def arrayCollapse(array_in, method):
    
    # Perform an array collapse
    if method == 'sum':
        print('(3d_collapse): Sum of extracted slices:')
        collapsed_array = np.sum(array_in, axis=0)
            
    elif method == 'mean':
        print('(3d_collapse): Mean of extracted slices:')
        collapsed_array = np.mean(array_in, axis=0)
    
    elif method == 'median':
        print('(3d_collapse): Median of extracted slices:')
        collapsed_array = np.median(array_in, axis=0)
        
    return collapsed_array

    

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
    
    print('***************** Dev Test *****************')
    print('(ifu_3d_collapse): Developement test Vr. 0.2')
    print('***************** Dev Test *****************')
    
    # Extract the desired slice...
    slice_array = array_in[sect[0]:sect[1], :, :]
        
    # ... and perform the desired operation, based on input mode.
    collapsed_array = arrayCollapse(slice_array, method=method)
    
    if sigma:
        # Subtract the collapsed array from the input datacube
    #    subtracted_array = ifu_math(slice_array, collapsed_array, method='subtract')
    #    print()
    #    print('(3d_collapse): Subtracted array shape:', subtracted_array.shape)
        
        # Perform sigma-clip on subtracted cube
        print('(3d_collapse): Clipping data...')
        #clipped_array = sigma_clip(subtracted_array, sigma, iters=None, axis=0, copy=False)
        clipped_array = sigma_clip(slice_array, sigma, iters=None, axis=0, copy=False)
        print()
        print('(3d_collapse): Array shape:', clipped_array.shape)
        
    #    if np.array_equal(clipped_array, subtracted_array): print('Damn, arrays are exactly the same!')
        if not np.array_equal(clipped_array, slice_array): 
            raise TypeError
            print('Damn, arrays are exactly the same!')    
        
        # Now that we have the sigma mask, recalculate the collapse...
        collapsed_array = arrayCollapse(clipped_array, method)    

    
    # Return the collaped array
    #collapsed_array = clipped_array
    print()
    print('(3d_collapse): Shape of returned array:', collapsed_array.shape)
    return collapsed_array