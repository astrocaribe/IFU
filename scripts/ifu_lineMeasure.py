# Global imports
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def ifu_lineMeasure(spectrum, region=[], display=False):
    """
    Measure the line (if present) in a given region of an 
    input spectrum.
    
    Parameters
    ----------
    spectrum : numpy.ndarray
               Input spectrum as a 1D array.
               
    region : tuple of ints, optional
             The region for which to measure the line.
             (default is [], in which the entire spectrum
             is used.)
             
    display : bool, optinal
              Display the line with diagnostic values.
              (default is False, diagnostic values displayed 
              to screen).
    
    Returns
    -------
    line : tuple of floats
           Line location (wavelength), FWHM, and intensity.
    
    """
    inSpectrum = 0
    
    if len(region) == 2:
        inSpectrum = spectrum[region[0]:region[1]]
    else:
        print('The spectral region must be entered as [a, b], \
        where a and b are the lower/upper limits!')
    
    return inSpectrum