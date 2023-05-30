from imgvar import augment_images
import numpy as np

images = np.array([ # 3 images, 2x2 pixels, rgb255
    [[[0, 0, 0], [1, 1, 1]],
    [[2, 2, 2], [3, 3, 3]]],
                
    [[[4, 4, 4], [5, 5, 5]],
    [[6, 6, 6], [7, 7, 7]]],
    
    [[[8, 8, 8], [9, 9, 9]],
    [[10, 10, 10], [11, 11, 11]]]
])

labels = np.array([ # 3 labels for each img
    ["verydark"],
    ["dark"],
    ["lessdark"]
])

print(type(labels[0])) # <class 'numpy.str_'>

new_images, new_labels = augment_images(images, labels, {"flip": ["horizontal", "vertical"]}, 1, label_verbose=1)

for i in range(len(new_images)):
    print(f"{new_labels[i]}: -------------------")
    print(new_images[i])
    print("-------------------\n")