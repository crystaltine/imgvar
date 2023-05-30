import numpy as np

images = np.array([ # 3 images, 2x2 pixels, rgb255
    [[[0, 0, 0], [1, 1, 1]],
    [[2, 2, 2], [3, 3, 3]]],
                
    [[[4, 4, 4], [5, 5, 5]],
    [[6, 6, 6], [7, 7, 7]]],
    
    [[[8, 8, 8], [9, 9, 9]],
    [[10, 10, 10], [11, 11, 11]]]
])

images = np.round(images + 0.1*255)
print(images)