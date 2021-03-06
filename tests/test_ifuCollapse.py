# Import necessarty modules
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip

import sys
sys.path.append('./scripts/')
from ifu_3d_collapse import collapse

# ======================================================
#                       Test suite
# ======================================================

def test_arrayCollapse():
    """
    1. Test the arrayCollapse function.
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    #result = _arrayCollapse(cube, method='mean')
    
    result = collapse(cube, region=[0, 29], method='mean')
    assert isinstance(result, np.ndarray)
    
    
def test_maskedCollapse():
    """
    2. Test the maskedCollapse function.
    """
    mu, sigma = 0, 15
    cube = np.random.normal(loc=mu, scale=sigma, size=(10, 20, 20))
    
    #clipped = sigma_clip(cube, sig=1, iters=None, copy=True)
    #collapsed_array = _maskedCollapse(clipped, method='median')
    
    collapsed_array = collapse(cube, region=[0,9], method='median', sigma=1.)
    assert isinstance(collapsed_array, np.ndarray)
    

def test_sliceFalseSigma():
    """
    3. Setting sigma value to 'False'
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = collapse(cube, region=[15, 27], method='median', sigma=False)
    assert isinstance(result, np.ndarray)
    
def test_sliceOmitSigma():
    """
    4. Omit sigma input argument
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = collapse(cube, region=[15, 27], method='median')
    assert isinstance(result, np.ndarray)


def test_sliceZeroSigma():
    """
    5. Setting sigma value to zero
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = collapse(cube, region=[15, 27], method='median', sigma=0)
    assert isinstance(result, np.ndarray)
    

def test_sliceSigma():
    """
    6. Set valid sigma value
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = collapse(cube, region=[15, 27], method='median', sigma=2.5)
    assert isinstance(result, np.ndarray)
    
def test_emptySlice():
    """
    7. Test an empty input z-slice selection
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = collapse(cube, method='median', sigma=2.5)
    assert isinstance(result, np.ndarray)
    
# ======================================================
#                       Test suite
# ======================================================    