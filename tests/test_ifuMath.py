#Import necessary modules
import sys
sys.path.append('./scripts/')

from ifu_math import math
import numpy as np

# ======================================================
#                       Test suite
# ======================================================
def test_addIntConstant():
    """
    1. Addition with constant integer
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 10, 'add')
    assert result.shape == cube.shape
    
    
def test_addFloatConstant():
    """
    2. Addition with constant float
    """   
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 5., 'add')
    assert result.shape == cube.shape
    
    
def test_subIntConstant():
    """
    3. Subtraction with constant integer
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 10, 'subtract')
    assert result.shape == cube.shape
    
    
def test_subFloatConstant():
    """
    4. Subtraction with constant float
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 5., 'subtract')
    assert result.shape == cube.shape

    
def test_mulIntConstant():
    """
    5. Multiplication with integer
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 10, 'multiply')
    assert result.shape == cube.shape

    
def test_mulFloatConstant():
    """
    6. Multiplication with constant float
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 5., 'multiply')
    assert result.shape == cube.shape

    
def test_divIntConstant():
    """
    7. Division with constant integer
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 10, 'divide')
    assert result.shape == cube.shape
    
    
def test_divFloatConstant():
    """
    8. Division with constant float
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 5., 'divide')
    assert result.shape == cube.shape
    

def test_unsupportedMethod():
    """
    9. Test with unsupported method 'dummy'
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 5., 'dummy')
    assert result.shape == cube.shape

    
def test_unsupportedOperator():
    """
    10. Test with unsupported operator 'r'
    Operator must be a 1D/2D/3D array of int/float!
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, 'r', 'add')
    assert isinstance(result, np.ndarray), 'Operator cannot be a string!'

    
def test_cubeMinImage():
    """
    11. 3D/2D math operation
    Subtracting an image from a cube.
    """
    
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    image = cube[15, :, :]
    
    result = math(cube, image, 'subtract')
    assert isinstance(result, np.ndarray)
    
      
def test_diffDims():
    """
    12. Test with different dimensions
    """
    
    cube = np.arange(30*3*10).reshape(30, 3, 10)
    image = cube[15, :, :].reshape(5, 6)
    
    result = math(cube, image, 'divide')
    assert isinstance(result, np.ndarray)


def test_scalarInput():
    """
    13. Test with input scalar list 
    """
    
    in_list = np.arange(10)
    
    result = math(in_list, 10, 'add')
    assert isinstance(result, np.ndarray)


def test_cubeAndSpectrum():
    """
    14. 3D/1D test with an spectrum as the operator
    
    Create a 2D spectrum image the same size as the 
    frame in the cube.
    """
    
    spectrum = np.random.randint(0, 10, size=(30))
    cube = np.arange(30*5*5).reshape(30, 5, 5)
    
    result = math(cube, spectrum, method='subtract')    
    assert isinstance(result, np.ndarray)

# ======================================================
#                       Test suite
# ======================================================