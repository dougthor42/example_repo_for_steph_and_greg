# -*- coding: utf-8 -*-
"""
FLIR Python Evaluation, test 2
"""
from pathlib import Path
from typing import Any
from typing import List
from typing import Tuple

import imageio
import numpy as np

from loguru import logger

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


def split_clusters(cluster_data: List[CoordType]) -> List[List[CoordType]]:
    """
    Split out a single list of coords representing N clusters into N lists.

    The input ``cluster_data`` is a list of ``(row, col)`` tuples. For each point
    in the input data, we look for any other coord that is neighboring that
    coord. If no neighbors are found, that point is removed and set aside in
    a separate list.
    """
    logger.info("Splitting out clusters.")

    # WIP
    return [
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (3, 4),
            (4, 3),
            (4, 4),
            (5, 2),
            (5, 5),
            (6, 1),
            (6, 6),
            (7, 0),
            (7, 7),
        ],
        [(0, 7), (1, 6)],
    ]


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
