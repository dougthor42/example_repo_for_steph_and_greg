# -*- coding: utf-8 -*-
"""
"""
import numpy as np
import pytest

from . import DATA_DIR
from .conftest import EXAMPLE_IMAGE
from flir_test_2 import flir


# Assumes a 5x5 array
@pytest.mark.parametrize(
    "coord, want",
    [
        ((-1, 4), True),
        ((2, 2), False),
        ((3, 8), True),
        ((-4, -4), True),
        ((-1, -1), True),
        ((7, 0), True),
        ((0, 0), False),
    ],
)
def test_out_of_bounds(coord, want):
    array = np.zeros((5, 5))
    got = flir.out_of_bounds(array, coord)
    assert got == want


@pytest.mark.parametrize(
    "coord, other, want",
    [
        ((0, 0), (0, 0), True),
        ((1, 1), (0, 0), True),
        ((1, 0), (0, 0), True),
        ((0, 1), (0, 0), True),
        ((0, 0), (0, 2), False),
        ((1, 1), (1, 3), False),
        ((5, 9), (6, 9), True),
        ((5, 9), (7, 3), False),
    ],
)
def test_is_neighbor(coord, other, want):
    got = flir.is_neighbor(coord, other)
    assert got == want


# TODO: Better parameter organization
@pytest.mark.parametrize(
    "data, want",
    [
        (
            [
                (0, 0),
                (0, 7),
                (1, 1),
                (1, 6),
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
            [
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
            ],
        )
    ],
)
def test_split_clusters(data, want):
    got = flir.split_clusters(data)
    assert got == want
    pass


@pytest.mark.parametrize("path", [DATA_DIR / "pathbpm.tif"])
def test_load_image_file(path):
    rv = flir.load_image_file(path)
    assert isinstance(rv, np.ndarray)


# TODO: Better parametrizing
@pytest.mark.parametrize(
    "image_data, want_marked, want_isolated, want_cluster",
    [
        (
            EXAMPLE_IMAGE,
            # marked
            16,
            # isolated
            [(0, 3)],
            # clusters
            [
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
            ],
        )
    ],
)
def test_find_marked_pixels(image_data, want_marked, want_isolated, want_cluster):
    got_marked, got_isolated, got_cluster = flir.find_marked_pixels(image_data)
    assert got_marked == want_marked
    assert got_isolated == want_isolated
    assert got_cluster == want_cluster


@pytest.mark.parametrize(
    "image_data, want", [(EXAMPLE_IMAGE, [110, 189, 223, 231, 231, 219, 189, 126])]
)
def test_encode_pixel_map(image_data, want):
    got = flir.encode_pixel_map(image_data)
    assert got == want


def test_main():
    pass
