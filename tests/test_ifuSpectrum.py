# Import necessarty modules
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip

import sys
sys.path.append('./scripts/')
from ifu_1d_spectrum import extractSpectrum


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
    
    testSpec = extractSpectrum(cube, [[30,30]], cals, trim=100, continuum=False, display=False)
    assert testSpec.shape[0] == 3 and isinstance(testSpec, np.ndarray)
    

def test_extractNoTrim():
    """
    2. Test the spectrum extraction function without a trim value.
    """
    
    testSpec = extractSpectrum(cube, [[30,30]], cals, continuum=False, display=False)
    assert testSpec.shape[0] == 3 and isinstance(testSpec, np.ndarray)    
 
def test_extractContinuum():
    """
    3. Test continuum-extracted spectrum.
    """
    
    testSpec = extractSpectrum(cube, [[30,30]], cals, continuum=True, display=False)
    assert testSpec.shape[0] == 3 and isinstance(testSpec, np.ndarray)    
    
def test_extractLists():
    """
    4. Test the spectrum extraction function on a range of spaxels.
    
    Test passes, but as a list of spaxels (list of [[x1, x2, ... xn], [y1, y2, ... yn]]).
    """
    
    testSpec = extractSpectrum(cube, [[27,33,30],[27,33,30]], cals, trim=100, continuum=False, display=False)
    assert testSpec.shape[0] == 3 and isinstance(testSpec, np.ndarray)
    
def test_extractPairs():
    """
    5. Test the spectrum extraction function on a range of spaxels.
    
    Test passes, but as pairs of lists (list of [[x1, y1], [x2, y2] ...[xn, yn]]).
    """
    
    testSpec = extractSpectrum(cube, [[27, 27], [33, 33], [15, 30]], cals, trim=100, continuum=False, display=False)
    assert testSpec.shape[0] == 3 and isinstance(testSpec, np.ndarray)
    
def test_extractPairsContinuum():
    """
    6. Test the spectrum extraction function on a range of spaxels, with continuum extraction.
    
    Test passes, but as pairs of lists (list of [[x1, y1], [x2, y2] ...[xn, yn]]).
    Continuum extraction is performed.
    """
    
    testSpec = extractSpectrum(cube, [[27, 27], [33, 33], [15, 30]], cals, trim=100, continuum=True, display=False)
    assert testSpec.shape[0] == 3 and isinstance(testSpec, np.ndarray)