import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_contrast(img: numpy.ndarray, factor: float) -> numpy.ndarray:
    """
    Applies constrast to target image.
    """
    pass