import subprocess

# ruff: noqa: S603, S607


def test_blend_cli() -> None:
	result = subprocess.run(
		[
			"blendmodes",
			"blend",
			"tests/data/src/rainbow.png",
			"tests/data/src/duck.png",
			"--blend",
			"multiply",
			"--output",
			"out.png",
		],
		capture_output=True,
		text=True,
		check=False,
	)
	assert "writing the result to" in result.stdout
