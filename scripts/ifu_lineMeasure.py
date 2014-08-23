# Global imports
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import sys
sys.path.append('./scripts/')

def ifu_1d_spectrum(spectrum, region=[], display=False):
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
    
    return line