""" Do stuff to images to prepare them
"""
from PIL import Image


def rasterImageOA(image, size, alpha=1.0, offsets=(0, 0)):
	""" Rasterise an image with offset and alpha to a given size"""
	imageOffset = rasterImageOffset(image, size, offsets)
	return Image.blend(Image.new("RGBA", size), imageOffset, alpha)

def rasterImageOffset(image, size, offsets=(0, 0)):
	""" Rasterise an image with offset to a given size"""
	imageOffset = Image.new("RGBA", size)
	imageOffset.paste(image.convert("RGBA"), offsets, image.convert("RGBA"))
	return imageOffset
