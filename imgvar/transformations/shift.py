import numpy
import PIL
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'imgvar\imgvar')))
from imgvar_errors import InvalidTransformationParameterError, InvalidVariationKeywordError

def apply_shift(img: numpy.ndarray, dir: str, offset: int) -> numpy.ndarray:
    """
    Applies shift to target image.
    """
    pass