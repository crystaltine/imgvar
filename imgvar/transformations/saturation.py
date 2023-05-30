import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_saturation(img: numpy.ndarray, strength: float) -> numpy.ndarray:
    """
    Applies saturation to target image.
    """
    pass