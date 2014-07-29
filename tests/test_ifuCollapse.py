# Import necessarty modules
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip

import sys
sys.path.append('./scripts/')
from ifu_3d_collapse import *


# ======================================================
#                       Test suite
# ======================================================

def test_arrayCollapse():
    """
    1. Test the arrayCollapse function.
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = arrayCollapse(cube, method='mean')
    assert isinstance(result, np.ndarray)
    
    
def test_arrayCollapse_list():
    """
    2. Test an arrayCollapse w/ a list of members.
    """
    mu, sigma = 0, 15
    cube = np.random.normal(loc=mu, scale=sigma, size=(10, 20, 20))
    clipped = sigma_clip(cube, sig=1, iters=None, copy=True)
    
    good = clipped.nonzero()
    
    clipped = sigma_clip(cube[good], sig=1, iters=None, copy=True)
    print(clipped)
    assert isinstance(clipped, np.ndarray)
    

def test_sliceFalseSigma():
    """
    3. Setting sigma value to 'False'
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median', sigma=False)
    assert isinstance(result, np.ndarray)
    
def test_sliceOmitSigma():
    """
    4. Omit sigma input argument
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median')
    assert isinstance(result, np.ndarray)


def test_sliceZeroSigma():
    """
    5. Setting sigma value to zero
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median', sigma=0)
    assert isinstance(result, np.ndarray)
    

def test_sliceSigma():
    """
    6. Set valid sigma value
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median', sigma=2.5)
    assert isinstance(result, np.ndarray)
# ======================================================
#                       Test suite
# ======================================================    