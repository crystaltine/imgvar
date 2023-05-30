# Example usage for new module imgvar:
# import imgvar
#
# (train_images, train_labels), (test_images, test_labels) = cifar10.load_data() # returns (q_train, a_train), (q_test, a_test)
# train_images, test_images = train_images / 255.0, test_images / 255.0
#
# variation_types = {
#   "brightness": (0.8, 1.2), 
#   "contrast": (0.8, 1.2), 
#   "rotation": (-10, 10) 
#   "shift": (-10, 10), 
#   "flip": True
# }
# train_images_with_variation = imgvar.augment_images(data=train_images, labels=train_labels, variations=variation_types, multiplier=5)
#
# train_images: original images. In this case, it's a numpy array of shape (50000 (n), 32, 32, 3)
# *** Each image is represented by a 32x32x3 3d array, where each element of the 32x32 is an (r, g, b) tuple ***
#
# train_labels: original labels. In this case, it's a numpy array of shape (50000 (n), 1). Augmented data should be inserted into the
#               array adjacent to the original data (preferrably at indicies i + 1 -> i + n), and the labels should be copied accordingly.
# variations (Might change format): a dictionary of the variations to be applied to the images. The keys are the names of the variations, and the values 
#             represent parameters. For example, the "brightness" variation takes a tuple of floats (min, max) that represent the range
#             of brightness values to be applied to the image. The "flip" variation takes a boolean value just to indicate its existence.
# multiplier: the number of variations to be applied to each image, per variation type. For example, if multiplier = 5, then each
#                 variation will be randomly applied 5 times to each image. 

import numpy
from .imgvar_keywords import KEYWORDS_FUNCTIONS, KEYWORDS_ONE_APPLICATION
from .imgvar_errors import InvalidVariationKeywordError, InvalidTransformationParameterError

def augment_images(
    images: numpy.ndarray,
    labels: numpy.ndarray, 
    variations: dict,
    excludes: dict = {}, 
    multiplier: int = 1, 
    combine: bool = False,
    label_verbose: int = 0
) -> tuple[numpy.ndarray, numpy.ndarray]:
    """
    Augments images and labels with specified variations. Returns a tuple of the augmented images and labels.
    See README and other docs on how to format the variations dictionary. Below is a list of parameters.
    
    `train_images`: original images. For example, a numpy array of shape `(50000, 32, 32, 3)`; Each image is represented by a 32x32x3 3d array, where each element of the 32x32 is an `(r, g, b)` tuple\n
    `train_labels`: original labels. In this case, it's a numpy array of shape `(50000, 1)`. Augmented data should be inserted into the array adjacent to the original data (preferrably at indicies `i+1` -> `i+n`), and the labels should be copied accordingly.\n
    `variations` (Might change format): a dictionary of the variations to be applied to the images. The keys are the names of the variations, and the values represent parameters. For example, `brightness` corresponds to a tuple of floats `(min, max)` that represent the rangeof brightness values to be applied to the image. `flip` variation takes a list which can contain any subset of `["horizontal", "vertical"]`.\n
    `excludes` (Might change format): specifies some labels which should not receive some variations. Keys should be variation types and values should be lists of excluded labels. For example, `{"flip": ["dog", "cat"]}` would mean that no dogs or cats should be flipped.\n
    `multiplier`: the number of variations to be applied to each image, per variation type. For example, if `multiplier = 5`, then each variation will be randomly applied 5 times to each image.\n
    `combine`: Toggles whether or not variations should apply to images that already have variations applied (i.e. should already flipped images also be blurred, shifted, etc)\n
    `label_verbose`: If 1, the returned labels array will have extra info about the variation used. If 0 (default), just the labels will be returned (recommended for training). For example, verbose 1 labels could be something like [airplane, airplane-flip_horizontal, airplane-flip_vertical, etc.] while verbose 0 labels would just be [airplane, airplane, airplane, etc.]
    
    # Example Usage:
    ```
    train_images: numpy.ndarray = numpy.array(...) # get train images from somewhere
    train_labels: numpy.ndarray = numpy.array(...) # get train labels from somewhere
    
    variation_types = {
        "brightness": (0.8, 1.2),
        "contrast": (0.8, 1.2), 
        "rotation": (-10, 10) 
        "shift": (-10, 10), 
        "flip": ["horizontal"]
    }
    train_images_with_variation = imgvar.augment_images(
        data=train_images, 
        labels=train_labels, 
        variations=variation_types, 
        excludes={}
        multiplier=3,
        combine=False,
        label_verbose=0
    )
    ```
    """
    for var in variations:
        if var not in KEYWORDS_FUNCTIONS.keys():
            raise InvalidVariationKeywordError(var)
    if multiplier < 1:
        raise ValueError("Multiplier must be an integer greater than 0")
    
    # Apply variations (TODO)
    augmented_images = images
    augmented_labels = labels.astype("object")
    
    if not combine:
        for i in range(len(images)-1, -1, -1): # iterate backwards so that the indicies don't get messed up
            img = images[i]
            label = labels[i]
            
            img_variations = []
            label_variations = []
            
            for var in variations:
                # flip is a one-time variation (unaffected by multiplier)
                func = KEYWORDS_FUNCTIONS[var]
                
                if type(variations[var]) == tuple: # range of parameters (select random in range)
                    for j in range(multiplier):
                        
                        var_param = numpy.random.uniform(variations[var][0], variations[var][1])
                        
                        img_variations.append(func(img, var_param))
                        
                        # TODO: Add info returning to all variation functions to return concise variation descriptions
                        if label_verbose == 0: label_variations.append(label)
                        else: label_variations.append([f"{label[0]}-{var}_{var_param}"])
                        
                        if var in KEYWORDS_ONE_APPLICATION: break
                            
                elif type(variations[var]) == list: # list of types of variations
                    for var_param in variations[var]:
                        for j in range(multiplier):
                            img_variations.append(func(img, var_param))
                            
                            # TODO: Add info returning to all variation functions to return concise variation descriptions
                            if label_verbose == 0: label_variations.append(label)
                            else: label_variations.append([f"{label[0]}-{var}_{var_param}"])
                            
                            if var in KEYWORDS_ONE_APPLICATION: break

            augmented_images = numpy.insert(augmented_images, i+1, img_variations, axis=0)            
            augmented_labels = numpy.insert(augmented_labels, i+1, label_variations, axis=0)
                
    else: # TODO
        for var in variations:
            for var_param in variations[var]:
                for i in range(len(augmented_images)-1, -1, -1): # iterate backwards so that the indicies don't get messed up
                    # flip is a one-time variation (unaffected by multiplier)
                    img = augmented_images[i]
                    label = augmented_labels[i]
                    func = KEYWORDS_FUNCTIONS[var]
                    
                    augmented_images = numpy.insert(augmented_images, i+1, func(img, var_param), axis=0)
                    augmented_labels = numpy.insert(augmented_labels, i, label, axis=0)
                    
    return (augmented_images, augmented_labels)
