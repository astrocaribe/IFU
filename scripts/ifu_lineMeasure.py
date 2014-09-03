# Global imports
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import sys
sys.path.append('./scripts/')
from ifu_utils import frame_convert, wave_convert


def lineMeasure(spectrum, region=[], display=False):
    """
    Measure the line (if present) in a given region of an 
    input spectrum.
    
    Parameters
    ----------
    spectrum : 2D numpy.ndarray
               Input spectrum as a 2D array; 
               spectrum[0] = wavelength
               spectrum[1] = frames
               spectrum[2] = counts
               
    region : list of ints, optional
             The region for which to measure the line.
             (default is [], in which the entire spectrum
             is used.)
             
    display : bool, optinal
              Display the line with diagnostic values.
              (default is False, diagnostic values displayed 
              to screen).
    
    Returns
    -------
    line : list of floats
           Line location (wavelength), FWHM, and intensity.
    
    """
    # Initialize the output spectrum
    # If zero, then something went wrong!
    line = 0
    
    idx, = np.where(spectrum[1, :] == region[0])
    print(idx, type(idx))
    
    if len(idx) == 0:
        print('Input range is outside allowed!')
        return line
    else:
        idx_range = region[1] - region[0]        
        
    
    if spectrum.shape[0] != 3:
        print("Spectrum must be of shape (3, n), when n = number of wavelengths/counts in spectrum!")
        
        return inSpectrum
    
    if len(region) == 2:
        inSpectrum = spectrum[2, idx:idx+idx_range]
    else:
        print('The spectral region must be entered as [a, b], where a and b are the lower/upper limits!')
    
    line = inSpectrum
    return line


if __name__ == "__main__":
    lineMeasure(spectrum, region=[], display=False)