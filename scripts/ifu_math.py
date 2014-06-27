#Global imports
import numpy as np
from astropy.io import fits

# Basic ifu math mode
def ifu_math(array_in, operator, method):
    """
    Perform basic arithmetic tasks on 3D data using 1D, 2D, or
    3D data as input.
    
    Keyword arguments:
    array_in  -- The 3D input array.
    
    operator  -- The array that is to operate on the input array
                 (array_in). Can be a scalar, list, image, or
                 datacube.
                
    method    -- Calculation method. Available are add, subtract,
                 multiply, and divide.
    
    
    Output(s):
    array_out -- The list, image or cube subtracted output array.
    
    Example usage:
    
        1. >> ifu_math(cube, 1000., method='subtract')
        
        Subtract the scalar value of 1000. from entire cube array.
        
        2. >> ifu_math(cube, image, method='subtract')
        
        Subtract an image of dimensions [x, y] from a cube array in
        the wavelength (z) plane. Image dimensions x, y] must match
        those of the input cube array.
        
        3. >> ifu_math(cube1, cube2, method='divide')
        
        Divive cube1 array by the contents of cube2 array, value for
        value. Arrays of both cubes must be identical.
        
    """    
    
    import numpy as np
    
    # Check to see if operator is a scalar (int or float); convert to numpy
    # list to allow shape determination
    
    #print()
    #print(operator, type(operator))
    #print()
    
    if isinstance(operator, np.ndarray):
        print('The operator dimensions are: {}'.format(np.shape(operator)))
    else:
        print('Input has been converted to a numpy array.')
        operator = np.array([operator])
        print('The operator dimensions are: {}'.format(np.shape(operator)))
    
    
    # Assure that the input array is a cube
    if array_in.ndim != 3:
        print('The input array must be a cube (3 dimensions)!')
        return
    else:
        print('Input array has {} dimensions.'.format(array_in.ndim))
    
    # ... and check dimensions of input and operator arrays    
    if operator.ndim == 1 and operator.shape[0] == 1:
        print('A scalar operation will take place.')
    elif operator.shape == array_in.shape:
        print('A 3D/3D operation will take place.')
    elif operator.ndim == 2 and (operator.shape[0] == array_in.shape[1] and operator.shape[1] == array_in.shape[2]):
        print('A 3D/2D operation will take place.')
    elif operator.ndim == 1 and operator.shape[0] > 1:
        # Create a spectrum 'image' to conduct the basic arithmetic functions
        print('A 3D/1D operation will take place.')
        spec_image = np.empty(array_in.shape)
        for ii in np.arange(array_in.shape[0]):
            spec_image[ii, :, :] = operator[ii]
            
        operator = spec_image
    else:
        print('Dimension of input array and operator do not match!')
    
    
    if method == 'add':
        print('IFU add mode chosen...')
        array_out = np.add(array_in, operator)            
    
    elif method == 'subtract':
        print('IFU subtract mode chosen...')
        array_out = np.subtract(array_in, operator)
    
    elif method == 'multiply':
        print('IFU multiply mode chosen...')
        array_out = np.multiply(array_in, operator)
    
    elif method == 'divide':
        print('IFU divide mode chosen...')
        array_out = np.divide(array_in, operator)
        
    else:
        print('There has been an input parse error, please check inputs again!')
        array_out = np.array([])
    
    return array_out