import numpy
import PIL

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_blur(img: numpy.ndarray, radius: int) -> numpy.ndarray:
    """
    Blurs the image with a gaussian blur of radius `radius`. This transformation will not be
    reapplied if `multiplier` is greater than 1.
    
    **Parameters**: `img`: `numpy.ndarray`, `radius`: `int`\n
    **Returns**: `numpy.ndarray` representing the image blurred with a gaussian blur of radius `radius`
    """
    return img.filter(PIL.ImageFilter.GaussianBlur(radius=radius))