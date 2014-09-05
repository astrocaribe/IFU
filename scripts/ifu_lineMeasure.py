# Global imports
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from astropy.modeling import models, fitting

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
    line, inSpectrum = [], []
    
    idx, = np.where((spectrum[0, :] >= region[0]) & (spectrum[0, :] <= region[1]))

    if region[0] >= spectrum[0, 0] and region[1] <= spectrum[0, -1]:
        print('Indeces: ', idx[0], idx[-1])
        print('Wavelength range: ', spectrum[0, idx[0]], spectrum[0, idx[-1]])
        inWave = spectrum[0, idx[0]:idx[-1]]
        inFrame = spectrum[1, idx[0]:idx[-1]]
        inSpectrum = spectrum[2, idx[0]:idx[-1]]
        
    else:    
        print('Wavelength range is outside that available:')
        print('Input spectrum range: ', spectrum[0, 0], spectrum[0, -1])
        return line


    # Initial parameter guesses
    amp_0 = inSpectrum.max()
    index, = np.where(inSpectrum == amp_0)
    mean_0 = inWave[index[0]]


    # Fit the data using a Gaussian
    g_init = models.Gaussian1D(amplitude=0., mean=mean_0, stddev=3.)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g(g_init, inWave, inSpectrum)

    print(g)
    
    
    # Display spectrum if set (DEBUG)
    if display:
        
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(inWave, inSpectrum, color='green', lw=2., label = 'Spectrum')
        
        
        # Plot gaussian fit
        ax.plot(inWave, g(inWave), color='red', lw=1., label='Gauss')
        xl = g.mean.value
        yl = ax.get_ylim()
        ax.plot([xl, xl], yl, color='black', lw=1.5, ls='--', label='Line Location')
        print('Limits: ', g.mean.value, yl)
        
        ax.set_xlim(inWave[0], inWave[-1])
        ax.set_xlabel('Wavelength ($\mu m$)')
        ax.set_ylabel('Counts (D/n)')
        
        ax_twin = ax.twiny()
        ax_twin.set_xlim(inFrame[0], inFrame[-1])
        ax_twin.set_xlabel('Datacube Frame')

        # Now add the legend with some customizations.
        ax.legend(loc='best', numpoints = 1, shadow=True)

    
    line = np.empty(2*len(inWave)).reshape(2, len(inWave))
    line[0, :] = inWave
    line[1, :] = inSpectrum
    return line


if __name__ == "__main__":
    lineMeasure(spectrum, region=[], display=False)