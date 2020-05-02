<a name=".blendmodes"></a>
## blendmodes

Use this module to apply a number of blending modes to a background and
foreground image

<a name=".blendmodes.blend"></a>
## blendmodes.blend

Provide blending functions and types

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

<a name=".blendmodes.blend.BlendType"></a>
### BlendType

```python
class BlendType(Enum)
```

Specify supported blend types

<a name=".blendmodes.blend.normal"></a>
#### normal

```python
normal(_background, foreground)
```

BlendType.NORMAL

<a name=".blendmodes.blend.multiply"></a>
#### multiply

```python
multiply(background, foreground)
```

BlendType.MULTIPLY

<a name=".blendmodes.blend.additive"></a>
#### additive

```python
additive(background, foreground)
```

BlendType.ADDITIVE

<a name=".blendmodes.blend.colourburn"></a>
#### colourburn

```python
colourburn(background, foreground)
```

BlendType.COLOURBURN

<a name=".blendmodes.blend.colourdodge"></a>
#### colourdodge

```python
colourdodge(background, foreground)
```

BlendType.COLOURDODGE

<a name=".blendmodes.blend.reflect"></a>
#### reflect

```python
reflect(background, foreground)
```

BlendType.REFLECT

<a name=".blendmodes.blend.glow"></a>
#### glow

```python
glow(background, foreground)
```

BlendType.GLOW

<a name=".blendmodes.blend.overlay"></a>
#### overlay

```python
overlay(background, foreground)
```

BlendType.OVERLAY

<a name=".blendmodes.blend.difference"></a>
#### difference

```python
difference(background, foreground)
```

BlendType.DIFFERENCE

<a name=".blendmodes.blend.negation"></a>
#### negation

```python
negation(background, foreground)
```

BlendType.NEGATION

<a name=".blendmodes.blend.lighten"></a>
#### lighten

```python
lighten(background, foreground)
```

BlendType.LIGHTEN

<a name=".blendmodes.blend.darken"></a>
#### darken

```python
darken(background, foreground)
```

BlendType.DARKEN

<a name=".blendmodes.blend.screen"></a>
#### screen

```python
screen(background, foreground)
```

BlendType.SCREEN

<a name=".blendmodes.blend.xor"></a>
#### xor

```python
xor(background, foreground)
```

BlendType.XOR

<a name=".blendmodes.blend.softlight"></a>
#### softlight

```python
softlight(background, foreground)
```

BlendType.SOFTLIGHT

<a name=".blendmodes.blend.hardlight"></a>
#### hardlight

```python
hardlight(background, foreground)
```

BlendType.HARDLIGHT

<a name=".blendmodes.blend.grainextract"></a>
#### grainextract

```python
grainextract(background, foreground)
```

BlendType.GRAINEXTRACT

<a name=".blendmodes.blend.grainmerge"></a>
#### grainmerge

```python
grainmerge(background, foreground)
```

BlendType.GRAINMERGE

<a name=".blendmodes.blend.divide"></a>
#### divide

```python
divide(background, foreground)
```

BlendType.DIVIDE

<a name=".blendmodes.blend.pinlight"></a>
#### pinlight

```python
pinlight(background, foreground)
```

BlendType.PINLIGHT

<a name=".blendmodes.blend.vividlight"></a>
#### vividlight

```python
vividlight(background, foreground)
```

BlendType.VIVIDLIGHT

<a name=".blendmodes.blend.exclusion"></a>
#### exclusion

```python
exclusion(background, foreground)
```

BlendType.EXCLUSION

<a name=".blendmodes.blend.hue"></a>
#### hue

```python
hue(background, foreground)
```

BlendType.HUE

<a name=".blendmodes.blend.saturation"></a>
#### saturation

```python
saturation(background, foreground)
```

BlendType.SATURATION

<a name=".blendmodes.blend.colour"></a>
#### colour

```python
colour(background, foreground)
```

BlendType.COLOUR

<a name=".blendmodes.blend.luminosity"></a>
#### luminosity

```python
luminosity(background, foreground)
```

BlendType.LUMINOSITY

<a name=".blendmodes.blend.destin"></a>
#### destin

```python
destin(backgroundAlpha, foregroundAlpha, backgroundColour, _foregroundColour)
```

'Clip' composite mode
All parts of 'layer above' which are alpha in 'layer below' will be made
also alpha in 'layer above'
(to whatever degree of alpha they were)

Destination which overlaps the source, replaces the source.

Fa = 0; Fb = αs
co = αb x Cb x αs
αo = αb x αs

**Arguments**:

- `source`: 
- `destination`: 

**Returns**:



<a name=".blendmodes.blend.destout"></a>
#### destout

```python
destout(backgroundAlpha, foregroundAlpha, backgroundColour, _foregroundColour)
```

reverse 'Clip' composite mode
All parts of 'layer below' which are alpha in 'layer above' will be made
also alpha in 'layer below'
(to whatever degree of alpha they were)

**Arguments**:

- `img_in`: 
- `img_layer`: 

**Returns**:



<a name=".blendmodes.blend.destatop"></a>
#### destatop

```python
destatop(backgroundAlpha, foregroundAlpha, backgroundColour, foregroundColour)
```

place the layer below above the 'layer above' in places where the 'layer above' exists
where 'layer below' does not exist, but 'layer above' does, place 'layer-above'

**Arguments**:

- `img_in`: 
- `img_layer`: 

**Returns**:



<a name=".blendmodes.blend.srcatop"></a>
#### srcatop

```python
srcatop(backgroundAlpha, foregroundAlpha, backgroundColour, foregroundColour)
```

place the layer below above the 'layer above' in places where the 'layer above' exists

**Arguments**:

- `img_in`: 
- `img_layer`: 

**Returns**:



<a name=".blendmodes.blend.blend"></a>
#### blend

```python
blend(background, foreground, blendType)
```

blend pixels

**Arguments**:

- `background` _np.array_ - background
- `foreground` _np.array_ - foreground
- `blendType` _BlendType_ - the blend type
  

**Returns**:

- `np.array` - new array representing the image
  
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

<a name=".blendmodes.blend.blendLayers"></a>
#### blendLayers

```python
blendLayers(background, foreground, blendType, opacity=1.0)
```

Blend layers using numpy array

**Arguments**:

- `background` _PIL.Image_ - background layer
- `foreground` _PIL.Image_ - foreground layer (must be same size as background)
- `blendType` _BlendType_ - The blendtype
- `opacity` _float_ - The opacity of the foreground image
  

**Returns**:

- `PIL.Image` - combined image

<a name=".blendmodes.imagetools"></a>
## blendmodes.imagetools

Do stuff to images to prepare them

<a name=".blendmodes.imagetools.rasterImageOA"></a>
#### rasterImageOA

```python
rasterImageOA(image, size, alpha=1.0, offsets=(0, 0))
```

Rasterise an image with offset and alpha to a given size

<a name=".blendmodes.imagetools.rasterImageOffset"></a>
#### rasterImageOffset

```python
rasterImageOffset(image, size, offsets=(0, 0))
```

Rasterise an image with offset to a given size

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

