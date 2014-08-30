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
               
    spaxel : list of ints, [[x, y]] or [[x1, y1], [x2, y2] ... [xn, yn]]
             The spaxel(s) (i.e., the [x, y] pixel location) for 
             which to perform the extraction.
             
    cals : list of floats
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
    spectrum_out : numpy.ndarray
               The extracted spectrum. The output is a 2d array, 
               where spectrum_out[0, :] is the wavelength (in $/mu $m) 
               and spectrum_out[1, :] is the counts (in D/N).
    """
        
    # Convert spaxel(s) to numpy arrays to evaluate how many are input, 
    # and unpack into seperate values
    spaxelList = np.array(spaxel)
    if spaxelList.shape[1] > 2:
        print('Input spaxels not in the right form. Resizing....')
        #npSpaxels = np.resize(spaxelList, (spaxelList.shape[1], spaxelList.shape[0]))
        npSpaxels = spaxelList.T
        print('Resizing done!')
        print()
    else:
        npSpaxels = spaxelList
    
    x, y = [], []
    for (ii, jj) in npSpaxels:
        x.append(ii)
        y.append(jj)
    
    # If too many spaxels entered, display a message (limit x)
    specLimit = 3
    if npSpaxels.shape[0] > specLimit:
        print('Too many spectra entered! Maximum of 3 will be processed...')


    # Extract spectrum at given spaxel, trimming from beginning/end of spectrum
    #spectrum = array_in[trim:-trim, spaxel[1], spaxel[0]]
    spectrum = array_in[trim:-trim, y[:specLimit], x[:specLimit]]
    if spectrum.shape[1] == 1:
        spectrum = spectrum[:, 0]
    
    spec_frame = np.arange(len(spectrum)) + trim    
    spec_wave = frame_convert(spec_frame, cals)
        
    # If a continuum-subtracted spectrum is required, calculate
    # and return...
    if continuum:                
        pTemp = np.polyfit(spec_wave, spectrum, 1)
        
        if spectrum.ndim == 1:
            p = pTemp
            continuum = p[0] * spec_wave + p[1]
        else:
            p = pTemp.T
            continuum = np.zeros(spectrum.shape)
            for rec, pfit in enumerate(p):
                continuum[:, rec] = pfit[0] * spec_wave + pfit[1]

        # Compute continuum-subtracted spectrum
        spectrum = spectrum - continuum
        
    # Display spectrum if set (DEBUG)
    if display:
        
        fig, ax = plt.subplots(figsize=(12, 4))

        if len(x) > 1:
            for rec, pos in enumerate(npSpaxels):
                ax.plot(spec_wave, spectrum[:, rec], label='[{}, {}]'.format(pos[0], pos[1]))
        else:
            ax.plot(spec_wave, spectrum, label='[{}, {}]'.format(x[0], y[0]))
        
        
        ax.set_xlim(spec_wave[0], spec_wave[-1])
        ax.set_xlabel('Wavelength ($\mu m$)')
        ax.set_ylabel('Counts (D/n)')
        
        ax_twin = ax.twiny()
        ax_twin.set_xlim(spec_frame[0], spec_frame[-1])
        ticks = spec_frame[::100]
        ax_twin.set_xticks(ticks, minor=True)
        ax_twin.set_xlabel('Datacube Frame')
        
        # Now add the legend with some customizations.
        ax.legend(loc='best', numpoints = 1, shadow=True)
        
    # Create an empty multidim array to store the spectral data
    # (wavelength and flux)
    # If multiple spaxles are entered, only the first is returned!    
    spectrum_out = np.empty(2*spectrum.shape[0]).reshape(2, spectrum.shape[0])
    spectrum_out[0, :] = spec_wave
    #spectrum_out[1, :] = spectrum
    
    if len(spectrum.shape) != 1:
        spectrum_out[1, :] = spectrum[:, 0]
    else:
        spectrum_out[1, :] = spectrum
                
    return spectrum_out