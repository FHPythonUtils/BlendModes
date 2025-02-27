"""Provide blending functions and types.

Adapted from https://github.com/addisonElliott/pypdn/blob/master/pypdn/reader.py
and https://gitlab.com/inklabapp/pyora/-/blob/master/pyora/BlendNonSep.py
MIT License Copyright (c) 2020 FredHappyface

Credits to:

MIT License Copyright (c) 2019 Paul Jewell
For implementing blending from the Open Raster Image Spec

MIT License Copyright (c) 2018 Addison Elliott
For implementing blending from Paint.NET

MIT License Copyright (c) 2017 pashango
For implementing a number of blending functions used by other popular image
editors
"""

from __future__ import annotations

import warnings

import numpy as np
from PIL import Image

from blendmodes.blendtype import BlendType

HALF_THRESHOLD = 0.5


def normal(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.NORMAL."""
	del background  # we don't care about this
	return foreground


def multiply(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.MULTIPLY."""
	return np.clip(foreground * background, 0.0, 1.0)


def additive(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.ADDITIVE."""
	return np.minimum(background + foreground, 1.0)


def colourburn(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.COLOURBURN."""
	with np.errstate(divide="ignore"):
		return np.where(
			foreground != 0.0, np.maximum(1.0 - ((1.0 - background) / foreground), 0.0), 0.0
		)


def colourdodge(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.COLOURDODGE."""
	with np.errstate(divide="ignore"):
		return np.where(foreground != 1.0, np.minimum(background / (1.0 - foreground), 1.0), 1.0)


def reflect(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.REFLECT."""
	with np.errstate(divide="ignore"):
		return np.where(
			foreground != 1.0, np.minimum((background**2) / (1.0 - foreground), 1.0), 1.0
		)


def glow(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.GLOW."""
	with np.errstate(divide="ignore"):
		return np.where(
			background != 1.0, np.minimum((foreground**2) / (1.0 - background), 1.0), 1.0
		)


def overlay(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.OVERLAY."""
	return np.where(
		background < HALF_THRESHOLD,
		2 * background * foreground,
		1.0 - (2 * (1.0 - background) * (1.0 - foreground)),
	)


def difference(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.DIFFERENCE."""
	return np.abs(background - foreground)


def negation(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.NEGATION."""
	return np.maximum(background - foreground, 0.0)


def lighten(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.LIGHTEN."""
	return np.maximum(background, foreground)


def darken(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.DARKEN."""
	return np.minimum(background, foreground)


def screen(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.SCREEN."""
	return background + foreground - background * foreground


def xor(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.XOR."""
	# XOR requires int values so convert to uint8
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		return imageIntToFloat(imageFloatToInt(background) ^ imageFloatToInt(foreground))


def softlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.SOFTLIGHT."""
	return (1.0 - background) * background * foreground + background * (
		1.0 - (1.0 - background) * (1.0 - foreground)
	)


def hardlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.HARDLIGHT."""
	return np.where(
		foreground < HALF_THRESHOLD,
		np.minimum(background * 2 * foreground, 1.0),
		np.minimum(1.0 - ((1.0 - background) * (1.0 - (foreground - 0.5) * 2.0)), 1.0),
	)


def grainextract(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.GRAINEXTRACT."""
	return np.clip(background - foreground + 0.5, 0.0, 1.0)


def grainmerge(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.GRAINMERGE."""
	return np.clip(background + foreground - 0.5, 0.0, 1.0)


def divide(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.DIVIDE."""
	return np.minimum((256.0 / 255.0 * background) / (1.0 / 255.0 + foreground), 1.0)


def pinlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.PINLIGHT."""
	return np.minimum(background, 2 * foreground) * (foreground < HALF_THRESHOLD) + np.maximum(
		background, 2 * (foreground - 0.5)
	) * (foreground >= HALF_THRESHOLD)


def vividlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.VIVIDLIGHT."""
	return colourburn(background, foreground * 2) * (foreground < HALF_THRESHOLD) + colourdodge(
		background, 2 * (foreground - 0.5)
	) * (foreground >= HALF_THRESHOLD)


def exclusion(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.EXCLUSION."""
	return background + foreground - (2.0 * background * foreground)


def _lum(colours: np.ndarray) -> np.ndarray:
	"""Luminosity.

	:param colours: x by x by 3 matrix of rgb color components of pixels
	:return: x by x by 3 matrix of luminosity of pixels
	"""
	return (colours[:, :, 0] * 0.299) + (colours[:, :, 1] * 0.587) + (colours[:, :, 2] * 0.114)


def _setLum(originalColours: np.ndarray, newLuminosity: np.ndarray) -> np.ndarray:
	"""Set a new luminosity value for the matrix of color."""
	_colours = originalColours.copy()
	_luminosity = _lum(_colours)

	# Apply deltaLum in a single step
	deltaLum = newLuminosity - _luminosity
	_colours += deltaLum[..., None]  # Broadcasting to RGB channels

	# Compute new luminosity, min, and max values
	_luminosity = _lum(_colours)
	minColours = np.min(_colours, axis=2)
	maxColours = np.max(_colours, axis=2)

	# Create masks for values that need adjustment
	minMask = minColours < 0
	maxMask = maxColours > 1

	# Apply min correction
	_colours[minMask] = _luminosity[minMask, None] + (
		(_colours[minMask] - _luminosity[minMask, None]) * _luminosity[minMask, None]
	) / (_luminosity[minMask, None] - minColours[minMask, None])

	# Apply max correction
	_colours[maxMask] = _luminosity[maxMask, None] + (
		(_colours[maxMask] - _luminosity[maxMask, None]) * (1 - _luminosity[maxMask, None])
	) / (maxColours[maxMask, None] - _luminosity[maxMask, None])

	return _colours


def _sat(colours: np.ndarray) -> np.ndarray:
	"""Saturation.

	:param colours: x by x by 3 matrix of rgb color components of pixels
	:return: int of saturation of pixels
	"""
	return np.max(colours, axis=2) - np.min(colours, axis=2)


def _setSat(originalColours: np.ndarray, newSaturation: np.ndarray) -> np.ndarray:
	"""Set a new saturation value for the matrix of color."""
	_colours = originalColours.copy()

	# Sort each pixel's color channels to find min, mid, and max
	sorted_indices = np.argsort(_colours, axis=2)
	minI = sorted_indices[:, :, 0]
	midI = sorted_indices[:, :, 1]
	maxI = sorted_indices[:, :, 2]

	# Extract min, mid, max values
	minColours = np.take_along_axis(_colours, minI[..., None], axis=2).squeeze()
	midColours = np.take_along_axis(_colours, midI[..., None], axis=2).squeeze()
	maxColours = np.take_along_axis(_colours, maxI[..., None], axis=2).squeeze()

	# Compute scaling factor
	rangeColours = maxColours - minColours
	nonzeroMask = rangeColours > 0

	# Apply saturation scaling
	midColours[nonzeroMask] = (
		(midColours[nonzeroMask] - minColours[nonzeroMask]) * newSaturation[nonzeroMask]
	) / rangeColours[nonzeroMask]
	maxColours[nonzeroMask] = newSaturation[nonzeroMask]

	# Zero out mid and max when rangeColours is 0
	midColours[~nonzeroMask] = 0
	maxColours[~nonzeroMask] = 0

	# Set min channel to zero
	minColours.fill(0)

	# Reassemble the color matrix
	np.put_along_axis(_colours, minI[..., None], minColours[..., None], axis=2)
	np.put_along_axis(_colours, midI[..., None], midColours[..., None], axis=2)
	np.put_along_axis(_colours, maxI[..., None], maxColours[..., None], axis=2)

	return _colours


def hue(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.HUE."""
	return _setLum(_setSat(foreground, _sat(background)), _lum(background))


def saturation(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.SATURATION."""
	return _setLum(_setSat(background, _sat(foreground)), _lum(background))


def colour(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.COLOUR."""
	return _setLum(foreground, _lum(background))


def luminosity(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.LUMINOSITY."""
	return _setLum(background, _lum(foreground))


def destin(
	backgroundAlpha: np.ndarray,
	foregroundAlpha: np.ndarray,
	backgroundColour: np.ndarray,
	foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
	"""'clip' composite mode.

	All parts of 'layer above' which are alpha in 'layer below' will be made
	also alpha in 'layer above'
	(to whatever degree of alpha they were)

	Destination which overlaps the source, replaces the source.

	Fa = 0; Fb = as
	co = ab x Cb x as
	ao = ab x as
	"""
	del foregroundColour  # Not used by function
	outAlpha = backgroundAlpha * foregroundAlpha
	with np.errstate(divide="ignore", invalid="ignore"):
		outRGB = np.divide(
			np.multiply((backgroundAlpha * foregroundAlpha)[:, :, None], backgroundColour),
			outAlpha[:, :, None],
		)
	return outRGB, outAlpha


def destout(
	backgroundAlpha: np.ndarray,
	foregroundAlpha: np.ndarray,
	backgroundColour: np.ndarray,
	foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
	"""Reverse 'Clip' composite mode.

	All parts of 'layer below' which are alpha in 'layer above' will be made
	also alpha in 'layer below'
	(to whatever degree of alpha they were)

	"""
	del foregroundColour  # Not used by function
	outAlpha = backgroundAlpha * (1 - foregroundAlpha)
	with np.errstate(divide="ignore", invalid="ignore"):
		outRGB = np.divide(
			np.multiply((backgroundAlpha * (1 - foregroundAlpha))[:, :, None], backgroundColour),
			outAlpha[:, :, None],
		)
	return outRGB, outAlpha


def destatop(
	backgroundAlpha: np.ndarray,
	foregroundAlpha: np.ndarray,
	backgroundColour: np.ndarray,
	foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
	"""Place the layer below above the 'layer above' in places where the 'layer above' exists...

	where 'layer below' does not exist, but 'layer above' does, place 'layer-above'

	"""
	outAlpha = (foregroundAlpha * (1 - backgroundAlpha)) + (backgroundAlpha * foregroundAlpha)
	with np.errstate(divide="ignore", invalid="ignore"):
		outRGB = np.divide(
			np.multiply((foregroundAlpha * (1 - backgroundAlpha))[:, :, None], foregroundColour)
			+ np.multiply((backgroundAlpha * foregroundAlpha)[:, :, None], backgroundColour),
			outAlpha[:, :, None],
		)
	return outRGB, outAlpha


def srcatop(
	backgroundAlpha: np.ndarray,
	foregroundAlpha: np.ndarray,
	backgroundColour: np.ndarray,
	foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
	"""Place the layer below above the 'layer above' in places where the 'layer above' exists."""
	outAlpha = (foregroundAlpha * backgroundAlpha) + (backgroundAlpha * (1 - foregroundAlpha))
	with np.errstate(divide="ignore", invalid="ignore"):
		outRGB = np.divide(
			np.multiply((foregroundAlpha * backgroundAlpha)[:, :, None], foregroundColour)
			+ np.multiply((backgroundAlpha * (1 - foregroundAlpha))[:, :, None], backgroundColour),
			outAlpha[:, :, None],
		)

	return outRGB, outAlpha


def imageIntToFloat(image: np.ndarray) -> np.ndarray:
	"""Convert a numpy array representing an image to an array of floats.

	Args:
	----
		image (np.ndarray): numpy array of ints

	Returns:
	-------
		np.ndarray: numpy array of floats

	"""
	return image / 255


def imageFloatToInt(image: np.ndarray) -> np.ndarray:
	"""Convert a numpy array representing an image to an array of ints.

	Args:
	----
		image (np.ndarray): numpy array of floats

	Returns:
	-------
		np.ndarray: numpy array of ints

	"""
	clippedIm = np.clip((image * 255).round(), 0, 255)
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore", category=RuntimeWarning)
		return clippedIm.astype(np.uint8)


def blend(background: np.ndarray, foreground: np.ndarray, blendType: BlendType) -> np.ndarray:
	"""Blend pixels.

	Args:
	----
		background (np.ndarray): background
		foreground (np.ndarray): foreground
		blendType (BlendType): the blend type

	Returns:
	-------
		np.ndarray: new array representing the image

	background: np.ndarray,
	foreground: np.ndarray and the return are in the form

		[[[0. 0. 0.]
		[0. 0. 0.]
		[0. 0. 0.]
		...
		[0. 0. 0.]
		[0. 0. 0.]
		[0. 0. 0.]]

		...

		[[0. 0. 0.]
		[0. 0. 0.]
		[0. 0. 0.]
		...
		[0. 0. 0.]
		[0. 0. 0.]
		[0. 0. 0.]]]

	"""
	blendLookup = {
		BlendType.NORMAL: normal,
		BlendType.MULTIPLY: multiply,
		BlendType.COLOURBURN: colourburn,
		BlendType.COLOURDODGE: colourdodge,
		BlendType.REFLECT: reflect,
		BlendType.OVERLAY: overlay,
		BlendType.DIFFERENCE: difference,
		BlendType.LIGHTEN: lighten,
		BlendType.DARKEN: darken,
		BlendType.SCREEN: screen,
		BlendType.SOFTLIGHT: softlight,
		BlendType.HARDLIGHT: hardlight,
		BlendType.GRAINEXTRACT: grainextract,
		BlendType.GRAINMERGE: grainmerge,
		BlendType.DIVIDE: divide,
		BlendType.HUE: hue,
		BlendType.SATURATION: saturation,
		BlendType.COLOUR: colour,
		BlendType.LUMINOSITY: luminosity,
		BlendType.XOR: xor,
		BlendType.NEGATION: negation,
		BlendType.PINLIGHT: pinlight,
		BlendType.VIVIDLIGHT: vividlight,
		BlendType.EXCLUSION: exclusion,
	}

	if blendType not in blendLookup:
		return normal(background, foreground)
	return blendLookup[blendType](background, foreground)


def blendLayers(
	background: Image.Image,
	foreground: Image.Image,
	blendType: BlendType,
	opacity: float = 1.0,
	offsets: tuple[int, int] = (0, 0),
) -> Image.Image:
	"""Blend two layers (background and foreground), where the background may
	be cropped if smaller than the foreground.

	:param Image.Image background: The background layer.
	:param Image.Image foreground: The foreground layer (must be the
	same size as the background).
	:param BlendType blendType: The blend type to be applied.
	:param float opacity: The opacity of the foreground image. Defaults to 1.0. (optional)
	:param tuple[int, int] offsets: Offsets for the foreground layer. Defaults to (0, 0). (optional)
	:return Image.Image: The combined image.

	Examples
	--------
	Blend two layers with default parameters
	>>> combined_image = blendLayers(background_image, foreground_image, BlendType.NORMAL)

	Blend two layers with custom opacity and offsets
	>>> combined_image = blendLayers(
	...	background_image,
	...	foreground_image,
	...	BlendType.MULTIPLY,
	...	opacity=0.7,
	...	offsets=(100, 50)
	...)

	"""
	arr = blendLayersArray(
		background=background,
		foreground=foreground,
		blendType=blendType,
		opacity=opacity,
		offsets=offsets,
	)

	return Image.fromarray(np.uint8(np.around(arr, 0)))


def blendLayersArray(
	background: np.ndarray | Image.Image,
	foreground: np.ndarray | Image.Image,
	blendType: BlendType,
	opacity: float = 1.0,
	offsets: tuple[int, int] = (0, 0),
) -> np.ndarray:
	"""Blend two layers (background and foreground), where the background may
	be cropped if smaller than the foreground.

	:param np.ndarray | Image.Image background: The background layer.
	:param np.ndarray | Image.Image foreground: The foreground layer (must be the
	same size as the background).
	:param BlendType blendType: The blend type to be applied.
	:param float opacity: The opacity of the foreground image. Defaults to 1.0. (optional)
	:param tuple[int, int] offsets: Offsets for the foreground layer. Defaults to (0, 0). (optional)
	:return np.ndarray: The combined image.

	Examples
	--------
	Blend two layers with default parameters
	>>> combined_image = blendLayers(background_image, foreground_image, BlendType.NORMAL)

	Blend two layers with custom opacity and offsets
	>>> combined_image = blendLayers(
	...	background_image,
	...	foreground_image,
	...	BlendType.MULTIPLY,
	...	opacity=0.7,
	...	offsets=(100, 50)
	...)

	"""

	# Convert the Image.Image to a numpy array if required
	bg = np.array(background.convert("RGBA")) if isinstance(background, Image.Image) else background
	fg = np.array(foreground.convert("RGBA")) if isinstance(foreground, Image.Image) else foreground

	# do any offset shifting first
	if offsets[0] > 0:
		fg = np.hstack((np.zeros((bg.shape[0], offsets[0], 4), dtype=np.float64), fg))
	elif offsets[0] < 0:
		if offsets[0] > -1 * fg.shape[1]:
			fg = fg[:, -1 * offsets[0] :, :]
		else:
			# offset offscreen completely, there is nothing left
			return np.zeros(bg.shape, dtype=np.float64)
	if offsets[1] > 0:
		fg = np.vstack((np.zeros((offsets[1], fg.shape[1], 4), dtype=np.float64), fg))
	elif offsets[1] < 0:
		if offsets[1] > -1 * fg.shape[0]:
			fg = fg[-1 * offsets[1] :, :, :]
		else:
			# offset offscreen completely, there is nothing left
			return np.zeros(bg.shape, dtype=np.float64)

	# resize array to fill small images with zeros
	if fg.shape[0] < bg.shape[0]:
		fg = np.vstack(
			(
				fg,
				np.zeros(
					(bg.shape[0] - fg.shape[0], fg.shape[1], 4),
					dtype=np.float64,
				),
			)
		)
	if fg.shape[1] < bg.shape[1]:
		fg = np.hstack(
			(
				fg,
				np.zeros(
					(fg.shape[0], bg.shape[1] - fg.shape[1], 4),
					dtype=np.float64,
				),
			)
		)

	# crop the source if the backdrop is smaller
	fg = fg[: bg.shape[0], : bg.shape[1], :]

	lower_norm = bg / 255.0
	upper_norm = fg / 255.0

	upper_alpha = upper_norm[:, :, 3] * opacity
	lower_alpha = lower_norm[:, :, 3]

	upper_rgb = upper_norm[:, :, :3]
	lower_rgb = lower_norm[:, :, :3]

	alphaFunc = {
		BlendType.DESTIN: destin,
		BlendType.DESTOUT: destout,
		BlendType.SRCATOP: srcatop,
		BlendType.DESTATOP: destatop,
	}

	with np.errstate(invalid="ignore", divide="ignore"):
		if blendType in alphaFunc:
			out_rgb, out_alpha = alphaFunc[blendType](
				lower_alpha, upper_alpha, lower_rgb, upper_rgb
			)
		else:
			out_rgb, out_alpha = alpha_comp_shell(
				lower_alpha, upper_alpha, lower_rgb, upper_rgb, blendType
			)

		return np.nan_to_num(np.dstack((out_rgb, out_alpha)), copy=False) * 255.0


def alpha_comp_shell(
	lower_alpha: np.ndarray,
	upper_alpha: np.ndarray,
	lower_rgb: np.ndarray,
	upper_rgb: np.ndarray,
	blendType: BlendType,
) -> tuple[np.ndarray, np.ndarray]:
	"""
	Implement common transformations occurring in any blend or composite mode.
	"""

	out_alpha = upper_alpha + lower_alpha - (upper_alpha * lower_alpha)

	blend_rgb = blend(lower_rgb, upper_rgb, blendType)

	lower_rgb_factor = (1.0 - upper_alpha) * lower_alpha
	upper_rgb_factor = (1.0 - lower_alpha) * upper_alpha
	blended_rgb_factor = lower_alpha * upper_alpha

	out_rgb = (
		lower_rgb_factor[:, :, None] * lower_rgb
		+ upper_rgb_factor[:, :, None] * upper_rgb
		+ blended_rgb_factor[:, :, None] * blend_rgb
	) / out_alpha[:, :, None]

	return out_rgb, out_alpha
