"""Test blendmodes."""

from __future__ import annotations

import sys
from pathlib import Path

from imgcompare import imgcompare
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from blendmodes.blend import BlendType, blendLayers


def test_normal() -> None:
	"""Test normal."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.NORMAL),
		Image.open(f"{THISDIR}/data/normal_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_multiply() -> None:
	"""Test multiply."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.MULTIPLY),
		Image.open(f"{THISDIR}/data/multiply_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_additive() -> None:
	"""Test additive."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.ADDITIVE),
		Image.open(f"{THISDIR}/data/additive_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_colourburn() -> None:
	"""Test colourburn."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOURBURN),
		Image.open(f"{THISDIR}/data/colourburn_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_colourdodge() -> None:
	"""Test colourdodge."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOURDODGE),
		Image.open(f"{THISDIR}/data/colourdodge_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_reflect() -> None:
	"""Test reflect."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.REFLECT),
		Image.open(f"{THISDIR}/data/reflect_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_glow() -> None:
	"""Test glow."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GLOW),
		Image.open(f"{THISDIR}/data/glow_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_overlay() -> None:
	"""Test overlay."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.OVERLAY),
		Image.open(f"{THISDIR}/data/overlay_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_difference() -> None:
	"""Test difference."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DIFFERENCE),
		Image.open(f"{THISDIR}/data/difference_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_negation() -> None:
	"""Test negation."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.NEGATION),
		Image.open(f"{THISDIR}/data/negation_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_lighten() -> None:
	"""Test lighten."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.LIGHTEN),
		Image.open(f"{THISDIR}/data/lighten_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_darken() -> None:
	"""Test darken."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DARKEN),
		Image.open(f"{THISDIR}/data/darken_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_screen() -> None:
	"""Test screen."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SCREEN),
		Image.open(f"{THISDIR}/data/screen_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_xor() -> None:
	"""Test xor."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.XOR),
		Image.open(f"{THISDIR}/data/xor_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_softlight() -> None:
	"""Test softlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SOFTLIGHT),
		Image.open(f"{THISDIR}/data/softlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_hardlight() -> None:
	"""Test hardlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.HARDLIGHT),
		Image.open(f"{THISDIR}/data/hardlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_grainextract() -> None:
	"""Test grainextract."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GRAINEXTRACT),
		Image.open(f"{THISDIR}/data/grainextract_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_grainmerge() -> None:
	"""Test grainmerge."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GRAINMERGE),
		Image.open(f"{THISDIR}/data/grainmerge_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_divide() -> None:
	"""Test divide."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DIVIDE),
		Image.open(f"{THISDIR}/data/divide_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_hue() -> None:
	"""Test hue."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.HUE),
		Image.open(f"{THISDIR}/data/hue_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_saturation() -> None:
	"""Test saturation."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SATURATION),
		Image.open(f"{THISDIR}/data/saturation_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_colour() -> None:
	"""Test colour."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOUR),
		Image.open(f"{THISDIR}/data/colour_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_luminosity() -> None:
	"""Test luminosity."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.LUMINOSITY),
		Image.open(f"{THISDIR}/data/luminosity_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_pinlight() -> None:
	"""Test pinlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.PINLIGHT),
		Image.open(f"{THISDIR}/data/pinlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_vividlight() -> None:
	"""Test vividlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.VIVIDLIGHT),
		Image.open(f"{THISDIR}/data/vividlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_exclusion() -> None:
	"""Test exclusion."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.EXCLUSION),
		Image.open(f"{THISDIR}/data/exclusion_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_destin() -> None:
	"""Test destin."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTIN),
		Image.open(f"{THISDIR}/data/destin_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_destout() -> None:
	"""Test destout."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTOUT),
		Image.open(f"{THISDIR}/data/destout_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_destatop() -> None:
	"""Test destatop."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTATOP),
		Image.open(f"{THISDIR}/data/destatop_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_srcatop() -> None:
	"""Test srcatop."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SRCATOP),
		Image.open(f"{THISDIR}/data/srcatop_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_non_rgba() -> None:
	background = Image.open(f"{THISDIR}/data/background.jpg")
	foreground = Image.open(f"{THISDIR}/data/foreground.jpg")
	blendLayers(background, foreground, BlendType.NORMAL)


if __name__ == "__main__":
	import sys

	import pytest

	pytest.main(sys.argv)
