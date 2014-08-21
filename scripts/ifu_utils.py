# Global imports
import numpy as np

def frame_convert(frame, cals):
    """ 
    Convert the frame to a wavelength using a starting value and 
    delta (in microns).
    
    Parameters
    ----------
    frame : int
        Datacube frame to convert to a wavelength.
    
    cals : tuple of ints
        Calibration constants for the given datacube.
        
    Returns
    -------
    wave : float
        The converted wavelength of the datacube frame.
        
    Raises
    ------
    Not yet implemented.
    """
    
    # Calculate the frame conversion
    wave = (frame - cals[0]) * cals[2] + cals[1]
    
    return wave # [format(z, '.3f') for z in wave] #

def wave_convert(wave, cals):
    """
    Convert the wavelength to a frame using a starting value and 
    delta (in microns).
    
    Parameters
    ----------
    wave : float
        The wavelength to convert to a datacube frame.
    
    cals : tuple of ints
        Calibration constants for the given datacube.
        
    Returns
    -------
    frame : int
        Datacube frame to converted from the input wavelength.
        
    Raises
    ------
    Not yet implemented.
    """
    
    from numpy import round
    from numpy import int

    # Calculate the wavelength conversion
    frame = cals[0] + ((wave - cals[1]) / cals[2])
    
    frame = np.int(np.round(frame))
    return frame