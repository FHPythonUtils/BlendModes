# blend

> Auto-generated documentation for [blendmodes.blend](../../blendmodes/blend.py) module.

Provide blending functions and types

- [Blendmodes](../README.md#blendmodes-index) / [Modules](../README.md#blendmodes-modules) / [blendmodes](index.md#blendmodes) / blend
    - [BlendType](#blendtype)
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

## BlendType

[[find in source code]](../../blendmodes/blend.py#L26)

```python
class BlendType(Enum):
```

Specify supported blend types

## additive

[[find in source code]](../../blendmodes/blend.py#L70)

```python
def additive(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.ADDITIVE

## blend

[[find in source code]](../../blendmodes/blend.py#L394)

```python
def blend(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
    blendType: BlendType,
) -> np.ndarray[np.float64]:
```

blend pixels

Args:
 background (np.ndarray[np.float64]): background
 foreground (np.ndarray[np.float64]): foreground
 blendType (BlendType): the blend type

Returns:
 np.ndarray[np.float64]: new array representing the image

 background: np.ndarray[np.float64],
foreground: np.ndarray[np.float64] and the return are in the form

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

#### See also

- [BlendType](#blendtype)

## blendLayers

[[find in source code]](../../blendmodes/blend.py#L445)

```python
def blendLayers(
    background: Image.Image,
    foreground: Image.Image,
    blendType: BlendType,
    opacity: float = 1.0,
) -> Image.Image:
```

Blend layers using numpy array

#### Arguments

- `background` *Image.Image* - background layer
- `foreground` *Image.Image* - foreground layer (must be same size as background)
- `blendType` *BlendType* - The blendtype
- `opacity` *float* - The opacity of the foreground image

#### Returns

- `Image.Image` - combined image

#### See also

- [BlendType](#blendtype)

## colour

[[find in source code]](../../blendmodes/blend.py#L277)

```python
def colour(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.COLOUR

## colourburn

[[find in source code]](../../blendmodes/blend.py#L75)

```python
def colourburn(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.COLOURBURN

## colourdodge

[[find in source code]](../../blendmodes/blend.py#L82)

```python
def colourdodge(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.COLOURDODGE

## darken

[[find in source code]](../../blendmodes/blend.py#L124)

```python
def darken(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.DARKEN

## destatop

[[find in source code]](../../blendmodes/blend.py#L330)

```python
def destatop(
    backgroundAlpha: np.ndarray[np.float64],
    foregroundAlpha: np.ndarray[np.float64],
    backgroundColour: np.ndarray[np.float64],
    foregroundColour: np.ndarray[np.float64],
):
```

place the layer below above the 'layer above' in places where the 'layer above' exists
where 'layer below' does not exist, but 'layer above' does, place 'layer-above'

#### Arguments

- `img_in`
- `img_layer`

## destin

[[find in source code]](../../blendmodes/blend.py#L288)

```python
def destin(
    backgroundAlpha: np.ndarray[np.float64],
    foregroundAlpha: np.ndarray[np.float64],
    backgroundColour: np.ndarray[np.float64],
    foregroundColour: np.ndarray[np.float64],
):
```

'Clip' composite mode
All parts of 'layer above' which are alpha in 'layer below' will be made
also alpha in 'layer above'
(to whatever degree of alpha they were)

Destination which overlaps the source, replaces the source.

Fa = 0; Fb = Î±s
co = Î±b x Cb x Î±s
Î±o = Î±b x Î±s

#### Arguments

- `source`
- `destination`

## destout

[[find in source code]](../../blendmodes/blend.py#L313)

```python
def destout(
    backgroundAlpha: np.ndarray[np.float64],
    foregroundAlpha: np.ndarray[np.float64],
    backgroundColour: np.ndarray[np.float64],
    foregroundColour: np.ndarray[np.float64],
):
```

reverse 'Clip' composite mode
All parts of 'layer below' which are alpha in 'layer above' will be made
also alpha in 'layer below'
(to whatever degree of alpha they were)

#### Arguments

- `img_in`
- `img_layer`

## difference

[[find in source code]](../../blendmodes/blend.py#L109)

```python
def difference(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.DIFFERENCE

## divide

[[find in source code]](../../blendmodes/blend.py#L166)

```python
def divide(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.DIVIDE

## exclusion

[[find in source code]](../../blendmodes/blend.py#L183)

```python
def exclusion(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.EXCLUSION

## glow

[[find in source code]](../../blendmodes/blend.py#L96)

```python
def glow(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.GLOW

## grainextract

[[find in source code]](../../blendmodes/blend.py#L156)

```python
def grainextract(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.GRAINEXTRACT

## grainmerge

[[find in source code]](../../blendmodes/blend.py#L161)

```python
def grainmerge(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.GRAINMERGE

## hardlight

[[find in source code]](../../blendmodes/blend.py#L149)

```python
def hardlight(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.HARDLIGHT

## hue

[[find in source code]](../../blendmodes/blend.py#L267)

```python
def hue(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.HUE

## imageFloatToInt

[[find in source code]](../../blendmodes/blend.py#L382)

```python
def imageFloatToInt(image: np.ndarray[np.float64]) -> np.ndarray[np.int64]:
```

Convert a numpy array representing an image to an array of ints

#### Arguments

- `image` *np.ndarray[np.float64]* - numpy array of floats

#### Returns

- `np.ndarray[np.int64]` - numpy array of ints

## imageIntToFloat

[[find in source code]](../../blendmodes/blend.py#L370)

```python
def imageIntToFloat(image: np.ndarray[np.int64]) -> np.ndarray[np.float64]:
```

Convert a numpy array representing an image to an array of floats

#### Arguments

- `image` *np.ndarray[np.int64]* - numpy array of ints

#### Returns

- `np.ndarray[np.float64]` - numpy array of floats

## lighten

[[find in source code]](../../blendmodes/blend.py#L119)

```python
def lighten(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.LIGHTEN

## luminosity

[[find in source code]](../../blendmodes/blend.py#L282)

```python
def luminosity(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.LUMINOSITY

## multiply

[[find in source code]](../../blendmodes/blend.py#L65)

```python
def multiply(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.MULTIPLY

## negation

[[find in source code]](../../blendmodes/blend.py#L114)

```python
def negation(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.NEGATION

## normal

[[find in source code]](../../blendmodes/blend.py#L60)

```python
def normal(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.NORMAL

## overlay

[[find in source code]](../../blendmodes/blend.py#L103)

```python
def overlay(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.OVERLAY

## pinlight

[[find in source code]](../../blendmodes/blend.py#L171)

```python
def pinlight(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.PINLIGHT

## reflect

[[find in source code]](../../blendmodes/blend.py#L89)

```python
def reflect(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.REFLECT

## saturation

[[find in source code]](../../blendmodes/blend.py#L272)

```python
def saturation(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.SATURATION

## screen

[[find in source code]](../../blendmodes/blend.py#L129)

```python
def screen(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.SCREEN

## softlight

[[find in source code]](../../blendmodes/blend.py#L143)

```python
def softlight(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.SOFTLIGHT

## srcatop

[[find in source code]](../../blendmodes/blend.py#L351)

```python
def srcatop(
    backgroundAlpha: np.ndarray[np.float64],
    foregroundAlpha: np.ndarray[np.float64],
    backgroundColour: np.ndarray[np.float64],
    foregroundColour: np.ndarray[np.float64],
):
```

place the layer below above the 'layer above' in places where the 'layer above' exists

#### Arguments

- `img_in`
- `img_layer`

## vividlight

[[find in source code]](../../blendmodes/blend.py#L177)

```python
def vividlight(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.VIVIDLIGHT

## xor

[[find in source code]](../../blendmodes/blend.py#L134)

```python
def xor(
    background: np.ndarray[np.float64],
    foreground: np.ndarray[np.float64],
) -> np.ndarray[np.float64]:
```

BlendType.XOR
