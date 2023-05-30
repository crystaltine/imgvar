import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_rotation(img: numpy.ndarray, angle: float, fill_tolerance: float, crop: bool) -> numpy.ndarray:
    """
    Applies rotation to target image.
    """
    pass