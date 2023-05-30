import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_hue(img: numpy.ndarray, offset: int) -> numpy.ndarray:
    """
    Applies hue to target image.
    """
    pass