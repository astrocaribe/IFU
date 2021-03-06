# Import necessarty modules
import numpy as np
from astropy.io import fits
from astropy.stats.funcs import sigma_clip

import sys
sys.path.append('./scripts/')
from ifu_1d_spectrum import *
from ifu_lineMeasure import *
from ifu_utils import *


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


def test_inputSpectra():
    """
    1. Test the input spectrum format.
    """
    
    testSpec = extractSpectrum(cube, [[30,30]], cals, region=None, iscontinuum=False, display=False)
    line = lineMeasure(testSpec[0, :], testSpec[2, :], region=[1.72, 1.77])
    assert len(line) > 0 and line[0] != 0
    
    
def test_inputRange():
    """
    2. Test the range input past limits.
    """
    
    testSpec = extractSpectrum(cube, [[30,30]], cals, region=None, iscontinuum=False, display=False)
    line = lineMeasure(testSpec[0, :], testSpec[1, :], region=[3000, 3100])
    assert line == []