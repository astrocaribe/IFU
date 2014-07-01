# Import necessarty modules
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip
from ifu_3d_collapse import *


# ======================================================
#                       Test suite
# ======================================================
def test_sliceFalseSigma():
    """
    1. Setting sigma value to 'False'
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median', sigma=False)
    assert isinstance(result, np.ndarray)

    
def test_sliceOmitSigma():
    """
    2. Omit sigma input argument
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median')
    assert isinstance(result, np.ndarray)


def test_sliceZeroSigma():
    """
    3. Setting sigma value to zero
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median', sigma=0)
    assert isinstance(result, np.ndarray)
    

def test_sliceSigma():
    """
    4. Set valid sigma value
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = ifu_3d_collapse(cube, sect=[15, 27], method='median', sigma=2.5)
    assert isinstance(result, np.ndarray)
# ======================================================
#                       Test suite
# ======================================================    