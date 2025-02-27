from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import numpy as np
from loguru import logger
from PIL import Image

from blendmodes.blend import blendLayersArray
from blendmodes.blendtype import BlendType
from blendmodes.imgdiff import image_diff_array

logger.remove()
logger.add(sys.stdout, level="INFO", format="<level>{level: <8}</level> | {message}")


def get_im_np(image: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> np.ndarray:
	"""Convert image at path to RGBA NumPy array."""
	img = image if isinstance(image, Image.Image) else Image.open(image).convert("RGBA")
	return np.array(img)


def main() -> None:
	# Parent parser with shared arguments
	common_parser = argparse.ArgumentParser(add_help=False)
	common_parser.add_argument("image1", type=Path, help="Path to the first image (background)")
	common_parser.add_argument("image2", type=Path, help="Path to the second image (foreground)")

	# Main parser
	parser = argparse.ArgumentParser(description="Blend or compare two images")
	subparsers = parser.add_subparsers(dest="command", required=True)

	# Blend Subcommand
	blend_parser = subparsers.add_parser("blend", parents=[common_parser], help="Blend two images")
	blend_parser.add_argument(
		"--blend",
		"-b",
		choices=[alias.lower() for mode in BlendType for alias in mode.values],
		help="Blend mode to use (e.g. normal, multiply, screen)",
	)
	blend_parser.add_argument("--output", "-o", type=Path, required=True, help="Output image path")

	# Diff Subcommand
	subparsers.add_parser("diff", parents=[common_parser], help="Compare two images")

	# Parse arguments
	args = parser.parse_args()

	img1 = get_im_np(args.image1)
	img2 = get_im_np(args.image2)

	if args.command == "diff":
		diff = image_diff_array(img1, img2)
		logger.info(
			f"Comparing {args.image1.name} and {args.image2.name} are {diff * 100:.2f}% different"
		)

	else:
		result = blendLayersArray(img1, img2, args.blend)
		result_im = Image.fromarray(np.uint8(np.around(result, 0)))
		result_im.save(args.output)
		logger.info(
			f"Blending {args.image1.name} and {args.image2.name} and "
			f"writing the result to {args.output}"
		)


if __name__ == "__main__":
	main()
