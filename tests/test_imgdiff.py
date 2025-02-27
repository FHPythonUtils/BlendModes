"""Test blendmodes.imgdiff"""

from __future__ import annotations

from pathlib import Path

import pytest
from imgcompare import imgcompare
from PIL import Image

THISDIR = Path(__file__).resolve().parent


from blendmodes.imgdiff import image_diff, is_equal, is_x_diff


# Example parameterized test for image_diff
@pytest.mark.parametrize(
	("image1", "image2", "expected_diff"),
	[
		(Image.new("RGBA", (2, 2), (255,) * 4), Image.new("RGBA", (2, 2), (255,) * 4), 0),
		(Image.new("RGBA", (2, 2), (0,) * 4), Image.new("RGBA", (2, 2), (255,) * 4), 100),
		# Identical images, no difference
		(
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			0,
		),
		# Completely different images
		(
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			Image.new("RGBA", (2, 2), (0, 255, 0, 255)),
			50,
		),
	],
)
def test_image_diff(image1: Image.Image, image2: Image.Image, expected_diff: float) -> None:
	diff = image_diff(image1, image2)
	assert diff == expected_diff, f"Expected {expected_diff}, but got {diff}"


# Example parameterized test for is_equal
@pytest.mark.parametrize(
	("image1", "image2", "tolerance", "expected_result"),
	[
		# Identical images, no tolerance
		(
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			0,
			True,
		),
		# Identical images, with tolerance
		(
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			5,
			True,
		),
		# Completely different images, no tolerance
		(
			Image.new("RGBA", (2, 2), (255, 0, 0, 255)),
			Image.new("RGBA", (2, 2), (0, 0, 0, 0)),
			0,
			False,
		),
		# Small difference, within tolerance
		(
			Image.new("RGBA", (2, 2), (100, 150, 200, 255)),
			Image.new("RGBA", (2, 2), (100, 150, 200, 250)),
			5,
			True,
		),
	],
)
def test_is_equal(
	image1: Image.Image,
	image2: Image.Image,
	tolerance: float,
	expected_result: bool,  # noqa: FBT001
) -> None:
	result = is_equal(image1, image2, tolerance=tolerance)
	assert result == expected_result, f"Expected {expected_result}, but got {result}"


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
	assert is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=66, tolerance=1)

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
	with pytest.raises(ValueError, match="Images must have the same dimensions for comparison"):
		image_diff(img1, img2)


def test_identical_rgba_vs_rgb() -> None:
	img1 = Image.new("RGBA", (100, 100), (255, 0, 0, 255))
	img2 = Image.new("RGB", (100, 100), "red")
	assert image_diff(img1, img2) == 0
	assert is_equal(img1, img2)
	assert is_x_diff(img1, img2, cmp_diff=0, tolerance=0)
