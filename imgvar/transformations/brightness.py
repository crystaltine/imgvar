import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_brightness(img: numpy.ndarray, factor: float, absolute: bool = True) -> numpy.ndarray:
    """
    Applies brightness to target image.\n
    `factor`: -1 (full darkness) to 1 (full brightness) (0 is no change)\n
    `absolute`:\n
    + If `True`, adds `factor * 255` to each pixel.\n
    + If `False`:\n
        - If `factor < 0`, adds `factor * pixel_value` from each pixel. (decreases distance to black by a proportion)\n
        - If `factor > 0`, adds `factor * (255 - pixel_value)` to each pixel. (decreases distance to white by a proportion)\n
    """
    if factor < -1: factor = -1
    elif factor > 1: factor = 1
    
    if absolute: return numpy.round(img + factor * 255) # Absolute brightness
    
    else:
        if factor < 0: return numpy.round(img + factor * img) # Proportionally darken
        elif factor > 0: return numpy.round(img + factor * (255 - img)) # Proportionally brighten
    return img