from __future__ import annotations

import random
from pathlib import Path

import pytest
from PIL import Image

from blendmodes.blend import BlendType, blendLayers

THISDIR = Path(__file__).resolve().parent


@pytest.mark.parametrize("blend_mode", random.choices(list(BlendType), k=200))
def test_blend_modes(blend_mode: BlendType) -> None:
	"""Test blend modes with random selection."""
	background = Image.open(THISDIR / "data" / "background.png")
	foreground = Image.open(THISDIR / "data" / "foreground.png")

	result = blendLayers(background, foreground, blend_mode)

	assert result is not None  # Ensure we get a valid image back
