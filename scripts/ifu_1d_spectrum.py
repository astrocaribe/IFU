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
        npSpaxels = np.resize(spaxelList, (spaxelList.shape[1], spaxelList.shape[0]))
        print('Resizing done!')
        print()
    else:
        npSpaxels = spaxelList
    
    x, y = [], []
    for (ii, jj) in npSpaxels:
        x.append(ii)
        y.append(jj)
       
    print('Spaxel shape! ', npSpaxels.shape)
    print('x Spaxels: ', x)
    print('y Spaxels: ', y)    
    
    # If too many spaxels entered, display a message (limit x)
    specLimit = 3
    if npSpaxels.shape[0] > specLimit:
        print('Too many spectra entered! Maximum of 3 will be processed...')
        
    #if npSpaxels.shape[1] > 2:
    #    print('Spaxel values must be entered in pairs! (e.g. spaxel=[[x1, y1], [x2, y2]])')
    #    return None
                
    # Extract spectrum at given spaxel, trimming from beginning/end of spectrum
    #spectrum = array_in[trim:-trim, spaxel[1], spaxel[0]]
    spectrum = array_in[trim:-trim, y[:specLimit], x[:specLimit]]
    if spectrum.shape[1] == 1:
        print('Shape change!!!!')
        spectrum = spectrum[:, 0]
    
    spec_frame = np.arange(len(spectrum)) + trim    
    spec_wave = frame_convert(spec_frame, cals)
        
    print('Spectrum.shape: ', spectrum.shape)
    print('Spec_frame.shape: ', spec_frame.shape)
    print('Spec_wave.shape: ', spec_wave.shape)
    
    # If a continuum-subtracted spectrum is required, calculate
    # and return...
    if continuum:        
        #compute an estimate for the continuum
        #p = np.polyfit(spec_wave, spectrum, 1)
        
        pTemp = np.polyfit(spec_wave, spectrum, 1)
        print('(continuum) pTemp.shape: ', pTemp.shape)
        
        if spectrum.ndim == 1:
            p = pTemp
            continuum = p[0] * spec_wave + p[1]
        else:
            p = np.resize(pTemp, (pTemp.shape[1], pTemp.shape[0]))
            print('(continuum) spec_wave.shape: ', spec_wave.shape)
            print('(continuum) p.shape: ', p.shape)
            continuum = np.zeros(spectrum.shape)
            for rec, (p0, p1) in enumerate(p):
                print('polyfit test...')
                continuum[:, rec] = p0 * spec_wave + p1
        

        print('(continuum) p.shape: ', p.shape)
        print('(continuum) p: ', p)        
        print('Gradient and y-intercept:')
        #continuum = p[:, 0] * spec_wave + p[:, 1]
        

        print('(continuum) Continuum shape: ', continuum.shape)
        print('(continuum) Spectrum.shape: ', spectrum.shape)
        print('(continuum) Spectrum type: ', type(spectrum))
        
        #compute continuum-subtracted spectrum
        #z = spectrum - y
        spectrum = spectrum - continuum
        
        print('(continuum2) Spectrum.shape: ', spectrum.shape)
    
    # Display spectrum if set (DEBUG)
    if display:
        
        fig, ax = plt.subplots(figsize=(12, 4))
        
        ax.set_xlim(spec_wave[0], spec_wave[-1])
        ax.plot(spec_wave, spectrum)
        ax.set_xlabel('Wavelength ($\mu m$)')
        ax.set_ylabel('Counts (D/n)')
        
        ax_twin = ax.twiny()
        ax_twin.set_xlim(spec_frame[0], spec_frame[-1])
        ticks = spec_frame[::100]
        ax_twin.set_xticks(ticks, minor=True)
        ax_twin.set_xlabel('Datacube Frame')
        
    # Create an empty multidim array to store the spectral data
    # (wavelength and flux)
    # If multiple spaxles are entered, only the first is returned!
    print('(after:) Spetrum.shape: ', spectrum.shape)
    
    spectrum_out = np.empty(2*spectrum.shape[0]).reshape(2, spectrum.shape[0])
    spectrum_out[0, :] = spec_wave
    #spectrum_out[1, :] = spectrum
    
    if len(spectrum.shape) != 1:
        spectrum_out[1, :] = spectrum[:, 0]
    else:
        spectrum_out[1, :] = spectrum
                
    return spectrum_out