"""Test blendmodes."""

from __future__ import annotations

from pathlib import Path

import pytest
from imgcompare import imgcompare
from PIL import Image

THISDIR = Path(__file__).resolve().parent


from blendmodes.blend import BlendType, blendLayers

BLEND_TESTS = [
	("normal_expected.png", BlendType.NORMAL),
	("multiply_expected.png", BlendType.MULTIPLY),
	("additive_expected.png", BlendType.ADDITIVE),
	("colourburn_expected.png", BlendType.COLOURBURN),
	("colourdodge_expected.png", BlendType.COLOURDODGE),
	("reflect_expected.png", BlendType.REFLECT),
	("glow_expected.png", BlendType.GLOW),
	("overlay_expected.png", BlendType.OVERLAY),
	("difference_expected.png", BlendType.DIFFERENCE),
	("negation_expected.png", BlendType.NEGATION),
	("lighten_expected.png", BlendType.LIGHTEN),
	("darken_expected.png", BlendType.DARKEN),
	("screen_expected.png", BlendType.SCREEN),
	("xor_expected.png", BlendType.XOR),
	("softlight_expected.png", BlendType.SOFTLIGHT),
	("hardlight_expected.png", BlendType.HARDLIGHT),
	("grainextract_expected.png", BlendType.GRAINEXTRACT),
	("grainmerge_expected.png", BlendType.GRAINMERGE),
	("divide_expected.png", BlendType.DIVIDE),
	("hue_expected.png", BlendType.HUE),
	("saturation_expected.png", BlendType.SATURATION),
	("colour_expected.png", BlendType.COLOUR),
	("luminosity_expected.png", BlendType.LUMINOSITY),
	("pinlight_expected.png", BlendType.PINLIGHT),
	("vividlight_expected.png", BlendType.VIVIDLIGHT),
	("exclusion_expected.png", BlendType.EXCLUSION),
	("destin_expected.png", BlendType.DESTIN),
	("destout_expected.png", BlendType.DESTOUT),
	("destatop_expected.png", BlendType.DESTATOP),
	("srcatop_expected.png", BlendType.SRCATOP),
]


@pytest.mark.parametrize(("expected_image", "blend_mode"), BLEND_TESTS)
def test_blend_modes_case1(expected_image: str, blend_mode: BlendType) -> None:
	background = Image.open(THISDIR / "data/src/rainbow.png")
	foreground = Image.open(THISDIR / "data/src/duck.png")

	result = blendLayers(background, foreground, blend_mode)
	expected_dir = THISDIR / "data/case1" / expected_image
	# result.save(expected_dir)
	expected = Image.open(expected_dir).convert("RGBA")

	assert imgcompare.is_equal(result, expected, tolerance=0.2)


@pytest.mark.parametrize(("expected_image", "blend_mode"), BLEND_TESTS)
def test_blend_modes_case2(expected_image: str, blend_mode: BlendType) -> None:
	background = Image.open(THISDIR / "data/src/noise_texture.png")
	foreground = Image.open(THISDIR / "data/src/red_soft_mask.png")

	result = blendLayers(background, foreground, blend_mode)
	expected_dir = THISDIR / "data/case2" / expected_image
	# result.save(expected_dir)
	expected = Image.open(expected_dir).convert("RGBA")

	assert imgcompare.is_equal(result, expected, tolerance=0.2)


@pytest.mark.parametrize(("expected_image", "blend_mode"), BLEND_TESTS)
def test_blend_modes_case3(expected_image: str, blend_mode: BlendType) -> None:
	background = Image.open(THISDIR / "data/src/red_soft_mask.png")
	foreground = Image.open(THISDIR / "data/src/rectangle_silhouette.png")

	result = blendLayers(background, foreground, blend_mode)
	expected_dir = THISDIR / "data/case3" / expected_image
	# result.save(expected_dir)
	expected = Image.open(expected_dir).convert("RGBA")

	assert imgcompare.is_equal(result, expected, tolerance=0.2)


def test_non_rgba() -> None:
	background = Image.open(THISDIR / "data/src/rainbow.jpg")
	foreground = Image.open(THISDIR / "data/src/duck.jpg")
	blendLayers(background, foreground, BlendType.NORMAL)


if __name__ == "__main__":
	for dest_filename, _ in BLEND_TESTS:
		blend_mode = dest_filename.split("_")[0]
		blend_mode = blend_mode[0].upper() + blend_mode[1:]

		print(f"""
## {blend_mode}

| Case | Background | Foreground | Output |
|------|---------|------|--------|
| Case 1 | ![img](../../tests/data/src/rainbow.png) | ![img](../../tests/data/src/duck.png) | ![img](../../tests/data/case1/{dest_filename}) |
| Case 2 | ![img](../../tests/data/src/noise_texture.png) | ![img](../../tests/data/src/red_soft_mask.png) | ![img](../../tests/data/case2/{dest_filename}) |
| Case 2 | ![img](../../tests/data/src/red_soft_mask.png) | ![img](../../tests/data/src/rectangle_silhouette.png) | ![img](../../tests/data/case3/{dest_filename}) |

		""")  # noqa: T201, E501
