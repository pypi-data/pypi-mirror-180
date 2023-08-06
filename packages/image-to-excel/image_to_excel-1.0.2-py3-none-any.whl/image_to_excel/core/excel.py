"""Module to write out data to a new excel file."""
import logging
from pathlib import Path

import numpy as np
import xlsxwriter
import xlsxwriter.format

logger = logging.getLogger(__name__)


class ExcelWriter:
    """Writes data to an excel file."""

    def __init__(self, output_path: Path) -> None:
        """Initialise the ExcelWriter.

        Args:
            output_path (Path): The path to write the excel file to.
        """
        logger.debug("Initialising ExcelWriter with output path %s", output_path)
        self.workbook = xlsxwriter.Workbook(output_path)
        self.worksheet = self.workbook.add_worksheet()

    def _get_pixel_format(self, pixel: np.ndarray) -> xlsxwriter.format.Format:
        """Get the format for a pixel.

        Args:
            pixel (np.ndarray): The pixel to get the format for.

        Returns:
            xlsxwriter.format.Format: The format for the pixel.
        """
        return self.workbook.add_format({"bg_color": f"#{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}"})

    def write_image_array(self, image: np.ndarray) -> None:
        """Write an image array to the excel file, using one cell to represent one pixel.

        Uses color formatting to set the color of each cell.

        Args:
            image (np.ndarray): The image to write to the worksheet.
        """
        total_rows: int = image.shape[0]

        for row_index, row in enumerate(image):
            for column_index, pixel in enumerate(row):
                self.worksheet.write(row_index, column_index, "", self._get_pixel_format(pixel))
            logger.debug("Wrote row %s of %s", row_index + 1, total_rows)

    def close(self) -> None:
        """Close the excel file."""
        logger.debug("Closing excel file")
        self.workbook.close()
