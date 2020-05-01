""" test blendmodes """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imgcompare import imgcompare
from PIL import Image
from blendmodes.blend import blendLayers, BlendType

def test_normal():
	""" test normal """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.NORMAL),
	THISDIR + "/normal_expected.png", tolerance=1))

def test_multiply():
	""" test multiply """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.MULTIPLY),
	THISDIR + "/multiply_expected.png", tolerance=1))

def test_additive():
	""" test additive """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.ADDITIVE),
	THISDIR + "/additive_expected.png", tolerance=1))

def test_colourburn():
	""" test colourburn """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.COLOURBURN),
	THISDIR + "/colourburn_expected.png", tolerance=1))

def test_colourdodge():
	""" test colourdodge """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.COLOURDODGE),
	THISDIR + "/colourdodge_expected.png", tolerance=1))

def test_reflect():
	""" test reflect """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.REFLECT),
	THISDIR + "/reflect_expected.png", tolerance=1))

def test_glow():
	""" test glow """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.GLOW),
	THISDIR + "/glow_expected.png", tolerance=1))

def test_overlay():
	""" test overlay """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.OVERLAY),
	THISDIR + "/overlay_expected.png", tolerance=1))

def test_difference():
	""" test difference """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.DIFFERENCE),
	THISDIR + "/difference_expected.png", tolerance=1))

def test_negation():
	""" test negation """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.NEGATION),
	THISDIR + "/negation_expected.png", tolerance=1))

def test_lighten():
	""" test lighten """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.LIGHTEN),
	THISDIR + "/lighten_expected.png", tolerance=1))

def test_darken():
	""" test darken """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.DARKEN),
	THISDIR + "/darken_expected.png", tolerance=1))

def test_screen():
	""" test screen """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.SCREEN),
	THISDIR + "/screen_expected.png", tolerance=1))

def test_xor():
	""" test xor """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.XOR),
	THISDIR + "/xor_expected.png", tolerance=1))

def test_softlight():
	""" test softlight """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.SOFTLIGHT),
	THISDIR + "/softlight_expected.png", tolerance=1))

def test_hardlight():
	""" test hardlight """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.HARDLIGHT),
	THISDIR + "/hardlight_expected.png", tolerance=1))

def test_grainextract():
	""" test grainextract """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.GRAINEXTRACT),
	THISDIR + "/grainextract_expected.png", tolerance=1))

def test_grainmerge():
	""" test grainmerge """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.GRAINMERGE),
	THISDIR + "/grainmerge_expected.png", tolerance=1))

def test_divide():
	""" test divide """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.DIVIDE),
	THISDIR + "/divide_expected.png", tolerance=1))

def test_hue():
	""" test hue """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.HUE),
	THISDIR + "/hue_expected.png", tolerance=1))

def test_saturation():
	""" test saturation """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.SATURATION),
	THISDIR + "/saturation_expected.png", tolerance=1))

def test_colour():
	""" test colour """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.COLOUR),
	THISDIR + "/colour_expected.png", tolerance=1))

def test_luminosity():
	""" test luminosity """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.LUMINOSITY),
	THISDIR + "/luminosity_expected.png", tolerance=1))

def test_pinlight():
	""" test pinlight """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.PINLIGHT),
	THISDIR + "/pinlight_expected.png", tolerance=1))

def test_vividlight():
	""" test vividlight """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.VIVIDLIGHT),
	THISDIR + "/vividlight_expected.png", tolerance=1))

def test_exclusion():
	""" test exclusion """
	background = Image.open(THISDIR + "/background.png")
	foreground = Image.open(THISDIR + "/foreground.png")
	assert(imgcompare.is_equal(blendLayers(background, foreground, BlendType.EXCLUSION),
	THISDIR + "/exclusion_expected.png", tolerance=1))

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
