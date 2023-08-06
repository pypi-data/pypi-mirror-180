"""Image manipulation module."""
import logging
from pathlib import Path

import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)


class ImageManipulator:
    """Image Manipulator. Can load + resize images."""

    def image_to_data(self, image_path: Path) -> np.ndarray:
        """Load an image file from disk and return it as a numpy array.

        Args:
            image_path (Path): The location of the image file on disk.
        """
        logger.debug("Loading image from %s", image_path)
        with open(image_path, "rb") as image_file:
            image = Image.open(image_file)
            return np.asarray(image)

    def resize_image(self, image: np.ndarray, new_size: tuple[int, int]) -> np.ndarray:
        """Resize an image to a new size.

        Args:
            image (np.ndarray): The image to resize.
            new_size (tuple[int, int]): The new size for the image.
        """
        logger.debug("Resizing image to %s", new_size)
        return np.asarray(Image.fromarray(image).resize(new_size, Image.ANTIALIAS))

    def resize_image_to_width(self, image: np.ndarray, new_width: int) -> np.ndarray:
        """Resize an image to a new width.

        Args:
            image (np.ndarray): The image to resize.
            new_width (int): The new width for the image.
        """
        logger.debug("Resizing image to width %s", new_width)
        current_width, current_height = image.shape[1], image.shape[0]

        if new_width >= current_width:
            logger.warning(
                "New width is greater than or the same as the current width. " "Using original image without resizing."
            )
            return image

        new_height = int(current_height * (new_width / current_width))
        return self.resize_image(image, (new_width, new_height))
