"""The main functionality of `image_to_excel`."""

import logging
from pathlib import Path

from .core.excel import ExcelWriter
from .core.image import ImageManipulator

logger = logging.getLogger(__name__)


class BaseClass:
    """Everything in the project comes back to here."""

    ACCEPTED_IMAGE_EXTENSIONS: list[str] = [".png", ".jpg", ".jpeg"]
    """The file extensions to accept for conversion."""

    def __init__(self, log_level: int = logging.INFO):
        """Initialises the base class for `image_to_excel` by loading the config and setting up a logger.

        Args:
            log_level (str): The level to use for package logs.
        """
        logging.getLogger("image_to_excel").setLevel(log_level)

    def validate_input_file(self, image_path: Path) -> None:
        """Validate the input file.

        Args:
            image_path (Path): The path to validate
        """
        if not image_path.exists():
            raise FileNotFoundError(f"Image file '{image_path}' does not exist.")

        if image_path.is_dir():
            raise ValueError(f"Image file '{image_path}' is a directory.")

        if image_path.suffix not in self.ACCEPTED_IMAGE_EXTENSIONS:
            raise ValueError(
                f"Image file '{image_path}' is not a valid image file.\n"
                f"Accepted extensions are: {', '.join(self.ACCEPTED_IMAGE_EXTENSIONS)}"
            )

    def validate_output_file(self, output_path: Path) -> None:
        """Validate the output file.

        Args:
            output_path (Path): The path to validate.
        """
        if not output_path.parent.exists():
            raise FileNotFoundError(f"Output directory '{output_path.parent}' does not exist.")

        if output_path.is_dir():
            raise ValueError(f"Output file '{output_path}' is a directory.")

        if output_path.suffix != ".xlsx":
            raise ValueError(f"Output file '{output_path}' is not a valid excel file. Please specify a '.xlsx' file.")

    def image_to_excel(self, image_path: Path, image_width: int, output_file_path: Path) -> None:
        """Convert an image to an excel file.

        Args:
            image_path (Path): The path to the image file to convert.
            image_width (int): The new width in pixels for the image.
                The height will be calculated automatically to maintain aspect ration.
            output_file_path (Path): The output excel file path.
        """
        image_manipulator = ImageManipulator()
        excel_writer = ExcelWriter(output_file_path)

        logger.info("Resizing image...")

        image_array = image_manipulator.image_to_data(image_path)
        image_array = image_manipulator.resize_image_to_width(image_array, image_width)

        logger.info("Writing image to excel file...")

        try:
            excel_writer.write_image_array(image_array)
        finally:
            excel_writer.close()

        logger.info("Image converted!")
