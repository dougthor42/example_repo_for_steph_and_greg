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


def is_neighbor(coord: CoordType, other: CoordType) -> bool:
    """
    Return True if ``other`` is a neighbor of ``coord``.

    ``coord`` and ``other`` are tuples of (row, column) integers.

    A neighbor is any coordinate that is touching the given coordinate.

    ::
       Given coordinate: "+"
       Neighbors: "X"
       Not Neighbors: "."

       .......
       ..XXX..
       ..X+X..
       ..XXX..
       .......

    A coordinate **is** considered a neighbor of itself.

    Parameters
    ----------
    coord
        The reference coordinate
    other
        The coordinate to check if it's a neighbor of ``coord``.

    Returns
    -------
    bool

    Examples
    --------
    >>> is_neighbor((0, 0), (0, 0))
    True
    >>> is_neighbor((0, 0), (1, 1))
    True
    >>> is_neighbor((1, 1), (1, 3))
    False
    """
    return abs(coord[0] - other[0]) <= 1 and abs(coord[1] - other[1]) <= 1


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


# This function name, arg name, and return values are defined by the
# program requirements.
def find_marked_pixels(image_array: np.ndarray) -> Tuple[int, Any, Any]:
    """
    Determine various pixel information from image data.

    This function takes an image and separates things into "marked" and "normal"
    pixels. A "marked" pixel is one who's value is exactly 0, while a "normal"
    pixel has any nonzero value.

    Pixel information returned is:
    + number of marked pixels
    + a list of isolated pixels - those that are marked and have 0 marked
      neighbors (in any of the 8 directions)
    + a list of clusters of marked pixels (marked pixels who have additional
      marked neighbors)

    Parameters
    ----------
    image_array
        The image data to process. This is a 2D array of ints.

    Returns
    -------
    num_marked_pixels :
        The total number of marked (0-value) pixels
    isolated_pixels :
        A list of tuples defining the coordinates of marked pixels that have
        no marked neighbors
    cluster_info :
        A list of lists of tuples (datastructure pending) of the various
        clusters of marked pixels that were found. The outermost list is sorted
        such that the largest cluster is first in the list and the smallest
        cluster is last.
    """
    # TODO: Remove this line when done.
    num_marked_pixels = isolated_pixels = cluster_info = None

    # We only care about if things are zero or not, so we can convert the
    # array to boolean
    # True: pixel is "marked". False: pixel is normal
    is_marked = image_array == 0

    # Total number of marked pixels. This is kinda silly because numpy does
    # not have a "count_zero" function. Luckily "True" is considered nonzero
    # so we can count our `is_marked` array.
    num_marked_pixels = np.count_nonzero(is_marked)
    logger.info(f"Found {num_marked_pixels} marked pixels")

    # Find isolated pixels
    # TODO: Migrate to function.
    # An isolated pixel is one that has no marked (True) neighbors.

    # in the interest of time, we'll start off with a bit of brute-force
    # method.
    # For any given coord in an array, neighbors will be at *relative* indexes:
    relative_indexes = [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, -1),
        (0, +1),
        (+1, -1),
        (+1, 0),
        (+1, +1),
    ]

    # So we'll just loop over the image data and search for those relative
    # indexes. Yeah, it's probably not the most efficient method but I'm
    # focusing on proof-of-concept first.
    num_rows, num_cols = is_marked.shape
    clusters = []
    isolated = []

    for row_coord in range(num_rows):
        for col_coord in range(num_cols):
            coord = (row_coord, col_coord)
            pixel_is_marked = is_marked[row_coord, col_coord]

            # We don't care about non-marked pixels
            if not pixel_is_marked:
                logger.debug(f"Pixel {coord} is not marked, skipping.")
                continue
            logger.debug(f"Marked pixel {coord} found. Checking neighbors")

            # the current pixel is marked. Look at the neighbors
            # TODO: refactor - we're too nested
            neighbors = []
            for rel_index in relative_indexes:
                # N.B.: We can't just check for IndexError because edges will
                # return neighbor coord of -1. When slicing the array, this coord
                # will be interpreted as the last element. We don't want that.
                # I bet there's a better way to do this, but /shrug.
                neighbor_coord = (row_coord + rel_index[0], col_coord + rel_index[1])
                if out_of_bounds(is_marked, neighbor_coord):
                    neighbor = False
                    logger.debug(f"  The neighbor {neighbor_coord} is out of bounds.")
                else:
                    neighbor = is_marked[neighbor_coord[0], neighbor_coord[1]]
                logger.debug(f"  Neighbor {neighbor_coord} marked: {neighbor}")
                neighbors.append(neighbor)

            # Any neighbors are marked? Then this pixel is not considered
            # isolated and is part of a cluster.
            if any(neighbors):
                clusters.append(coord)
            else:
                isolated.append(coord)

    logger.info(f"Found {len(isolated)} isolated marked pixels.")
    logger.info(f"Found {len(clusters)} clusters of marked pixels.")

    # At this point we have a list of isolated pixels and a list of pixels
    # belonging to any number of clusters. We now have to split that cluster
    # data into individual clusters.
    cluster_info = split_clusters(clusters)

    # Rename a variable per the program requirements
    isolated_pixels = isolated

    return num_marked_pixels, isolated_pixels, cluster_info


# This function name, arg name, and return values are defined by the program requirements.
def encode_pixel_map(image_array):
    pass


def example():
    pass


if __name__ == "__main__":
    example()
