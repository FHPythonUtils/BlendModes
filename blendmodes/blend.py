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

from .blendtype import BlendType


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
		background < 0.5,
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
		foreground < 0.5,
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
	return np.minimum(background, 2 * foreground) * (foreground < 0.5) + np.maximum(
		background, 2 * (foreground - 0.5)
	) * (foreground >= 0.5)


def vividlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
	"""BlendType.VIVIDLIGHT."""
	return colourburn(background, foreground * 2) * (foreground < 0.5) + colourdodge(
		background, 2 * (foreground - 0.5)
	) * (foreground >= 0.5)


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
	deltaLum = newLuminosity - _luminosity
	_colours[:, :, 0] += deltaLum
	_colours[:, :, 1] += deltaLum
	_colours[:, :, 2] += deltaLum
	_luminosity = _lum(_colours)
	_minColours = np.min(_colours, axis=2)
	_MaxColours = np.max(_colours, axis=2)
	for i in range(_colours.shape[0]):
		for j in range(_colours.shape[1]):
			_colour = _colours[i][j]
			newLuminosity = _luminosity[i, j]
			minColour = _minColours[i, j]
			maxColour = _MaxColours[i, j]
			if minColour < 0:
				_colours[i][j] = newLuminosity + (
					((_colour - newLuminosity) * newLuminosity) / (newLuminosity - minColour)
				)
			if maxColour > 1:
				_colours[i][j] = newLuminosity + (
					((_colour - newLuminosity) * (1 - newLuminosity)) / (maxColour - newLuminosity)
				)
	return _colours


def _sat(colours: np.ndarray) -> np.ndarray:
	"""Saturation.

	:param colours: x by x by 3 matrix of rgb color components of pixels
	:return: int of saturation of pixels
	"""
	return np.max(colours, axis=2) - np.min(colours, axis=2)


def _setSat(originalColours: np.ndarray, newSaturation: np.ndarray) -> np.ndarray:
	"""Set a new saturation value for the matrix of color.

	The current implementation cannot be vectorized in an efficient manner,
	so it is very slow,
	O(m*n) at least. This might be able to be improved with openCL if that is
	the direction that the lib takes.
	:param c: x by x by 3 matrix of rgb color components of pixels
	:param s: int of the new saturation value for the matrix
	:return: x by x by 3 matrix of luminosity of pixels
	"""
	_colours = originalColours.copy()
	for i in range(_colours.shape[0]):
		for j in range(_colours.shape[1]):
			_colour = _colours[i][j]
			minI = 0
			midI = 1
			maxI = 2
			if _colour[midI] < _colour[minI]:
				minI, midI = midI, minI
			if _colour[maxI] < _colour[midI]:
				midI, maxI = maxI, midI
			if _colour[midI] < _colour[minI]:
				minI, midI = midI, minI
			if _colour[maxI] - _colour[minI] > 0.0:
				_colours[i][j][midI] = ((_colour[midI] - _colour[minI]) * newSaturation[i, j]) / (
					_colour[maxI] - _colour[minI]
				)
				_colours[i][j][maxI] = newSaturation[i, j]
			else:
				_colours[i][j][midI] = 0
				_colours[i][j][maxI] = 0
			_colours[i][j][minI] = 0
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
	blendType: BlendType | tuple[str, ...],
	opacity: float = 1.0,
	offsets: tuple[int, int] = (0, 0),
) -> Image.Image:
	"""Blend two layers (background, and foreground).

	Note if the background is smaller than the foreground then some of the foreground will be cut
	off

	Args:
	----
		background (Image.Image): The background layer.
		foreground (Image.Image): The foreground layer (must be the same size as the background).
		blendType (BlendType): The blend type to be applied.
		opacity (float, optional): The opacity of the foreground image. Defaults to 1.0.
		offsets (Tuple[int, int], optional): Offsets for the foreground layer. Defaults to (0, 0).

	Returns:
	-------
		Image.Image: The combined image.

	Examples:
	--------
		# Blend two layers with default parameters
		combined_image = blendLayers(background_image, foreground_image, BlendType.NORMAL)

		# Blend two layers with custom opacity and offsets
		combined_image = blendLayers(
			background_image,
			foreground_image,
			BlendType.MULTIPLY,
			opacity=0.7,
			offsets=(100, 50)
		)

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
	"""Blend two layers (background, and foreground).

	Note if the background is smaller than the foreground then some of the foreground will be cut
	off

	Args:
	----
		background (np.ndarray | Image.Image): The background layer.
		foreground (np.ndarray | Image.Image): The foreground layer (must be the same size as the background).
		blendType (BlendType): The blend type to be applied.
		opacity (float, optional): The opacity of the foreground image. Defaults to 1.0.
		offsets (Tuple[int, int], optional): Offsets for the foreground layer. Defaults to (0, 0).

	Returns:
	-------
		np.ndarray: The combined image.

	Examples:
	--------
		# Blend two layers with default parameters
		combined_image = blendLayers(background_image, foreground_image, BlendType.NORMAL)

		# Blend two layers with custom opacity and offsets
		combined_image = blendLayers(
			background_image,
			foreground_image,
			BlendType.MULTIPLY,
			opacity=0.7,
			offsets=(100, 50)
		)

	"""
	# Convert the Image.Image to a numpy array if required
	if isinstance(background, Image.Image):
		background = np.array(background.convert("RGBA"))
	if isinstance(foreground, Image.Image):
		foreground = np.array(foreground.convert("RGBA"))

	# do any offset shifting first
	if offsets[0] > 0:
		foreground = np.hstack(
			(np.zeros((foreground.shape[0], offsets[0], 4), dtype=np.float64), foreground)
		)
	elif offsets[0] < 0:
		if offsets[0] > -1 * foreground.shape[1]:
			foreground = foreground[:, -1 * offsets[0] :, :]
		else:
			# offset offscreen completely, there is nothing left
			return np.zeros(background.shape, dtype=np.float64)
	if offsets[1] > 0:
		foreground = np.vstack(
			(np.zeros((offsets[1], foreground.shape[1], 4), dtype=np.float64), foreground)
		)
	elif offsets[1] < 0:
		if offsets[1] > -1 * foreground.shape[0]:
			foreground = foreground[-1 * offsets[1] :, :, :]
		else:
			# offset offscreen completely, there is nothing left
			return np.zeros(background.shape, dtype=np.float64)

	# resize array to fill small images with zeros
	if foreground.shape[0] < background.shape[0]:
		foreground = np.vstack(
			(
				foreground,
				np.zeros(
					(background.shape[0] - foreground.shape[0], foreground.shape[1], 4),
					dtype=np.float64,
				),
			)
		)
	if foreground.shape[1] < background.shape[1]:
		foreground = np.hstack(
			(
				foreground,
				np.zeros(
					(foreground.shape[0], background.shape[1] - foreground.shape[1], 4),
					dtype=np.float64,
				),
			)
		)

	# crop the source if the backdrop is smaller
	foreground = foreground[: background.shape[0], : background.shape[1], :]

	lower_norm = background / 255.0
	upper_norm = foreground / 255.0

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
	blendType: BlendType | tuple[str, ...],
) -> tuple[np.ndarray, np.ndarray]:
	"""
	Implement common transformations occurring in any blend or composite mode.
	"""

	out_alpha = upper_alpha + lower_alpha - (upper_alpha * lower_alpha)

	blend_rgb = blend(lower_rgb, upper_rgb, blendType)

	lower_rgb_part = np.multiply(((1.0 - upper_alpha) * lower_alpha)[:, :, None], lower_rgb)
	upper_rgb_part = np.multiply(((1.0 - lower_alpha) * upper_alpha)[:, :, None], upper_rgb)
	blended_rgb_part = np.multiply((lower_alpha * upper_alpha)[:, :, None], blend_rgb)

	out_rgb = np.divide((lower_rgb_part + upper_rgb_part + blended_rgb_part), out_alpha[:, :, None])

	return out_rgb, out_alpha
