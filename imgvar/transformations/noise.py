import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_noise(img: numpy.ndarray, rate: float, strength: float) -> numpy.ndarray:
    """
    Applies noise to target image.
    """
    pass