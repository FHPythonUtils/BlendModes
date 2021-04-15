"""Do stuff to images to prepare them.
"""
from typing import Tuple

from PIL import Image


def rasterImageOA(
	image: Image.Image, size: Tuple[int, int], alpha: float = 1.0, offsets: Tuple[int, int] = (0, 0)
) -> Image.Image:
	"""Rasterise an image with offset and alpha to a given size.

	Args:
		image (Image.Image): pil image to draw
		size (Tuple[int, int]): width, height as a tuple
		alpha (float, optional): alpha transparency. Defaults to 1.0.
		offsets (Tuple[int, int], optional): x, y offsets as a tuple.
		Defaults to (0, 0).

	Returns:
		Image.Image: new image
	"""
	imageOffset = rasterImageOffset(image, size, offsets)
	return Image.blend(Image.new("RGBA", size), imageOffset, alpha)


def rasterImageOffset(image: Image.Image, size: Tuple[int, int], offsets: Tuple[int, int] = (0, 0)):
	"""Rasterise an image with offset to a given size.

	Args:
		image (Image.Image): pil image to draw
		size (Tuple[int, int]): width, height as a tuple
		offsets (Tuple[int, int], optional): x, y offsets as a tuple.
		Defaults to (0, 0).

	Returns:
		Image.Image: new image
	"""
	imageOffset = Image.new("RGBA", size)
	imageOffset.paste(image.convert("RGBA"), offsets, image.convert("RGBA"))
	return imageOffset
