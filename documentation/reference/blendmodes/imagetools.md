# Imagetools

[Blendmodes Index](../README.md#blendmodes-index) / [Blendmodes](./index.md#blendmodes) / Imagetools

> Auto-generated documentation for [blendmodes.imagetools](../../../blendmodes/imagetools.py) module.

- [Imagetools](#imagetools)
  - [renderWAlphaOffset](#renderwalphaoffset)

## renderWAlphaOffset

[Show source in imagetools.py:8](../../../blendmodes/imagetools.py#L8)

Render an image with offset and alpha to a given size.

#### Arguments

----
 - `image` *Image.Image* - pil image to draw
 size (tuple[int, int]): width, height as a tuple
 - `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
 offsets (tuple[int, int], optional): x, y offsets as a tuple.
 Defaults to (0, 0).

#### Returns

-------
 - `Image.Image` - new image

#### Signature

```python
def renderWAlphaOffset(
    image: Image.Image,
    size: tuple[int, int],
    alpha: float = 1.0,
    offsets: tuple[int, int] = (0, 0),
) -> Image.Image: ...
```