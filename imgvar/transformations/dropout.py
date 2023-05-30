import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_dropout(img: numpy.ndarray, rate: float) -> numpy.ndarray:
    """
    Applies dropout to target image.
    """
    pass