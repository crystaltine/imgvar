"""
A list of keywords (options) that are available for each variation type.
"""
from transformations.flip import apply_flip
from transformations.blur import apply_blur
from transformations.brightness import apply_brightness
from transformations.contrast import apply_contrast
from transformations.rotation import apply_rotation
from transformations.shift import apply_shift
from transformations.hue import apply_hue
from transformations.saturation import apply_saturation
from transformations.dropout import apply_dropout
from transformations.noise import apply_noise

KEYWORDS_FUNCTIONS = {
    "brightness": apply_brightness,
    "contrast": apply_contrast,
    "rotation": apply_rotation,
    "shift": apply_shift,
    "flip": apply_flip,
    "noise": apply_noise,
    "blur": apply_blur,
    "hue": apply_hue,
    "saturation": apply_saturation,
    "dropout": apply_dropout
}

KEYWORDS_ONE_APPLICATION = set([
    "flip"
])