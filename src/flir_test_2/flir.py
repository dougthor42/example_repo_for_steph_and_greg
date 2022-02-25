# -*- coding: utf-8 -*-
"""
FLIR Python Evaluation, test 2
"""
from pathlib import Path
from typing import Any
from typing import Tuple

import imageio
import numpy as np

from flir_test_2.custom_types import CoordType


def out_of_bounds(array: np.ndarray, coord: CoordType) -> bool:
    """
    Check if a coordinate is out of bounds of an array.
    """
    row_coord, col_coord = coord
    num_rows, num_cols = array.shape
    is_out_of_bounds = (
        row_coord < 0 or col_coord < 0 or row_coord >= num_rows or col_coord >= num_cols
    )
    return is_out_of_bounds


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
