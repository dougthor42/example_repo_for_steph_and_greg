# -*- coding: utf-8 -*-
"""
FLIR Python Evaluation, test 2
"""
from pathlib import Path
from typing import Any
from typing import Tuple

import imageio
import numpy as np


def load_image_file(path: Path) -> np.ndarray:
    """
    Load a image file into a numpy array.

    Parameters
    ----------
    path :
        The path to the file.

    Returns
    -------
    image_data
        A 2D numpy array of image data.
    """
    image = imageio.imread(path)
    image_data = np.array(image)
    return image_data


# This function name, arg name, and return values are defined by the program requirements.
def find_marked_pixels(image_array: np.ndarray) -> Tuple[int, Any, Any]:
    pass


# This function name, arg name, and return values are defined by the program requirements.
def encode_pixel_map(image_array):
    pass


def example():
    pass


if __name__ == "__main__":
    example()
