# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2025 - 2025/02/20

- optimise `_setLum` and `_setSat` functions
- use uv instead of poetry

## 2024.1.1 - 2024/03/17

- suppress warnings

## 2024.1 - 2024/01/27

- remove `imagetools.renderWAlphaOffset` as `blendLayers` now supports this:
  ```py
	def blendLayers(
		background: Image.Image,
		foreground: Image.Image,
		blendType: BlendType | tuple[str, ...],
		opacity: float = 1.0,
		offsets: tuple[int, int] = (0, 0),
	) -> Image.Image:
  ```
- better support for different sized images. Note if the background is smaller than the
  foreground then some of the foreground will be cut off

## 2024.0.1 - 2024/01/19

- update dependencies
- ruff linting

## 2024 - 2024/01/07

- update dependencies

## 2023 - 2023/08/31

- Update deps

## 2022 - 2022/01/23

- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Update tests
- Update deps

## 2021.3.3 - 2021/10/28

- Fix crash due to deprecation using a different function signature

## 2021.3.2 - 2021/10/26

- Use pre-commit to enforce reasonable standards + consistency
- Update readme with improved docs on installing and running python (fairly generic)
- Remove classifiers for license + python versions and rely on poetry to generate these
- Update tooling config (pyproject.toml)
- Convert images to RGBA for blending https://github.com/FHPythonUtils/BlendModes/issues/2

## 2021.3.1 - 2021/10/14

- Use pre-commit to enforce reasonable standards + consistency
- Update readme with improved docs on installing and running python (fairly generic)
- Remove classifiers for license + python versions and rely on poetry to generate these
- Update tooling config (pyproject.toml)

## 2021.3 - 2021/07/24

- use aenum

## 2021.2 - 2021/07/23

- Mark deprecated functions with @deprecated decorator
- add blendtype.py and change BlendType to str enum

## 2021.1 - 2021/06/08

- Deprecated 'raster' functions and replaced with more accurate naming
- Typing improvements
- Update deps

## 2021 - 2021/04/16

- Updated typing (removed data-science-types)
- Updated formatting
- Improved docstrings
- Update tests

## 2020.3 - 2020/10/29

- Using FHMake to build
- Added type hinting
- Dropped support for python < 3.7
- Added support for python 3.9

## 2020.2.2 - 2020/05/08

- Removed `scikit-image`
- Now compatible with python 3.5

## 2020.2.1 - 2020/05/06

- Updated classifiers

## 2020.2 - 2020/05/02

- Added destin, destout, destatop and srcatop
- Updated license with credits
- Added credits to readme (these were previously in the source file)

## 2020.1 - 2020/05/01

- Added pinlight, vividlight and exclusion
- Fix hardlight, negation

## 2020 - 2020/05/01

- First release
