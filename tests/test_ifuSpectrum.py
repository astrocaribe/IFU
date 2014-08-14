# Import necessarty modules
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip

import sys
sys.path.append('./scripts/')
from ifu_1d_spectrum import *


# ======================================================
#                       Test suite
# ======================================================
    
# Read in cube, including header for wavelength calibration values
cube, header = fits.getdata('./data/NGC4151_Hband.fits', 1, header=True)
    
# Read in crpix, crval, and cdelt values from the header.
# Convert crpix and crdelt values from angstroms to microns
#header = fits.getheader('./data/NGC4151_Hband.fits', ext=1)
crpix = header['CRPIX3']
crval = header['CRVAL3']/1.e4
cdelt = header['CDELT3']/1.e4
cals = [crpix, crval, cdelt]


def test_extractSpaxel():
    """
    1. Test the spectrum extraction function on a single spaxel.
    """
    
    testSpec = ifu_1d_spectrum(cube, [30,30], cals, trim=100, continuum=False, display=False)
    assert isinstance(testSpec, np.ndarray)
    

def test_extractNoTrim():
    """
    2. Test the spectrum extraction function without a trim value.
    """
    
    testSpec = ifu_1d_spectrum(cube, [30,30], cals, continuum=False, display=False)
    assert isinstance(testSpec, np.ndarray)
    
 
def test_extractContinuum():
    """
    3. Test continuum-extracted spectrum.
    """
    
    testSpec = ifu_1d_spectrum(cube, [30,30], cals, continuum=True, display=False)
    assert isinstance(testSpec, np.ndarray)
    
    
def test_extractRange():
    """
    4. Test the spectrum extraction function on a range of spaxels.
    
    Test passes, but as a list of spaxels (list of x and y).
    """
    
    testSpec = ifu_1d_spectrum(cube, [[27,33],[27,33]], cals, trim=100, continuum=False, display=False)
    assert isinstance(testSpec, np.ndarray)
    