# -*- coding: utf-8 -*-
import numpy as np

# example_image_array from flir_test_skeleton.py
EXAMPLE_IMAGE = np.array(
    [
        [0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
    ],
    dtype=np.uint32,
)
