from unittest import TestCase
from imgvar.main import augment_images
import numpy as np
import logging

class BrightnessTests(TestCase):
    def assert_numpy_array_equal(self, arr1, arr2):
        self.assertEqual(arr1.shape, arr2.shape)
        self.assertTrue(np.array_equal(arr1, arr2))
    
    def setUp(self) -> None:
        self.images = np.array([ # 3 images, 2x2 pixels, rgb255
            [[[0, 1, 2], [3, 4, 5]],
            [[6, 7, 8], [19, 20, 21]]],
                        
            [[[98, 97, 96], [125, 124, 123]],
            [[122, 121, 120], [69, 68, 67]]],
            
            [[[240, 250, 240], [245, 255, 245]],
            [[220, 230, 220], [160, 200, 160]]]
        ])
        self.labels = np.array([ # 3 labels for each img
            ["bluish-dark"],
            ["redish-medium"],
            ["greenish-bright"]
        ])
        
    def test_fully_brighten(self):
        new_images, new_labels = augment_images(self.images, self.labels, {"brightness": (1.0, 1.0)})
        
        self.assertEqual(new_images.shape, (6, 2, 2, 3))
        self.assertEqual(new_labels.shape, (6, 1))
        
        fullbright_2x2 = np.array([[[255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255]]])
        logging.debug(new_images[0])
        self.assert_numpy_array_equal(new_images[0], fullbright_2x2)
        
        
        