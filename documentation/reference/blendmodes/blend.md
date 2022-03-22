# Blend

> Auto-generated documentation for [blendmodes.blend](../../../blendmodes/blend.py) module.

Provide blending functions and types.

- [Blendmodes](../README.md#blendmodes-index) / [Modules](../MODULES.md#blendmodes-modules) / [Blendmodes](index.md#blendmodes) / Blend
    - [additive](#additive)
    - [blend](#blend)
    - [blendLayers](#blendlayers)
    - [colour](#colour)
    - [colourburn](#colourburn)
    - [colourdodge](#colourdodge)
    - [darken](#darken)
    - [destatop](#destatop)
    - [destin](#destin)
    - [destout](#destout)
    - [difference](#difference)
    - [divide](#divide)
    - [exclusion](#exclusion)
    - [glow](#glow)
    - [grainextract](#grainextract)
    - [grainmerge](#grainmerge)
    - [hardlight](#hardlight)
    - [hue](#hue)
    - [imageFloatToInt](#imagefloattoint)
    - [imageIntToFloat](#imageinttofloat)
    - [lighten](#lighten)
    - [luminosity](#luminosity)
    - [multiply](#multiply)
    - [negation](#negation)
    - [normal](#normal)
    - [overlay](#overlay)
    - [pinlight](#pinlight)
    - [reflect](#reflect)
    - [saturation](#saturation)
    - [screen](#screen)
    - [softlight](#softlight)
    - [srcatop](#srcatop)
    - [vividlight](#vividlight)
    - [xor](#xor)

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

## additive

[[find in source code]](../../../blendmodes/blend.py#L41)

```python
def additive(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.ADDITIVE.

## blend

[[find in source code]](../../../blendmodes/blend.py#L384)

```python
def blend(
    background: np.ndarray,
    foreground: np.ndarray,
    blendType: BlendType,
) -> np.ndarray:
```

Blend pixels.

#### Arguments

- `background` *np.ndarray* - background
- `foreground` *np.ndarray* - foreground
- `blendType` *BlendType* - the blend type

#### Returns

- `np.ndarray` - new array representing the image

- `background` - np.ndarray,
- `foreground` - np.ndarray and the return are in the form

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

## blendLayers

[[find in source code]](../../../blendmodes/blend.py#L448)

```python
def blendLayers(
    background: Image.Image,
    foreground: Image.Image,
    blendType: BlendType | tuple[str, ...],
    opacity: float = 1.0,
) -> Image.Image:
```

Blend layers using numpy array.

#### Arguments

- `background` *Image.Image* - background layer
- `foreground` *Image.Image* - foreground layer (must be same size as background)
- `blendType` *BlendType* - The blendtype
- `opacity` *float* - The opacity of the foreground image

#### Returns

- `Image.Image` - combined image

## colour

[[find in source code]](../../../blendmodes/blend.py#L260)

```python
def colour(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.COLOUR.

## colourburn

[[find in source code]](../../../blendmodes/blend.py#L46)

```python
def colourburn(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.COLOURBURN.

## colourdodge

[[find in source code]](../../../blendmodes/blend.py#L54)

```python
def colourdodge(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.COLOURDODGE.

## darken

[[find in source code]](../../../blendmodes/blend.py#L100)

```python
def darken(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.DARKEN.

## destatop

[[find in source code]](../../../blendmodes/blend.py#L321)

```python
def destatop(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
):
```

Place the layer below above the 'layer above' in places where the 'layer above' exists...

where 'layer below' does not exist, but 'layer above' does, place 'layer-above'

## destin

[[find in source code]](../../../blendmodes/blend.py#L270)

```python
def destin(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
):
```

'clip' composite mode.

All parts of 'layer above' which are alpha in 'layer below' will be made
also alpha in 'layer above'
(to whatever degree of alpha they were)

Destination which overlaps the source, replaces the source.

Fa = 0; Fb = αs
co = αb x Cb x αs
αo = αb x αs

## destout

[[find in source code]](../../../blendmodes/blend.py#L298)

```python
def destout(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
):
```

Reverse 'Clip' composite mode.

All parts of 'layer below' which are alpha in 'layer above' will be made
also alpha in 'layer below'
(to whatever degree of alpha they were)

## difference

[[find in source code]](../../../blendmodes/blend.py#L85)

```python
def difference(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.DIFFERENCE.

## divide

[[find in source code]](../../../blendmodes/blend.py#L144)

```python
def divide(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.DIVIDE.

## exclusion

[[find in source code]](../../../blendmodes/blend.py#L163)

```python
def exclusion(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.EXCLUSION.

## glow

[[find in source code]](../../../blendmodes/blend.py#L68)

```python
def glow(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.GLOW.

## grainextract

[[find in source code]](../../../blendmodes/blend.py#L134)

```python
def grainextract(
    background: np.ndarray,
    foreground: np.ndarray,
) -> np.ndarray:
```

BlendType.GRAINEXTRACT.

## grainmerge

[[find in source code]](../../../blendmodes/blend.py#L139)

```python
def grainmerge(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.GRAINMERGE.

## hardlight

[[find in source code]](../../../blendmodes/blend.py#L125)

```python
def hardlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.HARDLIGHT.

## hue

[[find in source code]](../../../blendmodes/blend.py#L250)

```python
def hue(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.HUE.

## imageFloatToInt

[[find in source code]](../../../blendmodes/blend.py#L372)

```python
def imageFloatToInt(image: np.ndarray) -> np.ndarray:
```

Convert a numpy array representing an image to an array of ints.

#### Arguments

- `image` *np.ndarray* - numpy array of floats

#### Returns

- `np.ndarray` - numpy array of ints

## imageIntToFloat

[[find in source code]](../../../blendmodes/blend.py#L360)

```python
def imageIntToFloat(image: np.ndarray) -> np.ndarray:
```

Convert a numpy array representing an image to an array of floats.

#### Arguments

- `image` *np.ndarray* - numpy array of ints

#### Returns

- `np.ndarray` - numpy array of floats

## lighten

[[find in source code]](../../../blendmodes/blend.py#L95)

```python
def lighten(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.LIGHTEN.

## luminosity

[[find in source code]](../../../blendmodes/blend.py#L265)

```python
def luminosity(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.LUMINOSITY.

## multiply

[[find in source code]](../../../blendmodes/blend.py#L36)

```python
def multiply(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.MULTIPLY.

## negation

[[find in source code]](../../../blendmodes/blend.py#L90)

```python
def negation(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.NEGATION.

## normal

[[find in source code]](../../../blendmodes/blend.py#L30)

```python
def normal(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.NORMAL.

## overlay

[[find in source code]](../../../blendmodes/blend.py#L76)

```python
def overlay(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.OVERLAY.

## pinlight

[[find in source code]](../../../blendmodes/blend.py#L149)

```python
def pinlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.PINLIGHT.

## reflect

[[find in source code]](../../../blendmodes/blend.py#L60)

```python
def reflect(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.REFLECT.

## saturation

[[find in source code]](../../../blendmodes/blend.py#L255)

```python
def saturation(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.SATURATION.

## screen

[[find in source code]](../../../blendmodes/blend.py#L105)

```python
def screen(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.SCREEN.

## softlight

[[find in source code]](../../../blendmodes/blend.py#L118)

```python
def softlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.SOFTLIGHT.

## srcatop

[[find in source code]](../../../blendmodes/blend.py#L342)

```python
def srcatop(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
):
```

Place the layer below above the 'layer above' in places where the 'layer above' exists.

## vividlight

[[find in source code]](../../../blendmodes/blend.py#L156)

```python
def vividlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.VIVIDLIGHT.

## xor

[[find in source code]](../../../blendmodes/blend.py#L110)

```python
def xor(background: np.ndarray, foreground: np.ndarray) -> np.ndarray:
```

BlendType.XOR.
