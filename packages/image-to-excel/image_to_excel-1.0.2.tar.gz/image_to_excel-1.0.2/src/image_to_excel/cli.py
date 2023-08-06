"""CLI functionality of `image_to_excel`."""

import logging
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from pathlib import Path

from . import BaseClass


def cli_main() -> None:
    """CLI entrypoint for `image_to_excel`. Uses `BaseClass`."""
    argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    argparser.add_argument("-v", "--verbose", help="Enable verbose logging", action="store_true")
    argparser.add_argument("image_path", help="The path to the image file to convert")
    argparser.add_argument("output_file_path", help="The output excel file path")
    argparser.add_argument("-w", "--width", help="The new width in pixels for the image", type=int, default=100)

    args = argparser.parse_args()
    verbose_logging: bool = args.verbose
    image_path = Path(args.image_path)
    output_file_path = Path(args.output_file_path)
    image_width = args.width

    if verbose_logging:
        level = logging.DEBUG
    else:
        level = logging.INFO

    app = BaseClass(log_level=level)

    # simple validation bits
    if image_path == output_file_path:
        raise ValueError("The input and output file paths must be different.")

    app.validate_input_file(image_path)
    app.validate_output_file(output_file_path)

    app.image_to_excel(image_path, image_width, output_file_path)
