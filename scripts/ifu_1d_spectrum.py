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
    '''
    Description:
    '''
    
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
        
        ax.set_xlim(0, array_in.shape[0])
        ax.plot(spec_frame, spectrum)
        ax.set_xlabel('Datacube Frame ($z$)')
        ax.set_ylabel('Counts')
        
        ax_twin = ax.twiny()
        ticks = frame_range[::500]
        ax_twin.set_xticks(ticks, minor=True)
        ax_twin.set_xticklabels(np.round(frame_convert(ticks, cals), 3))
        ax_twin.set_xlabel('Wavelength ($\mu m$)')
            
    return spectrum