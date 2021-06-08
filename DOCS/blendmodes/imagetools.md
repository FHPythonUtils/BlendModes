# imagetools

> Auto-generated documentation for [blendmodes.imagetools](../../blendmodes/imagetools.py) module.

Do stuff to images to prepare them.

- [Blendmodes](../README.md#blendmodes-index) / [Modules](../README.md#blendmodes-modules) / [blendmodes](index.md#blendmodes) / imagetools
    - [rasterImageOA](#rasterimageoa)
    - [rasterImageOffset](#rasterimageoffset)
    - [renderWAlphaOffset](#renderwalphaoffset)

## rasterImageOA

[[find in source code]](../../blendmodes/imagetools.py#L8)

```python
def rasterImageOA(
    image: Image.Image,
    size: tuple[(int, int)],
    alpha: float = 1.0,
    offsets: tuple[(int, int)] = (0, 0),
) -> Image.Image:
```

## rasterImageOffset

[[find in source code]](../../blendmodes/imagetools.py#L17)

```python
def rasterImageOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    offsets: tuple[(int, int)] = (0, 0),
) -> Image.Image:
```

## renderWAlphaOffset

[[find in source code]](../../blendmodes/imagetools.py#L26)

```python
def renderWAlphaOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    alpha: float = 1.0,
    offsets: tuple[(int, int)] = (0, 0),
) -> Image.Image:
```

Render an image with offset and alpha to a given size.

#### Arguments

- `image` *Image.Image* - pil image to draw
size (tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
offsets (tuple[int, int], optional): x, y offsets as a tuple.
Defaults to (0, 0).

#### Returns

- `Image.Image` - new image
