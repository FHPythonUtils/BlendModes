# Getting Started - Examples

Be sure to include the following for the functions below

```python
from blendmodes.blend import blendLayers, BlendType

background = Image.open(THISDIR + "/background.png")
foreground = Image.open(THISDIR + "/foreground.png")
```

## Normal

```python
blendLayers(background, foreground, BlendType.NORMAL)
```

![Normal](../../tests/data/normal_expected.png)

## Multiply

```python
blendLayers(background, foreground, BlendType.MULTIPLY)
```

![Multiply](../../tests/data/multiply_expected.png)

## Additive

```python
blendLayers(background, foreground, BlendType.ADDITIVE)
```

![Additive](../../tests/data/additive_expected.png)

## ColourBurn

```python
blendLayers(background, foreground, BlendType.COLOURBURN)
```

![ColourBurn](../../tests/data/colourburn_expected.png)

## ColourDodge

```python
blendLayers(background, foreground, BlendType.COLOURDODGE)
```

![ColourDodge](../../tests/data/colourdodge_expected.png)

## Reflect

```python
blendLayers(background, foreground, BlendType.REFLECT)
```

![Reflect](../../tests/data/reflect_expected.png)

## Glow

```python
blendLayers(background, foreground, BlendType.GLOW)
```

![Glow](../../tests/data/glow_expected.png)

## Overlay

```python
blendLayers(background, foreground, BlendType.OVERLAY)
```

![Overlay](../../tests/data/overlay_expected.png)

## Difference

```python
blendLayers(background, foreground, BlendType.DIFFERENCE)
```

![Difference](../../tests/data/difference_expected.png)

## Negation

```python
blendLayers(background, foreground, BlendType.NEGATION)
```

![Negation](../../tests/data/negation_expected.png)

## Lighten

```python
blendLayers(background, foreground, BlendType.LIGHTEN)
```

![Lighten](../../tests/data/lighten_expected.png)

## Darken

```python
blendLayers(background, foreground, BlendType.DARKEN)
```

![Darken](../../tests/data/darken_expected.png)

## Screen

```python
blendLayers(background, foreground, BlendType.SCREEN)
```

![Screen](../../tests/data/screen_expected.png)

## XOR

```python
blendLayers(background, foreground, BlendType.XOR)
```

![XOR](../../tests/data/xor_expected.png)

## SoftLight

```python
blendLayers(background, foreground, BlendType.SOFTLIGHT)
```

![SoftLight](../../tests/data/softlight_expected.png)

## HardLight

```python
blendLayers(background, foreground, BlendType.HARDLIGHT)
```

![HardLight](../../tests/data/hardlight_expected.png)

## GrainExtract

```python
blendLayers(background, foreground, BlendType.GRAINEXTRACT)
```

![GrainExtract](../../tests/data/grainextract_expected.png)

## GrainMerge

```python
blendLayers(background, foreground, BlendType.GRAINMERGE)
```

![GrainMerge](../../tests/data/grainmerge_expected.png)

## Divide

```python
blendLayers(background, foreground, BlendType.DIVIDE)
```

![Divide](../../tests/data/divide_expected.png)

## Hue

```python
blendLayers(background, foreground, BlendType.HUE)
```

![Hue](../../tests/data/hue_expected.png)

## Saturation

```python
blendLayers(background, foreground, BlendType.SATURATION)
```

![Saturation](../../tests/data/saturation_expected.png)

## Colour

```python
blendLayers(background, foreground, BlendType.COLOUR)
```

![Colour](../../tests/data/colour_expected.png)

## Luminosity

```python
blendLayers(background, foreground, BlendType.LUMINOSITY)
```

![Luminosity](../../tests/data/luminosity_expected.png)

## PinLight

```python
blendLayers(background, foreground, BlendType.PINLIGHT)
```

![PinLight](../../tests/data/pinlight_expected.png)

## VividLight

```python
blendLayers(background, foreground, BlendType.VIVIDLIGHT)
```

![VividLight](../../tests/data/vividlight_expected.png)

## Exclusion

```python
blendLayers(background, foreground, BlendType.EXCLUSION)
```

![Exclusion](../../tests/data/exclusion_expected.png)

## DestIn

```python
blendLayers(background, foreground, BlendType.DESTIN)
```

![Exclusion](../../tests/data/destin_expected.png)

## DestOut

```python
blendLayers(background, foreground, BlendType.DESTOUT)
```

![Exclusion](../../tests/data/destout_expected.png)

## DestAtop

```python
blendLayers(background, foreground, BlendType.DESTATOP)
```

![Exclusion](../../tests/data/destatop_expected.png)

## SrcAtop

```python
blendLayers(background, foreground, BlendType.SRCATOP)
```

![Exclusion](../../tests/data/srcatop_expected.png)
