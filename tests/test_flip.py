from unittest import TestCase
from imgvar.main import augment_images
import numpy as np

class FlipTests(TestCase):
    def assert_numpy_array_equal(self, arr1, arr2):
        self.assertEqual(arr1.shape, arr2.shape)
        self.assertTrue(np.array_equal(arr1, arr2))
    
    def setUp(self) -> None:
        self.images = np.array([ # 3 images, 2x2 pixels, rgb255
            [[[0, 0, 0], [1, 1, 1]],
            [[2, 2, 2], [3, 3, 3]]],
                        
            [[[4, 4, 4], [5, 5, 5]],
            [[6, 6, 6], [7, 7, 7]]],
            
            [[[8, 8, 8], [9, 9, 9]],
            [[10, 10, 10], [11, 11, 11]]]
        ])
        self.labels = np.array([ # 3 labels for each img
            ["verydark"],
            ["dark"],
            ["lessdark"]
        ])
        
        return super().setUp()

    def test_horizontal_flip(self):
        new_images, new_labels = augment_images(self.images, self.labels, {"flip": ["horizontal"]})
        
        self.assertEqual(new_images.shape, (6, 2, 2, 3))
        self.assertEqual(new_labels.shape, (6, 1))
        
        horiz_flip_img1 = np.array([[[1, 1, 1], [0, 0, 0]], [[3, 3, 3], [2, 2, 2]]])
        self.assert_numpy_array_equal(new_images[1], horiz_flip_img1)
        
    def test_vertical_flip(self):
        new_images, new_labels = augment_images(self.images, self.labels, {"flip": ["vertical"]})
        
        self.assertEqual(new_images.shape, (6, 2, 2, 3))
        self.assertEqual(new_labels.shape, (6, 1))
        
        vert_flip_img1 = np.array([[[2, 2, 2], [3, 3, 3]], [[0, 0, 0], [1, 1, 1]]])
        self.assert_numpy_array_equal(new_images[1], vert_flip_img1)
    
    def test_both_flips(self):      
        new_images, new_labels = augment_images(self.images, self.labels, {"flip": ["horizontal", "vertical"]})
        
        self.assertEqual(new_images.shape, (9, 2, 2, 3))
        self.assertEqual(new_labels.shape, (9, 1))
        
        vert_flip_img1 = np.array([[[2, 2, 2], [3, 3, 3]], [[0, 0, 0], [1, 1, 1]]])
        horiz_flip_img1 = np.array([[[1, 1, 1], [0, 0, 0]], [[3, 3, 3], [2, 2, 2]]])
        self.assert_numpy_array_equal(new_images[1], horiz_flip_img1)
        self.assert_numpy_array_equal(new_images[2], vert_flip_img1)
        
        labels = np.array([["verydark"], ["verydark"], ["verydark"], ["dark"], ["dark"], ["dark"], ["lessdark"], ["lessdark"], ["lessdark"]])
        self.assert_numpy_array_equal(labels, new_labels)