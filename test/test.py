"""Test blendmodes."""

from __future__ import annotations

import sys
from pathlib import Path

from imgcompare import imgcompare
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from blendmodes.blend import BlendType, blendLayers

# pylint:disable=invalid-name


def test_normal():
	"""Test normal."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.NORMAL),
		Image.open(f"{THISDIR}/data/normal_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_multiply():
	"""Test multiply."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.MULTIPLY),
		Image.open(f"{THISDIR}/data/multiply_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_additive():
	"""Test additive."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.ADDITIVE),
		Image.open(f"{THISDIR}/data/additive_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_colourburn():
	"""Test colourburn."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOURBURN),
		Image.open(f"{THISDIR}/data/colourburn_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_colourdodge():
	"""Test colourdodge."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOURDODGE),
		Image.open(f"{THISDIR}/data/colourdodge_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_reflect():
	"""Test reflect."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.REFLECT),
		Image.open(f"{THISDIR}/data/reflect_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_glow():
	"""Test glow."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GLOW),
		Image.open(f"{THISDIR}/data/glow_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_overlay():
	"""Test overlay."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.OVERLAY),
		Image.open(f"{THISDIR}/data/overlay_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_difference():
	"""Test difference."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DIFFERENCE),
		Image.open(f"{THISDIR}/data/difference_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_negation():
	"""Test negation."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.NEGATION),
		Image.open(f"{THISDIR}/data/negation_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_lighten():
	"""Test lighten."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.LIGHTEN),
		Image.open(f"{THISDIR}/data/lighten_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_darken():
	"""Test darken."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DARKEN),
		Image.open(f"{THISDIR}/data/darken_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_screen():
	"""Test screen."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SCREEN),
		Image.open(f"{THISDIR}/data/screen_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_xor():
	"""Test xor."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.XOR),
		Image.open(f"{THISDIR}/data/xor_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_softlight():
	"""Test softlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SOFTLIGHT),
		Image.open(f"{THISDIR}/data/softlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_hardlight():
	"""Test hardlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.HARDLIGHT),
		Image.open(f"{THISDIR}/data/hardlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_grainextract():
	"""Test grainextract."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GRAINEXTRACT),
		Image.open(f"{THISDIR}/data/grainextract_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_grainmerge():
	"""Test grainmerge."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GRAINMERGE),
		Image.open(f"{THISDIR}/data/grainmerge_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_divide():
	"""Test divide."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DIVIDE),
		Image.open(f"{THISDIR}/data/divide_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_hue():
	"""Test hue."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.HUE),
		Image.open(f"{THISDIR}/data/hue_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_saturation():
	"""Test saturation."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SATURATION),
		Image.open(f"{THISDIR}/data/saturation_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_colour():
	"""Test colour."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOUR),
		Image.open(f"{THISDIR}/data/colour_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_luminosity():
	"""Test luminosity."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.LUMINOSITY),
		Image.open(f"{THISDIR}/data/luminosity_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_pinlight():
	"""Test pinlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.PINLIGHT),
		Image.open(f"{THISDIR}/data/pinlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_vividlight():
	"""Test vividlight."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.VIVIDLIGHT),
		Image.open(f"{THISDIR}/data/vividlight_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_exclusion():
	"""Test exclusion."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.EXCLUSION),
		Image.open(f"{THISDIR}/data/exclusion_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_destin():
	"""Test destin."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTIN),
		Image.open(f"{THISDIR}/data/destin_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_destout():
	"""Test destout."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTOUT),
		Image.open(f"{THISDIR}/data/destout_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_destatop():
	"""Test destatop."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTATOP),
		Image.open(f"{THISDIR}/data/destatop_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_srcatop():
	"""Test srcatop."""
	background = Image.open(f"{THISDIR}/data/background.png")
	foreground = Image.open(f"{THISDIR}/data/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SRCATOP),
		Image.open(f"{THISDIR}/data/srcatop_expected.png").convert("RGBA"),
		tolerance=0.2,
	)


def test_non_rgba():
	background = Image.open(f"{THISDIR}/data/background.jpg")
	foreground = Image.open(f"{THISDIR}/data/foreground.jpg")
	blendLayers(background, foreground, BlendType.NORMAL)


test_normal()
test_multiply()
test_additive()
test_colourburn()
test_colourdodge()
test_reflect()
test_glow()
test_overlay()
test_difference()
test_negation()
test_lighten()
test_darken()
test_screen()
test_xor()
test_softlight()
test_hardlight()
test_grainextract()
test_grainmerge()
test_divide()
test_hue()
test_saturation()
test_colour()
test_luminosity()
test_pinlight()
test_vividlight()
test_exclusion()
test_destin()
test_destout()
test_destatop()
test_srcatop()
test_non_rgba()
