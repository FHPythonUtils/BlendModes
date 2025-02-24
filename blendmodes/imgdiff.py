from __future__ import annotations

import numpy as np
from PIL import Image


def is_x_diff(
	img1in: Image.Image,
	img2in: Image.Image,
	compare_mode: str = "RGBA",
	cmp_diff: float = 0,
	tolerance: float = 0,
	*,
	percentage: bool = True,
) -> bool:
	"""
	Compare two images and return True/False if the image is within `tolerance` of
	`cmp_diff`.

	For example, a black and white image compared in 'RGB' mode would
	return a value of 100, which would then be checked if its between
	`cmp_diff - tolerance` and `cmp_diff + tolerance`

	:param Image.Image img1in: image 1 to compare
	:param Image.Image img2in: image 2 to compare
	:param str compare_mode: how should the pillow images be compared? eg RGBA, RGB, L etc
	:param float cmp_diff: how 'unequal' should the images be? 0 for identical, 1 (or 100)
	for completely different (eg black + white in L mode)
	param float tolerance: what tolerance should we accept on the inequality?
	param bool percentage: are we comparing in percentage mode vs 0-1 mode?

	:return bool: True/False if the images are within `tolerance` of
	`cmp_diff`.

	Example Use
	-----------

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=33, tolerance=1)
	True

	>>> img1 = Image.new("RGB", (100, 100), "white")
	>>> img2 = Image.new("RGB", (100, 100), "black")
	>>> is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=100, tolerance=1)
	True

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> is_x_diff(img1, img2, compare_mode="L", cmp_diff=18, tolerance=1)
	True

	"""
	compare_res = image_diff(img1in, img2in, compare_mode, percentage=percentage)
	return cmp_diff - tolerance <= compare_res <= cmp_diff + tolerance


def is_equal(
	img1in: Image.Image,
	img2in: Image.Image,
	compare_mode: str = "RGBA",
	tolerance: float = 0,
	*,
	percentage: bool = True,
) -> bool:
	"""
	Compare two images and return True/False if the image is within `tolerance` of
	`cmp_diff`.

	For example, a black and white image compared in 'RGB' mode would
	return a value of 100, which would then be checked if its between
	`cmp_diff - tolerance` and `cmp_diff + tolerance`

	:param Image.Image img1in: image 1 to compare
	:param Image.Image img2in: image 2 to compare
	:param str compare_mode: how should the pillow images be compared? eg RGBA, RGB, L etc
	param float tolerance: what tolerance should we accept on any inequality?
	param bool percentage: are we comparing in percentage mode vs 0-1 mode?

	:return bool: if the images are equal with a given tolerance

	Example Use
	-----------

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> is_equal(img1, img2, compare_mode="RGB", tolerance=1)
	False

	>>> img1 = Image.new("RGB", (100, 100), "white")
	>>> img2 = Image.new("RGB", (100, 100), "black")
	>>> is_equal(img1, img2, compare_mode="RGB", tolerance=1)
	False

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> is_equal(img1, img2, compare_mode="L", tolerance=1)
	False

	"""
	compare_res = image_diff(img1in, img2in, compare_mode, percentage=percentage)
	return compare_res <= tolerance


def image_diff(
	img1in: Image.Image, img2in: Image.Image, compare_mode: str = "RGBA", *, percentage: bool = True
) -> float:
	"""
	Compare two images and return the difference as a value between 0 and 1, or
	if percentage: 0 and 100.

	For example, a black and white image compared in 'RGB' mode would
	return a value of 100, which would then be checked if its between
	`cmp_diff - tolerance` and `cmp_diff + tolerance`

	:param Image.Image img1in: image 1 to compare
	:param Image.Image img2in: image 2 to compare
	:param str compare_mode: how should the pillow images be compared? eg RGBA, RGB, L etc
	param bool percentage: are we comparing in percentage mode vs 0-1 mode?

	:return float: value representing how different the images are

	Example Use
	-----------

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> res = image_diff(img1, img2, compare_mode="RGB")
	>>> int(res)
	33

	>>> img1 = Image.new("RGB", (100, 100), "white")
	>>> img2 = Image.new("RGB", (100, 100), "black")
	>>> image_diff(img1, img2, compare_mode="RGB")
	100.0

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> res = image_diff(img1, img2, compare_mode="L")
	>>> int(res)
	18

	"""
	img1 = img1in.convert(mode=compare_mode)
	img2 = img2in.convert(mode=compare_mode)
	return image_diff_array(img1, img2) * (100 if percentage else 1)


def image_diff_array(img1in: Image.Image | np.ndarray, img2in: Image.Image | np.ndarray) -> float:
	"""
	Compare two images and return difference between 0, and 1.
	Supports both PIL Images and NumPy arrays.

	Both images must be in the same mode/ shape

	:param Image.Image | np.ndarray img1in: image 1 to compare
	:param Image.Image | np.ndarray img2in: image 2 to compare
	:return float: value representing how different the images are. between 0, and 1


	Example Use
	-----------

	>>> img1 = Image.new("RGB", (100, 100), "red")
	>>> img2 = Image.new("RGB", (100, 100), "blue")
	>>> res = image_diff(img1, img2)
	>>> int(res)
	25

	>>> img1 = Image.new("RGB", (100, 100), "white")
	>>> img2 = Image.new("RGB", (100, 100), "black")
	>>> image_diff(img1, img2)
	75.0

	"""
	# Convert PIL images to NumPy arrays if needed
	img1 = np.array(img1in) if isinstance(img1in, Image.Image) else img1in
	img2 = np.array(img2in) if isinstance(img2in, Image.Image) else img2in
	# Ensure images have the same dimensions
	if img1.shape != img2.shape:
		msg = "Images must have the same dimensions for comparison."
		raise ValueError(msg)

	# Compute absolute difference
	difference = np.abs(img1 - img2)

	# Sum the differences and normalize to get a percentage
	total_diff = np.sum(difference)
	return float(total_diff / img1.size / 255)


if __name__ == "__main__":
	import doctest

	doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
	doctest.testmod()
