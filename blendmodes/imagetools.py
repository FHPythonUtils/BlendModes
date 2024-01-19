"""Do stuff to images to prepare them.
"""
from __future__ import annotations

from PIL import Image


def renderWAlphaOffset(
	image: Image.Image, size: tuple[int, int], alpha: float = 1.0, offsets: tuple[int, int] = (0, 0)
) -> Image.Image:
	"""Render an image with offset and alpha to a given size.

	Args:
	----
		image (Image.Image): pil image to draw
		size (tuple[int, int]): width, height as a tuple
		alpha (float, optional): alpha transparency. Defaults to 1.0.
		offsets (tuple[int, int], optional): x, y offsets as a tuple.
		Defaults to (0, 0).

	Returns:
	-------
		Image.Image: new image
	"""
	imageOffset = Image.new("RGBA", size)
	imageOffset.paste(image.convert("RGBA"), offsets, image.convert("RGBA"))
	return Image.blend(Image.new("RGBA", size), imageOffset, alpha)
