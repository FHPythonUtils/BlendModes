[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/BlendModes.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/7df4678b2a2145119898ce3a9be8b5fc.svg?style=for-the-badge)](https://www.codacy.com/manual/FHPythonUtils/BlendModes)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/BlendModes.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/BlendModes.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/BlendModes.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/BlendModes.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/BlendModes.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/blendmodes.svg?style=for-the-badge)](https://pypi.org/project/blendmodes/)
[![PyPI Version](https://img.shields.io/pypi/v/blendmodes.svg?style=for-the-badge)](https://pypi.org/project/blendmodes/)

<!-- omit in TOC -->
# BlendModes

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Use this module to apply a number of blending modes to a background and
foreground image.

## Credits

Credits to:

### MIT License Copyright (c) 2019 Paul Jewell
For implementing blending from the Open Raster Image Spec

### MIT License Copyright (c) 2018 Addison Elliott
For implementing blending from Paint.NET

### MIT License Copyright (c) 2017 pashango
For implementing a number of blending functions used by other popular image
editors

- [Credits](#credits)
	- [MIT License Copyright (c) 2019 Paul Jewell](#mit-license-copyright-c-2019-paul-jewell)
	- [MIT License Copyright (c) 2018 Addison Elliott](#mit-license-copyright-c-2018-addison-elliott)
	- [MIT License Copyright (c) 2017 pashango](#mit-license-copyright-c-2017-pashango)
- [Docs](#docs)
- [Examples](#examples)
	- [Normal](#normal)
	- [Multiply](#multiply)
	- [Additive](#additive)
	- [ColourBurn](#colourburn)
	- [ColourDodge](#colourdodge)
	- [Reflect](#reflect)
	- [Glow](#glow)
	- [Overlay](#overlay)
	- [Difference](#difference)
	- [Negation](#negation)
	- [Lighten](#lighten)
	- [Darken](#darken)
	- [Screen](#screen)
	- [XOR](#xor)
	- [SoftLight](#softlight)
	- [HardLight](#hardlight)
	- [GrainExtract](#grainextract)
	- [GrainMerge](#grainmerge)
	- [Divide](#divide)
	- [Hue](#hue)
	- [Saturation](#saturation)
	- [Colour](#colour)
	- [Luminosity](#luminosity)
	- [PinLight](#pinlight)
	- [VividLight](#vividlight)
	- [Exclusion](#exclusion)
	- [DestIn](#destin)
	- [DestOut](#destout)
	- [DestAtop](#destatop)
	- [SrcAtop](#srcatop)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [How to update, build and publish](#how-to-update-build-and-publish)
- [Download](#download-1)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)

## Docs
See the [Docs](/DOCS.md) for more information.

Generate with pydoc-markdown 3
```bash
pydoc-markdown > DOCS.md
```
Alternatively use `make.py` to run a load of commands


## Examples

Be sure to include the following for the functions below
```python
from blendmodes.blend import blendLayers, BlendType

background = Image.open(THISDIR + "/background.png")
foreground = Image.open(THISDIR + "/foreground.png")
```

### Normal

```python
blendLayers(background, foreground, BlendType.NORMAL)
```
![Normal](test/normal_expected.png)

### Multiply

```python
blendLayers(background, foreground, BlendType.MULTIPLY)
```
![Multiply](test/multiply_expected.png)

### Additive

```python
blendLayers(background, foreground, BlendType.ADDITIVE)
```
![Additive](test/additive_expected.png)

### ColourBurn

```python
blendLayers(background, foreground, BlendType.COLOURBURN)
```
![ColourBurn](test/colourburn_expected.png)

### ColourDodge

```python
blendLayers(background, foreground, BlendType.COLOURDODGE)
```
![ColourDodge](test/colourdodge_expected.png)

### Reflect

```python
blendLayers(background, foreground, BlendType.REFLECT)
```
![Reflect](test/reflect_expected.png)

### Glow

```python
blendLayers(background, foreground, BlendType.GLOW)
```
![Glow](test/glow_expected.png)

### Overlay

```python
blendLayers(background, foreground, BlendType.OVERLAY)
```
![Overlay](test/overlay_expected.png)

### Difference

```python
blendLayers(background, foreground, BlendType.DIFFERENCE)
```
![Difference](test/difference_expected.png)

### Negation

```python
blendLayers(background, foreground, BlendType.NEGATION)
```
![Negation](test/negation_expected.png)

### Lighten

```python
blendLayers(background, foreground, BlendType.LIGHTEN)
```
![Lighten](test/lighten_expected.png)

### Darken

```python
blendLayers(background, foreground, BlendType.DARKEN)
```
![Darken](test/darken_expected.png)

### Screen

```python
blendLayers(background, foreground, BlendType.SCREEN)
```
![Screen](test/screen_expected.png)

### XOR

```python
blendLayers(background, foreground, BlendType.XOR)
```
![XOR](test/xor_expected.png)

### SoftLight

```python
blendLayers(background, foreground, BlendType.SOFTLIGHT)
```
![SoftLight](test/softlight_expected.png)

### HardLight

```python
blendLayers(background, foreground, BlendType.HARDLIGHT)
```
![HardLight](test/hardlight_expected.png)

### GrainExtract

```python
blendLayers(background, foreground, BlendType.GRAINEXTRACT)
```
![GrainExtract](test/grainextract_expected.png)

### GrainMerge

```python
blendLayers(background, foreground, BlendType.GRAINMERGE)
```
![GrainMerge](test/grainmerge_expected.png)

### Divide

```python
blendLayers(background, foreground, BlendType.DIVIDE)
```
![Divide](test/divide_expected.png)

### Hue

```python
blendLayers(background, foreground, BlendType.HUE)
```
![Hue](test/hue_expected.png)

### Saturation

```python
blendLayers(background, foreground, BlendType.SATURATION)
```
![Saturation](test/saturation_expected.png)

### Colour

```python
blendLayers(background, foreground, BlendType.COLOUR)
```
![Colour](test/colour_expected.png)

### Luminosity

```python
blendLayers(background, foreground, BlendType.LUMINOSITY)
```
![Luminosity](test/luminosity_expected.png)

### PinLight

```python
blendLayers(background, foreground, BlendType.PINLIGHT)
```
![PinLight](test/pinlight_expected.png)

### VividLight

```python
blendLayers(background, foreground, BlendType.VIVIDLIGHT)
```
![VividLight](test/vividlight_expected.png)

### Exclusion

```python
blendLayers(background, foreground, BlendType.EXCLUSION)
```
![Exclusion](test/exclusion_expected.png)

### DestIn

```python
blendLayers(background, foreground, BlendType.DESTIN)
```
![Exclusion](test/destin_expected.png)

### DestOut

```python
blendLayers(background, foreground, BlendType.DESTOUT)
```
![Exclusion](test/destout_expected.png)

### DestAtop

```python
blendLayers(background, foreground, BlendType.DESTATOP)
```
![Exclusion](test/destatop_expected.png)

### SrcAtop

```python
blendLayers(background, foreground, BlendType.SRCATOP)
```
![Exclusion](test/srcatop_expected.png)

## Install With PIP

```python
pip install blendmodes
```

Head to https://pypi.org/project/blendmodes/ for more info


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/BlendModes
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.
