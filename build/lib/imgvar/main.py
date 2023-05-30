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
from imgvar_keywords import KEYWORDS_FUNCTIONS
import imgvar_errors

def augment_images(images: numpy.ndarray, labels: numpy.ndarray, variations: dict, multiplier: int = 5) -> tuple[numpy.ndarray, numpy.ndarray]:
    """
    # Example Usage:
    ```
    train_images: numpy.ndarray = numpy.array(...)
    train_labels: numpy.ndarray = numpy.array(...)
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
        multiplier=5
    )
    ```
    
    `train_images`: original images. In this case, it's a numpy array of shape `(50000 (n), 32, 32, 3)`; Each image is represented by a 32x32x3 3d array, where each element of the 32x32 is an `(r, g, b)` tuple\n
    `train_labels`: original labels. In this case, it's a numpy array of shape `(50000 (n), 1)`. Augmented data should be inserted into the array adjacent to the original data (preferrably at indicies `i+1` -> `i+n`), and the labels should be copied accordingly.\n
    `variations` (Might change format): a dictionary of the variations to be applied to the images. The keys are the names of the variations, and the values represent parameters. For example, `brightness` corresponds to a tuple of floats `(min, max)` that represent the rangeof brightness values to be applied to the image. `flip` variation takes a list which can contain any subset of `["horizontal", "vertical"]`.\n
    `multiplier`: the number of variations to be applied to each image, per variation type. For example, if `multiplier = 5`, then each variation will be randomly applied 5 times to each image.\n
    """
    for var in variations:
        if var not in KEYWORDS_FUNCTIONS.keys():
            raise imgvar_errors.InvalidVariationError(var)
    if multiplier < 1:
        raise ValueError("Multiplier must be an integer greater than 0")
    
    # Apply variations (TODO)
    
    # Pretend only FLIP for now
    augmented_images = images
    augmented_labels = labels
    
    for var in variations:
        for i in range(len(images)-1, -1, -1): # iterate backwards so that the indicies don't get messed up
            # flip is a one-time variation (unaffected by multiplier)
            img = images[i]
            label = labels[i]
            func = KEYWORDS_FUNCTIONS[var]
            for var_param in variations[var]:
                augmented_images = numpy.insert(augmented_images, i+1, func(img, var_param), axis=0)
                numpy.insert(augmented_labels, i, label, axis=0)
    
    #for var in variations:
    #    augmented_images = []
    #    augmented_labels = []
    #    func = KEYWORDS_FUNCTIONS[var]
    #    args = {dir: KEYWORDS_TYPES[var]}
    #    for i in range(len(images)):
    #        for j in range(multiplier):
    #            augmented_images.append(func(images[i], **), variations[var]))
    #            augmented_labels.append(labels[i])
    #            if var in []:
    #                augmented_images.append(func(images[i], **args))
    #    images = numpy.concatenate((images, augmented_images))
    #    labels = numpy.concatenate((labels, augmented_labels))
    return (images, labels)
