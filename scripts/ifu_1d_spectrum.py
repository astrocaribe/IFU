# Global imports
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import sys
sys.path.append('./scripts/')
from ifu_math import *
from ifu_utils import *

def ifu_1d_spectrum(array_in, spaxel, cals, trim=100, continuum=False, display=False):
    """
    Extract the spectrum of a gixen spaxel from a given datacube.
    
    Parameters
    ----------
    array_in : numpy.ndarray
               Input datacube.
               
    spaxel : tuple of ints
             The spaxel (i.e., the [x, y] pixel location) for 
             which to perform the extraction.
             
    cals : tuple of floats
           Calibration values for the input datacube; 
           (crpix, crval, crdelt).
           
    trim : int
           Integer amount to trim from begin/end of the datacube.
           
    continuum : bool, optional
                Perforn a continuum subtraction (default is False, 
                no continuum subtraction is done).
    
    display : bool, optional
              Display the extracted spectrum (default is False,
              spectrum is not displayed).
    
    Returns
    -------
    spectrum : numpy.ndarray
               The extracted spectrum.
    """
    
    # Create an array of frame indeces from length of input array
    frame_range = np.arange(len(array_in))
        
    # Extract spectrum at given spaxel, trimming from beginning/end of spectrum
    spectrum = array_in[trim:-trim, spaxel[1], spaxel[0]]
    spec_frame = np.arange(len(spectrum)) + trim
    spec_wave = frame_convert(spec_frame, cals)
        
    # If a continuum-subtracted spectrum is required, calculate
    # and return...
    if continuum:
        #compute an estimate for the continuum
        p = np.polyfit(spec_wave, spectrum, 1)
        print('Gradient and y-intercept:')
        print(p)
        y = p[0] * spec_wave + p[1]
    
        #compute continuum-subtracted spectrum
        #z = spectrum - y
        spectrum = spectrum - y
    
    # Display spectrum if set (DEBUG)
    if display:
        
        fig, ax = plt.subplots(figsize=(10, 4))
        
        ax.set_xlim(spec_wave[0], spec_wave[-1])
        ax.plot(spec_wave, spectrum)
        ax.set_xlabel('Wavelength ($\mu m$)')
        
        ax_twin = ax.twiny()
        ticks = frame_range[::250]
        ax_twin.set_xticks(ticks, minor=True)
        ax_twin.set_xlabel('Datacube Frame')
            
    return spectrum