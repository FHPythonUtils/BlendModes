# Blend

[Blendmodes Index](../README.md#blendmodes-index) / [Blendmodes](./index.md#blendmodes) / Blend

> Auto-generated documentation for [blendmodes.blend](../../../blendmodes/blend.py) module.

- [Blend](#blend)
  - [_lum](#_lum)
  - [_sat](#_sat)
  - [_setLum](#_setlum)
  - [_setSat](#_setsat)
  - [additive](#additive)
  - [alpha_comp_shell](#alpha_comp_shell)
  - [blend](#blend)
  - [blendLayers](#blendlayers)
  - [blendLayersArray](#blendlayersarray)
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

## _lum

[Show source in blend.py:170](../../../blendmodes/blend.py#L170)

Luminosity.

#### Arguments

- `colours` - x by x by 3 matrix of rgb color components of pixels

#### Returns

x by x by 3 matrix of luminosity of pixels

#### Signature

```python
def _lum(colours: np.ndarray) -> np.ndarray: ...
```



## _sat

[Show source in blend.py:210](../../../blendmodes/blend.py#L210)

Saturation.

#### Arguments

- `colours` - x by x by 3 matrix of rgb color components of pixels

#### Returns

int of saturation of pixels

#### Signature

```python
def _sat(colours: np.ndarray) -> np.ndarray: ...
```



## _setLum

[Show source in blend.py:179](../../../blendmodes/blend.py#L179)

Set a new luminosity value for the matrix of color.

#### Signature

```python
def _setLum(originalColours: np.ndarray, newLuminosity: np.ndarray) -> np.ndarray: ...
```



## _setSat

[Show source in blend.py:219](../../../blendmodes/blend.py#L219)

Set a new saturation value for the matrix of color.

#### Signature

```python
def _setSat(originalColours: np.ndarray, newSaturation: np.ndarray) -> np.ndarray: ...
```



## additive

[Show source in blend.py:43](../../../blendmodes/blend.py#L43)

BlendType.ADDITIVE.

#### Signature

```python
def additive(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## alpha_comp_shell

[Show source in blend.py:623](../../../blendmodes/blend.py#L623)

Implement common transformations occurring in any blend or composite mode.

#### Signature

```python
def alpha_comp_shell(
    lower_alpha: np.ndarray,
    upper_alpha: np.ndarray,
    lower_rgb: np.ndarray,
    upper_rgb: np.ndarray,
    blendType: BlendType,
) -> tuple[np.ndarray, np.ndarray]: ...
```

#### See also

- [BlendType](./blendtype.md#blendtype)



## blend

[Show source in blend.py:402](../../../blendmodes/blend.py#L402)

Blend pixels.

#### Arguments

----
 - `background` *np.ndarray* - background
 - `foreground` *np.ndarray* - foreground
 - `blendType` *BlendType* - the blend type

#### Returns

-------
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

#### Signature

```python
def blend(
    background: np.ndarray, foreground: np.ndarray, blendType: BlendType
) -> np.ndarray: ...
```

#### See also

- [BlendType](./blendtype.md#blendtype)



## blendLayers

[Show source in blend.py:469](../../../blendmodes/blend.py#L469)

Blend two layers (background and foreground), where the background may
be cropped if smaller than the foreground.

:param Image.Image background: The background layer.
:param Image.Image foreground: The foreground layer (must be the
same size as the background).

#### Arguments

- `blendType` *BlendType* - The blend type to be applied.
- `opacity` *float* - The opacity of the foreground image. Defaults to 1.0. (optional)
:param tuple[int, int] offsets: Offsets for the foreground layer. Defaults to (0, 0). (optional)

#### Returns

Type: *Image.Image*
The combined image.

Examples
--------
Blend two layers with default parameters

```python
>>> combined_image = blendLayers(background_image, foreground_image, BlendType.NORMAL)
```

Blend two layers with custom opacity and offsets

```python
>>> combined_image = blendLayers(
...	background_image,
...	foreground_image,
...	BlendType.MULTIPLY,
...	opacity=0.7,
...	offsets=(100, 50)
...)
```

#### Signature

```python
def blendLayers(
    background: Image.Image,
    foreground: Image.Image,
    blendType: BlendType,
    opacity: float = 1.0,
    offsets: tuple[int, int] = (0, 0),
) -> Image.Image: ...
```

#### See also

- [BlendType](./blendtype.md#blendtype)



## blendLayersArray

[Show source in blend.py:513](../../../blendmodes/blend.py#L513)

Blend two layers (background and foreground), where the background may
be cropped if smaller than the foreground.

:param np.ndarray | Image.Image background: The background layer.
:param np.ndarray | Image.Image foreground: The foreground layer (must be the
same size as the background).

#### Arguments

- `blendType` *BlendType* - The blend type to be applied.
- `opacity` *float* - The opacity of the foreground image. Defaults to 1.0. (optional)
:param tuple[int, int] offsets: Offsets for the foreground layer. Defaults to (0, 0). (optional)

#### Returns

Type: *np.ndarray*
The combined image.

Examples
--------
Blend two layers with default parameters

```python
>>> combined_image = blendLayers(background_image, foreground_image, BlendType.NORMAL)
```

Blend two layers with custom opacity and offsets

```python
>>> combined_image = blendLayers(
...	background_image,
...	foreground_image,
...	BlendType.MULTIPLY,
...	opacity=0.7,
...	offsets=(100, 50)
...)
```

#### Signature

```python
def blendLayersArray(
    background: np.ndarray | Image.Image,
    foreground: np.ndarray | Image.Image,
    blendType: BlendType,
    opacity: float = 1.0,
    offsets: tuple[int, int] = (0, 0),
) -> np.ndarray: ...
```

#### See also

- [BlendType](./blendtype.md#blendtype)



## colour

[Show source in blend.py:269](../../../blendmodes/blend.py#L269)

BlendType.COLOUR.

#### Signature

```python
def colour(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## colourburn

[Show source in blend.py:48](../../../blendmodes/blend.py#L48)

BlendType.COLOURBURN.

#### Signature

```python
def colourburn(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## colourdodge

[Show source in blend.py:56](../../../blendmodes/blend.py#L56)

BlendType.COLOURDODGE.

#### Signature

```python
def colourdodge(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## darken

[Show source in blend.py:102](../../../blendmodes/blend.py#L102)

BlendType.DARKEN.

#### Signature

```python
def darken(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## destatop

[Show source in blend.py:330](../../../blendmodes/blend.py#L330)

Place the layer below above the 'layer above' in places where the 'layer above' exists...

where 'layer below' does not exist, but 'layer above' does, place 'layer-above'

#### Signature

```python
def destatop(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]: ...
```



## destin

[Show source in blend.py:279](../../../blendmodes/blend.py#L279)

'clip' composite mode.

All parts of 'layer above' which are alpha in 'layer below' will be made
also alpha in 'layer above'
(to whatever degree of alpha they were)

Destination which overlaps the source, replaces the source.

Fa = 0; Fb = as
co = ab x Cb x as
ao = ab x as

#### Signature

```python
def destin(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]: ...
```



## destout

[Show source in blend.py:307](../../../blendmodes/blend.py#L307)

Reverse 'Clip' composite mode.

All parts of 'layer below' which are alpha in 'layer above' will be made
also alpha in 'layer below'
(to whatever degree of alpha they were)

#### Signature

```python
def destout(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]: ...
```



## difference

[Show source in blend.py:87](../../../blendmodes/blend.py#L87)

BlendType.DIFFERENCE.

#### Signature

```python
def difference(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## divide

[Show source in blend.py:146](../../../blendmodes/blend.py#L146)

BlendType.DIVIDE.

#### Signature

```python
def divide(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## exclusion

[Show source in blend.py:165](../../../blendmodes/blend.py#L165)

BlendType.EXCLUSION.

#### Signature

```python
def exclusion(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## glow

[Show source in blend.py:70](../../../blendmodes/blend.py#L70)

BlendType.GLOW.

#### Signature

```python
def glow(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## grainextract

[Show source in blend.py:136](../../../blendmodes/blend.py#L136)

BlendType.GRAINEXTRACT.

#### Signature

```python
def grainextract(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## grainmerge

[Show source in blend.py:141](../../../blendmodes/blend.py#L141)

BlendType.GRAINMERGE.

#### Signature

```python
def grainmerge(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## hardlight

[Show source in blend.py:127](../../../blendmodes/blend.py#L127)

BlendType.HARDLIGHT.

#### Signature

```python
def hardlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## hue

[Show source in blend.py:259](../../../blendmodes/blend.py#L259)

BlendType.HUE.

#### Signature

```python
def hue(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## imageFloatToInt

[Show source in blend.py:384](../../../blendmodes/blend.py#L384)

Convert a numpy array representing an image to an array of ints.

#### Arguments

----
 - `image` *np.ndarray* - numpy array of floats

#### Returns

-------
 - `np.ndarray` - numpy array of ints

#### Signature

```python
def imageFloatToInt(image: np.ndarray) -> np.ndarray: ...
```



## imageIntToFloat

[Show source in blend.py:369](../../../blendmodes/blend.py#L369)

Convert a numpy array representing an image to an array of floats.

#### Arguments

----
 - `image` *np.ndarray* - numpy array of ints

#### Returns

-------
 - `np.ndarray` - numpy array of floats

#### Signature

```python
def imageIntToFloat(image: np.ndarray) -> np.ndarray: ...
```



## lighten

[Show source in blend.py:97](../../../blendmodes/blend.py#L97)

BlendType.LIGHTEN.

#### Signature

```python
def lighten(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## luminosity

[Show source in blend.py:274](../../../blendmodes/blend.py#L274)

BlendType.LUMINOSITY.

#### Signature

```python
def luminosity(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## multiply

[Show source in blend.py:38](../../../blendmodes/blend.py#L38)

BlendType.MULTIPLY.

#### Signature

```python
def multiply(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## negation

[Show source in blend.py:92](../../../blendmodes/blend.py#L92)

BlendType.NEGATION.

#### Signature

```python
def negation(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## normal

[Show source in blend.py:32](../../../blendmodes/blend.py#L32)

BlendType.NORMAL.

#### Signature

```python
def normal(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## overlay

[Show source in blend.py:78](../../../blendmodes/blend.py#L78)

BlendType.OVERLAY.

#### Signature

```python
def overlay(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## pinlight

[Show source in blend.py:151](../../../blendmodes/blend.py#L151)

BlendType.PINLIGHT.

#### Signature

```python
def pinlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## reflect

[Show source in blend.py:62](../../../blendmodes/blend.py#L62)

BlendType.REFLECT.

#### Signature

```python
def reflect(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## saturation

[Show source in blend.py:264](../../../blendmodes/blend.py#L264)

BlendType.SATURATION.

#### Signature

```python
def saturation(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## screen

[Show source in blend.py:107](../../../blendmodes/blend.py#L107)

BlendType.SCREEN.

#### Signature

```python
def screen(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## softlight

[Show source in blend.py:120](../../../blendmodes/blend.py#L120)

BlendType.SOFTLIGHT.

#### Signature

```python
def softlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## srcatop

[Show source in blend.py:351](../../../blendmodes/blend.py#L351)

Place the layer below above the 'layer above' in places where the 'layer above' exists.

#### Signature

```python
def srcatop(
    backgroundAlpha: np.ndarray,
    foregroundAlpha: np.ndarray,
    backgroundColour: np.ndarray,
    foregroundColour: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]: ...
```



## vividlight

[Show source in blend.py:158](../../../blendmodes/blend.py#L158)

BlendType.VIVIDLIGHT.

#### Signature

```python
def vividlight(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```



## xor

[Show source in blend.py:112](../../../blendmodes/blend.py#L112)

BlendType.XOR.

#### Signature

```python
def xor(background: np.ndarray, foreground: np.ndarray) -> np.ndarray: ...
```