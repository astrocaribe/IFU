# Global imports
import numpy as np

def frame_convert(frame, cals):
    ''' 
    Convert the frame to a wavelength using a starting value and 
    delta (in microns) specific to the NGC4151_Hband.fits file
    '''
    
    # Calculate the frame conversion
    wave = (frame - cals[0]) * cals[2] + cals[1]
    
    return wave # [format(z, '.3f') for z in wave] #

def wave_convert(wave, cals):
    '''
    Convert the wavelength to a frame using a starting value and 
    delta (in microns) specific to the NGC4151_Hband.fits file 
    '''
    
    from numpy import round
    from numpy import int

    # Calculate the wavelength conversion
    frame = cals[0] + ((wave - cals[1]) / cals[2])
    
    frame = np.int(np.round(frame))
    return frame