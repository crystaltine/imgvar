import numpy
from PIL import Image

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_flip(img: numpy.ndarray, dir: str) -> numpy.ndarray:
    """
    Flips images horizontally or vertically. This transformation will not be
    reapplied if `multiplier` is greater than 1.
    
    **Parameters**: `img`: `numpy.ndarray`, `dir`: `str` (`'horizontal'`, `'vertical'`)\n
    **Returns**: `numpy.ndarray` representing the image flipped on the selected axis
    """
    if dir == "horizontal":
        return numpy.flip(img, axis=1)
    elif dir == "vertical":
        return numpy.flip(img, axis=0)
    else:
        raise InvalidTransformationParameterError(dir, "flip")