"""Provide blending functions and types

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

from enum import Enum, auto
import warnings
import numpy as np
import skimage
from PIL import Image

class BlendType(Enum):
	"""Specify supported blend types
	"""
	NORMAL = auto()
	MULTIPLY = auto()
	ADDITIVE = auto()
	COLOURBURN = auto()
	COLOURDODGE = auto()
	REFLECT = auto()
	GLOW = auto()
	OVERLAY = auto()
	DIFFERENCE = auto()
	NEGATION = auto()
	LIGHTEN = auto()
	DARKEN = auto()
	SCREEN = auto()
	XOR = auto()
	SOFTLIGHT = auto()
	HARDLIGHT = auto()
	GRAINEXTRACT = auto()
	GRAINMERGE = auto()
	DIVIDE = auto()
	HUE = auto()
	SATURATION = auto()
	COLOUR = auto()
	LUMINOSITY = auto()
	PINLIGHT = auto()
	VIVIDLIGHT = auto()
	EXCLUSION = auto()
	DESTIN = auto()
	DESTOUT = auto()
	SRCATOP = auto()
	DESTATOP = auto()

def normal(_background, foreground):
	""" BlendType.NORMAL """
	return foreground

def multiply(background, foreground):
	""" BlendType.MULTIPLY """
	return np.clip(foreground * background, 0.0, 1.0)

def additive(background, foreground):
	""" BlendType.ADDITIVE """
	return np.minimum(background + foreground, 1.0)

def colourburn(background, foreground):
	""" BlendType.COLOURBURN """
	with np.errstate(divide='ignore'):
		return np.where(foreground != 0.0, np.maximum(1.0 - ((1.0 -
		background) / foreground), 0.0), 0.0)

def colourdodge(background, foreground):
	""" BlendType.COLOURDODGE """
	with np.errstate(divide='ignore'):
		return np.where(foreground != 1.0, np.minimum(background / (1.0 -
		foreground), 1.0), 1.0)

def reflect(background, foreground):
	""" BlendType.REFLECT """
	with np.errstate(divide='ignore'):
		return np.where(foreground != 1.0, np.minimum((background ** 2) / (1.0
		- foreground), 1.0), 1.0)

def glow(background, foreground):
	""" BlendType.GLOW """
	with np.errstate(divide='ignore'):
		return np.where(background != 1.0, np.minimum((foreground ** 2) / (1.0
		- background), 1.0), 1.0)

def overlay(background, foreground):
	""" BlendType.OVERLAY """
	return np.where(background < 0.5, 2 * background * foreground, 1.0 - (2 *
		(1.0 - background) * (1.0 - foreground)))

def difference(background, foreground):
	""" BlendType.DIFFERENCE """
	return np.abs(background - foreground)

def negation(background, foreground):
	""" BlendType.NEGATION """
	return np.maximum(background - foreground, 0.0)

def lighten(background, foreground):
	""" BlendType.LIGHTEN """
	return np.maximum(background, foreground)

def darken(background, foreground):
	""" BlendType.DARKEN """
	return np.minimum(background, foreground)

def screen(background, foreground):
	""" BlendType.SCREEN """
	return background + foreground - background * foreground

def xor(background, foreground):
	""" BlendType.XOR """
	# XOR requires int values so convert to uint8
	with warnings.catch_warnings():
		warnings.simplefilter('ignore')
		return skimage.img_as_float(skimage.img_as_uint(background) ^
		skimage.img_as_uint(foreground))

def softlight(background, foreground):
	""" BlendType.SOFTLIGHT """
	return (1.0 - background) * background * foreground + background * \
	(1.0 - (1.0 - background) * (1.0 - foreground))

def hardlight(background, foreground):
	""" BlendType.HARDLIGHT """
	return np.where(foreground < 0.5, np.minimum(background * 2 * foreground, 1.0),
		np.minimum(1.0 - ((1.0 - background) * (1.0 - (foreground - 0.5) * 2.0)),
		1.0))

def grainextract(background, foreground):
	""" BlendType.GRAINEXTRACT """
	return np.clip(background - foreground + 0.5, 0.0, 1.0)

def grainmerge(background, foreground):
	""" BlendType.GRAINMERGE """
	return np.clip(background + foreground - 0.5, 0.0, 1.0)

def divide(background, foreground):
	""" BlendType.DIVIDE """
	return np.minimum((256.0 / 255.0 * background) / (1.0 / 255.0 + foreground), 1.0)

def pinlight(background, foreground):
	""" BlendType.PINLIGHT """
	return np.minimum(background, 2 * foreground) * (foreground < 0.5) + np.maximum(
		background,	2 * (foreground - 0.5)) * (foreground >= 0.5)

def vividlight(background, foreground):
	""" BlendType.VIVIDLIGHT """
	return colourburn(background, foreground * 2) * (foreground < 0.5) + colourdodge(
		background, 2 * (foreground - 0.5)) * (foreground >= 0.5)

def exclusion(background, foreground):
	""" BlendType.EXCLUSION """
	return background + foreground - ((2.0 * background * foreground))

def _lum(colours):
	"""
	:param colours: x by x by 3 matrix of rgb color components of pixels
	:return: x by x by 3 matrix of luminosity of pixels
	"""
	return (colours[:, :, 0] * 0.299) + (colours[:, :, 1] * 0.587) + (colours[:, :, 2] * 0.114)

def _setLum(originalColours, newLuminosity):
	"""	Set a new luminosity value for the matrix of color	"""
	_c = originalColours.copy()
	_l = _lum(_c)
	d = newLuminosity - _l
	_c[:, :, 0] += d
	_c[:, :, 1] += d
	_c[:, :, 2] += d
	_l = _lum(_c)
	_n = np.min(_c, axis=2)
	_x = np.max(_c, axis=2)
	for i in range(_c.shape[0]):
		for j in range(_c.shape[1]):
			c = _c[i][j]
			newLuminosity = _l[i, j]
			n = _n[i, j]
			x = _x[i, j]
			if n < 0:
				_c[i][j] = newLuminosity + (((c - newLuminosity) * newLuminosity) / (newLuminosity - n))
			if x > 1:
				_c[i][j] = newLuminosity + (((c - newLuminosity) * (1 - newLuminosity)) / (x - newLuminosity))
	return _c

def _sat(colours):
	"""
	:param colours: x by x by 3 matrix of rgb color components of pixels
	:return: int of saturation of pixels
	"""
	return np.max(colours, axis=2) - np.min(colours, axis=2)


def _setSat(originalColours, newSaturation):
	"""
	Set a new saturation value for the matrix of color

	The current implementation cannot be vectorized in an efficient manner,
	so it is very slow,
	O(m*n) at least. This might be able to be improved with openCL if that is
	the direction that the lib takes.
	:param c: x by x by 3 matrix of rgb color components of pixels
	:param s: int of the new saturation value for the matrix
	:return: x by x by 3 matrix of luminosity of pixels
	"""
	_c = originalColours.copy()
	for i in range(_c.shape[0]):
		for j in range(_c.shape[1]):
			c = _c[i][j]
			min_i = 0
			mid_i = 1
			max_i = 2
			if c[mid_i] < c[min_i]:
				min_i, mid_i = mid_i, min_i
			if c[max_i] < c[mid_i]:
				mid_i, max_i = max_i, mid_i
			if c[mid_i] < c[min_i]:
				min_i, mid_i = mid_i, min_i
			if c[max_i] - c[min_i] > 0.0:
				_c[i][j][mid_i] = (((c[mid_i] - c[min_i]) * newSaturation[i, j]) / (c[max_i] - c[min_i]))
				_c[i][j][max_i] = newSaturation[i, j]
			else:
				_c[i][j][mid_i] = 0
				_c[i][j][max_i] = 0
			_c[i][j][min_i] = 0
	return _c



def hue(background, foreground):
	""" BlendType.HUE """
	return _setLum(_setSat(foreground, _sat(background)), _lum(background))

def saturation(background, foreground):
	""" BlendType.SATURATION """
	return _setLum(_setSat(background, _sat(foreground)), _lum(background))

def colour(background, foreground):
	""" BlendType.COLOUR """
	return _setLum(foreground, _lum(background))

def luminosity(background, foreground):
	""" BlendType.LUMINOSITY """
	return _setLum(background, _lum(foreground))


def destin(backgroundAlpha, foregroundAlpha, backgroundColour, _foregroundColour):
	"""
	'Clip' composite mode
	All parts of 'layer above' which are alpha in 'layer below' will be made
	also alpha in 'layer above'
	(to whatever degree of alpha they were)

	Destination which overlaps the source, replaces the source.

	Fa = 0; Fb = αs
	co = αb x Cb x αs
	αo = αb x αs

	:param source:
	:param destination:
	:return:
	"""
	outAlpha = backgroundAlpha * foregroundAlpha
	with np.errstate(divide='ignore', invalid="ignore"):
		outRGB = np.divide(np.multiply((backgroundAlpha *
		foregroundAlpha)[:, :, None], backgroundColour), outAlpha[:, :, None])
	return outRGB, outAlpha


def destout(backgroundAlpha, foregroundAlpha, backgroundColour, _foregroundColour):
	"""
	reverse 'Clip' composite mode
	All parts of 'layer below' which are alpha in 'layer above' will be made
	also alpha in 'layer below'
	(to whatever degree of alpha they were)
	:param img_in:
	:param img_layer:
	:return:
	"""
	outAlpha = backgroundAlpha * (1 - foregroundAlpha)
	with np.errstate(divide='ignore', invalid="ignore"):
		outRGB = np.divide(np.multiply((backgroundAlpha *
		(1 - foregroundAlpha))[:, :, None], backgroundColour), outAlpha[:, :, None])
	return outRGB, outAlpha

def destatop(backgroundAlpha, foregroundAlpha, backgroundColour, foregroundColour):
	"""
	place the layer below above the 'layer above' in places where the 'layer above' exists
	where 'layer below' does not exist, but 'layer above' does, place 'layer-above'

	:param img_in:
	:param img_layer:
	:return:
	"""
	outAlpha = (foregroundAlpha * (1 - backgroundAlpha)) + (backgroundAlpha * foregroundAlpha)
	with np.errstate(divide='ignore', invalid="ignore"):
		outRGB = np.divide(
			np.multiply((foregroundAlpha * (1 - backgroundAlpha))[:, :, None], foregroundColour) +
			np.multiply((backgroundAlpha * foregroundAlpha)[:, :, None], backgroundColour),
			outAlpha[:, :, None]
		)
	return outRGB, outAlpha



def srcatop(backgroundAlpha, foregroundAlpha, backgroundColour, foregroundColour):
	"""
	place the layer below above the 'layer above' in places where the 'layer above' exists
	:param img_in:
	:param img_layer:
	:return:
	"""

	outAlpha = (foregroundAlpha * backgroundAlpha) + (backgroundAlpha * (1 - foregroundAlpha))
	with np.errstate(divide='ignore', invalid="ignore"):
		outRGB = np.divide(
			np.multiply((foregroundAlpha * backgroundAlpha)[:, :, None], foregroundColour) +
			np.multiply((backgroundAlpha * (1 - foregroundAlpha))[:, :, None], backgroundColour),
			outAlpha[:, :, None]
		)

	return outRGB, outAlpha


def blend(background, foreground, blendType):
	"""blend pixels

	Args:
		background (np.array): background
		foreground (np.array): foreground
		blendType (BlendType): the blend type

	Returns:
		np.array: new array representing the image

	background, foreground and the return are in the form

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
	blendLookup = {BlendType.NORMAL: normal, BlendType.MULTIPLY: multiply,
	BlendType.COLOURBURN: colourburn, BlendType.COLOURDODGE: colourdodge,
	BlendType.REFLECT: reflect, BlendType.OVERLAY: overlay,
	BlendType.DIFFERENCE: difference, BlendType.LIGHTEN: lighten,
	BlendType.DARKEN: darken, BlendType.SCREEN: screen,
	BlendType.SOFTLIGHT: softlight, BlendType.HARDLIGHT: hardlight,
	BlendType.GRAINEXTRACT: grainextract, BlendType.GRAINMERGE: grainmerge,
	BlendType.DIVIDE: divide, BlendType.HUE: hue, BlendType.SATURATION: saturation,
	BlendType.COLOUR: colour, BlendType.LUMINOSITY: luminosity,
	BlendType.XOR: xor, BlendType.NEGATION: negation,
	BlendType.PINLIGHT: pinlight, BlendType.VIVIDLIGHT: vividlight,
	BlendType.EXCLUSION: exclusion}

	if blendType not in blendLookup:
		return normal(background, foreground)
	return blendLookup[blendType](background, foreground)


def blendLayers(background, foreground, blendType, opacity=1.0):
	"""Blend layers using numpy array

	Args:
		background (PIL.Image): background layer
		foreground (PIL.Image): foreground layer (must be same size as background)
		blendType (BlendType): The blendtype
		opacity (float): The opacity of the foreground image

	Returns:
		PIL.Image: combined image
	"""
	# Convert the PIL.Image to a numpy array
	foreground = skimage.img_as_float(np.array(foreground))
	background = skimage.img_as_float(np.array(background))

	# Get the alpha from the layers
	backgroundAlpha = background[:, :, 3]
	foregroundAlpha = foreground[:, :, 3] * opacity
	combinedAlpha = backgroundAlpha * foregroundAlpha

	# Get the colour from the layers
	backgroundColor = background[:, :, 0:3]
	foregroundColor = foreground[:, :, 0:3]

	# Some effects require alpha
	alphaFunc = {BlendType.DESTIN: destin, BlendType.DESTOUT: destout,
	BlendType.SRCATOP: srcatop, BlendType.DESTATOP: destatop}

	if blendType in alphaFunc:
		return Image.fromarray(skimage.img_as_ubyte(np.clip(np.dstack(
		alphaFunc[blendType](backgroundAlpha, foregroundAlpha, backgroundColor,
		foregroundColor)), a_min=0, a_max=1)))

	# Get the colours and the alpha for the new image
	colorComponents = (backgroundAlpha - combinedAlpha)[:, :,
	None] * backgroundColor + (foregroundAlpha - combinedAlpha)[:, :,
	None] * foregroundColor + combinedAlpha[:, :, None] * blend(backgroundColor,
	foregroundColor, blendType)
	alphaComponent = backgroundAlpha + foregroundAlpha - combinedAlpha

	return Image.fromarray(skimage.img_as_ubyte(np.clip(
		np.dstack((colorComponents, alphaComponent)), a_min=0, a_max=1)))
