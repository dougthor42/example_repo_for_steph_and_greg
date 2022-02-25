# -*- coding: utf-8 -*-
import os

import click

from . import flir


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "-o",
    "--outfile",
    required=True,
    type=click.Path(),
    help="The file to store data to.",
)
def main(filename, outfile):
    image_data = flir.load_image_file(filename)

    num_marked, isolated, clusters = flir.find_marked_pixels(image_data)
    pixel_map = flir.encode_pixel_map(image_data)

    hex_str = " ".join("{:02X}".format(val) for val in pixel_map)

    # TODO: This should be a function in flir.py and should be tested.
    with open(outfile, "w") as openf:

        # TODO: A desired file format was not provided, so just record
        # basic info. JSON is probably a good option for the future.
        openf.write(f"Number of Marked Pixels: {num_marked}" + os.linesep)
        openf.write(f"Isoloated pixels: {isolated}" + os.linesep)
        openf.write(f"Number of clusters: {len(clusters)}" + os.linesep)
        openf.write(f"Custers: {clusters}" + os.linesep)
        openf.write(f"Hex image data: {hex_str}" + os.linesep)

        print("Complete")
