"""Test blendmodes."""

import os
import sys
from pathlib import Path

from imgcompare import imgcompare
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from blendmodes.blend import BlendType, blendLayers

# pylint:disable=invalid-name


def test_normal():
	"""Test normal."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.NORMAL),
		THISDIR + "/normal_expected.png",
		tolerance=1,
	)


def test_multiply():
	"""Test multiply."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.MULTIPLY),
		THISDIR + "/multiply_expected.png",
		tolerance=1,
	)


def test_additive():
	"""Test additive."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.ADDITIVE),
		THISDIR + "/additive_expected.png",
		tolerance=1,
	)


def test_colourburn():
	"""Test colourburn."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOURBURN),
		THISDIR + "/colourburn_expected.png",
		tolerance=1,
	)


def test_colourdodge():
	"""Test colourdodge."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOURDODGE),
		THISDIR + "/colourdodge_expected.png",
		tolerance=1,
	)


def test_reflect():
	"""Test reflect."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.REFLECT),
		THISDIR + "/reflect_expected.png",
		tolerance=1,
	)


def test_glow():
	"""Test glow."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GLOW),
		THISDIR + "/glow_expected.png",
		tolerance=1,
	)


def test_overlay():
	"""Test overlay."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.OVERLAY),
		THISDIR + "/overlay_expected.png",
		tolerance=1,
	)


def test_difference():
	"""Test difference."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DIFFERENCE),
		THISDIR + "/difference_expected.png",
		tolerance=1,
	)


def test_negation():
	"""Test negation."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.NEGATION),
		THISDIR + "/negation_expected.png",
		tolerance=1,
	)


def test_lighten():
	"""Test lighten."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.LIGHTEN),
		THISDIR + "/lighten_expected.png",
		tolerance=1,
	)


def test_darken():
	"""Test darken."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DARKEN),
		THISDIR + "/darken_expected.png",
		tolerance=1,
	)


def test_screen():
	"""Test screen."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SCREEN),
		THISDIR + "/screen_expected.png",
		tolerance=1,
	)


def test_xor():
	"""Test xor."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.XOR),
		THISDIR + "/xor_expected.png",
		tolerance=1,
	)


def test_softlight():
	"""Test softlight."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SOFTLIGHT),
		THISDIR + "/softlight_expected.png",
		tolerance=1,
	)


def test_hardlight():
	"""Test hardlight."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.HARDLIGHT),
		THISDIR + "/hardlight_expected.png",
		tolerance=1,
	)


def test_grainextract():
	"""Test grainextract."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GRAINEXTRACT),
		THISDIR + "/grainextract_expected.png",
		tolerance=1,
	)


def test_grainmerge():
	"""Test grainmerge."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.GRAINMERGE),
		THISDIR + "/grainmerge_expected.png",
		tolerance=1,
	)


def test_divide():
	"""Test divide."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DIVIDE),
		THISDIR + "/divide_expected.png",
		tolerance=1,
	)


def test_hue():
	"""Test hue."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.HUE),
		THISDIR + "/hue_expected.png",
		tolerance=1,
	)


def test_saturation():
	"""Test saturation."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SATURATION),
		THISDIR + "/saturation_expected.png",
		tolerance=1,
	)


def test_colour():
	"""Test colour."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.COLOUR),
		THISDIR + "/colour_expected.png",
		tolerance=1,
	)


def test_luminosity():
	"""Test luminosity."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.LUMINOSITY),
		THISDIR + "/luminosity_expected.png",
		tolerance=1,
	)


def test_pinlight():
	"""Test pinlight."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.PINLIGHT),
		THISDIR + "/pinlight_expected.png",
		tolerance=1,
	)


def test_vividlight():
	"""Test vividlight."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.VIVIDLIGHT),
		THISDIR + "/vividlight_expected.png",
		tolerance=1,
	)


def test_exclusion():
	"""Test exclusion."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.EXCLUSION),
		THISDIR + "/exclusion_expected.png",
		tolerance=1,
	)


def test_destin():
	"""Test destin."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTIN),
		THISDIR + "/destin_expected.png",
		tolerance=1,
	)


def test_destout():
	"""Test destout."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTOUT),
		THISDIR + "/destout_expected.png",
		tolerance=1,
	)


def test_destatop():
	"""Test destatop."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.DESTATOP),
		THISDIR + "/destatop_expected.png",
		tolerance=1,
	)


def test_srcatop():
	"""Test srcatop."""
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert imgcompare.is_equal(
		blendLayers(background, foreground, BlendType.SRCATOP),
		THISDIR + "/srcatop_expected.png",
		tolerance=1,
	)


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
