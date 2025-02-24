# Getting Started - Examples

Below, you'll find practical examples to help you get started with blending/compositing
images with the `blendmodes` library. Whether you're experimenting with simple overlays
or crafting intricate compositions, these examples will guide you through the process.

To begin, let’s take a look at our two source images:

![Rainbow](../../tests/data/src/rainbow.png)
![Duck](../../tests/data/src/duck.png)

We'll use these images as our **background** and **foreground** in the examples below.

To blend two images together, use the `blendLayers` function with your chosen blend mode:

```python
from blendmodes.blend import blendLayers, BlendType

background = Image.open(THISDIR + "/rainbow.png")
foreground = Image.open(THISDIR + "/duck.png")
```

Blend modes define how the **foreground** interacts with the **background**. Let’s start with the most fundamental mode:

## Normal

The **Normal** blend mode places the foreground image on top of the background without
any additional blending effects.

```python
blendLayers(background, foreground, BlendType.NORMAL)
```

![Normal](../../tests/data/case1/normal_expected.png)


Further examples of different blend types using `rainbow.png` and `duck.png` are as below

Note: for other composition examples (without code snippets), check out the [extended blend mode examples](blend_examples.md).

## Multiply

```python
blendLayers(background, foreground, BlendType.MULTIPLY)
```

![Multiply](../../tests/data/case1/multiply_expected.png)

## Additive

```python
blendLayers(background, foreground, BlendType.ADDITIVE)
```

![Additive](../../tests/data/case1/additive_expected.png)

## ColourBurn

```python
blendLayers(background, foreground, BlendType.COLOURBURN)
```

![ColourBurn](../../tests/data/case1/colourburn_expected.png)

## ColourDodge

```python
blendLayers(background, foreground, BlendType.COLOURDODGE)
```

![ColourDodge](../../tests/data/case1/colourdodge_expected.png)

## Reflect

```python
blendLayers(background, foreground, BlendType.REFLECT)
```

![Reflect](../../tests/data/case1/reflect_expected.png)

## Glow

```python
blendLayers(background, foreground, BlendType.GLOW)
```

![Glow](../../tests/data/case1/glow_expected.png)

## Overlay

```python
blendLayers(background, foreground, BlendType.OVERLAY)
```

![Overlay](../../tests/data/case1/overlay_expected.png)

## Difference

```python
blendLayers(background, foreground, BlendType.DIFFERENCE)
```

![Difference](../../tests/data/case1/difference_expected.png)

## Negation

```python
blendLayers(background, foreground, BlendType.NEGATION)
```

![Negation](../../tests/data/case1/negation_expected.png)

## Lighten

```python
blendLayers(background, foreground, BlendType.LIGHTEN)
```

![Lighten](../../tests/data/case1/lighten_expected.png)

## Darken

```python
blendLayers(background, foreground, BlendType.DARKEN)
```

![Darken](../../tests/data/case1/darken_expected.png)

## Screen

```python
blendLayers(background, foreground, BlendType.SCREEN)
```

![Screen](../../tests/data/case1/screen_expected.png)

## XOR

```python
blendLayers(background, foreground, BlendType.XOR)
```

![XOR](../../tests/data/case1/xor_expected.png)

## SoftLight

```python
blendLayers(background, foreground, BlendType.SOFTLIGHT)
```

![SoftLight](../../tests/data/case1/softlight_expected.png)

## HardLight

```python
blendLayers(background, foreground, BlendType.HARDLIGHT)
```

![HardLight](../../tests/data/case1/hardlight_expected.png)

## GrainExtract

```python
blendLayers(background, foreground, BlendType.GRAINEXTRACT)
```

![GrainExtract](../../tests/data/case1/grainextract_expected.png)

## GrainMerge

```python
blendLayers(background, foreground, BlendType.GRAINMERGE)
```

![GrainMerge](../../tests/data/case1/grainmerge_expected.png)

## Divide

```python
blendLayers(background, foreground, BlendType.DIVIDE)
```

![Divide](../../tests/data/case1/divide_expected.png)

## Hue

```python
blendLayers(background, foreground, BlendType.HUE)
```

![Hue](../../tests/data/case1/hue_expected.png)

## Saturation

```python
blendLayers(background, foreground, BlendType.SATURATION)
```

![Saturation](../../tests/data/case1/saturation_expected.png)

## Colour

```python
blendLayers(background, foreground, BlendType.COLOUR)
```

![Colour](../../tests/data/case1/colour_expected.png)

## Luminosity

```python
blendLayers(background, foreground, BlendType.LUMINOSITY)
```

![Luminosity](../../tests/data/case1/luminosity_expected.png)

## PinLight

```python
blendLayers(background, foreground, BlendType.PINLIGHT)
```

![PinLight](../../tests/data/case1/pinlight_expected.png)

## VividLight

```python
blendLayers(background, foreground, BlendType.VIVIDLIGHT)
```

![VividLight](../../tests/data/case1/vividlight_expected.png)

## Exclusion

```python
blendLayers(background, foreground, BlendType.EXCLUSION)
```

![Exclusion](../../tests/data/case1/exclusion_expected.png)

## DestIn

```python
blendLayers(background, foreground, BlendType.DESTIN)
```

![Exclusion](../../tests/data/case1/destin_expected.png)

## DestOut

```python
blendLayers(background, foreground, BlendType.DESTOUT)
```

![Exclusion](../../tests/data/case1/destout_expected.png)

## DestAtop

```python
blendLayers(background, foreground, BlendType.DESTATOP)
```

![Exclusion](../../tests/data/case1/destatop_expected.png)

## SrcAtop

```python
blendLayers(background, foreground, BlendType.SRCATOP)
```

![Exclusion](../../tests/data/case1/srcatop_expected.png)
