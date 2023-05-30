KEYWORDS_TYPES = {
    "brightness",
    "contrast",
    "rotation",
    "shift",
    "flip",
    "noise",
    "blur",
    "hue",
    "saturation",
    "dropout"
}

class InvalidVariationKeywordError():
    """Raised when an image variance type is invalid (not recognized by the module)"""
    def __init__(self, incorrect_param: str):
        self.message = f"Variation {incorrect_param} transformation doesn't exist! \
            \nValid transformations are: {KEYWORDS_TYPES}"
        super().__init__(self.message)

class InvalidTransformationParameterError():
    """Raised when a parameter for a transformation is invalid (i.e. invalid keyword, range value, etc.)"""
    def __init__(self, incorrect_param, transformation_name: str):
        self.message = f"Invalid  parameter '{incorrect_param}' for transformation '{transformation_name}'"
        # Add param template list (e.g. "brightness": (min: float, max: float))
        super().__init__(self.message)