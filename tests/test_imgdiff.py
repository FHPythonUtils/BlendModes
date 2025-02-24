"""Test blendmodes.imgdiff"""

from __future__ import annotations

from pathlib import Path

import pytest
from imgcompare import imgcompare
from PIL import Image

THISDIR = Path(__file__).resolve().parent


from blendmodes.imgdiff import image_diff, is_equal, is_x_diff


def test_identical_images() -> None:
	img = Image.new("RGB", (100, 100), "red")
	assert image_diff(img, img) == 0.0
	assert is_equal(img, img)
	assert is_x_diff(img, img, cmp_diff=0, tolerance=0)

	# Test against imagecompare
	assert imgcompare.image_diff_percent(img, img) == image_diff(img, img)


def test_completely_different_images() -> None:
	img1 = Image.new("RGB", (100, 100), "white")
	img2 = Image.new("RGB", (100, 100), "black")
	assert image_diff(img1, img2, compare_mode="RGB") == 100
	assert not is_equal(img1, img2)
	assert is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=100, tolerance=0)

	# Test against imagecompare
	assert imgcompare.image_diff_percent(img1, img2) == image_diff(img1, img2, "RGB")


def test_red_blue_rgb() -> None:
	img1 = Image.new("RGB", (100, 100), "red")
	img2 = Image.new("RGB", (100, 100), "blue")
	assert is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=33, tolerance=1)

	# Test against imagecompare
	# assert imgcompare.image_diff_percent(img1, img2) == image_diff(img1, img2, compare_mode="RGB")


def test_red_blue_l() -> None:
	img1 = Image.new("RGB", (100, 100), "red")
	img2 = Image.new("RGB", (100, 100), "blue")
	assert is_x_diff(img1, img2, compare_mode="L", cmp_diff=18, tolerance=1)

	# Test against imagecompare
	# assert imgcompare.image_diff_percent(img1, img2) == image_diff(img1, img2, compare_mode="L")


def test_different_size_images() -> None:
	img1 = Image.new("RGB", (100, 100), "red")
	img2 = Image.new("RGB", (50, 50), "blue")
	with pytest.raises(ValueError):
		image_diff(img1, img2)


def test_identical_rgba_vs_rgb() -> None:
	img1 = Image.new("RGBA", (100, 100), (255, 0, 0, 255))
	img2 = Image.new("RGB", (100, 100), "red")
	assert image_diff(img1, img2) == 0
	assert is_equal(img1, img2)
	assert is_x_diff(img1, img2, cmp_diff=0, tolerance=0)
