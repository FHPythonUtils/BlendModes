from __future__ import annotations

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


# Create a solid color image
def create_solid_color_image(
	size: tuple[int, int] = (400, 400), color: tuple[int, ...] = (255, 0, 0, 255)
) -> Image.Image:
	img = Image.new("RGBA", size, color)
	img.save("solid_color.png")
	return img


# Create a gradient image
def create_gradient_image(
	size: tuple[int, int] = (400, 400),
	start_color: tuple[int, ...] = (0, 0, 255),
	end_color: tuple[int, ...] = (255, 0, 0),
) -> Image.Image:
	img = Image.new("RGB", size)
	for x in range(size[0]):
		blend_factor = x / size[0]
		color = (
			int(start_color[0] * (1 - blend_factor) + end_color[0] * blend_factor),
			int(start_color[1] * (1 - blend_factor) + end_color[1] * blend_factor),
			int(start_color[2] * (1 - blend_factor) + end_color[2] * blend_factor),
		)
		ImageDraw.Draw(img).line([(x, 0), (x, size[1])], fill=color)
	img.save("gradient.png")
	return img


# Create a soft-edged circular mask
def create_soft_mask(size: tuple[int, int] = (400, 400)) -> Image.Image:
	img = Image.new("L", size, 0)
	draw = ImageDraw.Draw(img)
	draw.ellipse((50, 50, size[0] - 50, size[1] - 50), fill=255)
	img = img.filter(ImageFilter.GaussianBlur(20))
	img.save("soft_mask.png")
	return img


# Create a noisy texture
def create_noise_texture(size: tuple[int, int] = (400, 400)) -> Image.Image:

	rng = np.random.default_rng()
	noise_array = rng.integers(0, 255, (size[1], size[0]), dtype=np.uint8)
	img = Image.fromarray(noise_array, mode="L")
	img.save("noise_texture.png")
	return img


# Create a silhouette image (e.g., black cat)
def create_silhouette(shape:str="circle") -> Image.Image:
	img = Image.new("RGBA", size=(400, 400), color=(255, 255, 255, 0))
	draw = ImageDraw.Draw(img)
	if shape == "circle":
		draw.ellipse((100, 100, 300, 300), fill=(50, 0, 50, 255))
	elif shape == "rectangle":
		draw.rectangle((100, 150, 300, 350), fill=(50, 0, 50, 255))
	img.save(f"{shape}_silhouette.png")
	return img


def create_red_soft_mask(size: tuple[int, int] = (400, 400)) -> Image.Image:
	# Create an RGBA image with transparency
	img = Image.new("RGBA", size, (255, 255, 255, 0))
	mask = Image.new("L", size, 0)  # Grayscale mask for blurring

	draw = ImageDraw.Draw(mask)
	draw.ellipse((50, 50, size[0] - 50, size[1] - 50), fill=255)
	mask = mask.filter(ImageFilter.GaussianBlur(30))  # Feather effect

	# Apply the mask as alpha channel to a red image
	red_layer = Image.new("RGBA", size, (255, 0, 0, 255))  # Solid red
	img = Image.composite(red_layer, img, mask)  # Blend using mask

	img.save("red_soft_mask.png")
	return img


# Generate all images
create_solid_color_image()
create_gradient_image()
create_soft_mask()
create_noise_texture()
create_silhouette("circle")
create_silhouette("rectangle")
create_red_soft_mask()
