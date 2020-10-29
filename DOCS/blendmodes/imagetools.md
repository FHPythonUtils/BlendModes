# imagetools

> Auto-generated documentation for [blendmodes.imagetools](../../blendmodes/imagetools.py) module.

Do stuff to images to prepare them

- [Blendmodes](../README.md#blendmodes-index) / [Modules](../README.md#blendmodes-modules) / [blendmodes](index.md#blendmodes) / imagetools
    - [rasterImageOA](#rasterimageoa)
    - [rasterImageOffset](#rasterimageoffset)

## rasterImageOA

[[find in source code]](../../blendmodes/imagetools.py#L7)

```python
def rasterImageOA(
    image: Image.Image,
    size: Tuple[(int, int)],
    alpha: float = 1.0,
    offsets: Tuple[(int, int)] = (0, 0),
) -> Image.Image:
```

Rasterise an image with offset and alpha to a given size

#### Arguments

- `image` *Image.Image* - pil image to draw
size (Tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
   offsets (Tuple[int, int], optional): x, y offsets as a tuple.
   Defaults to (0, 0).

#### Returns

- `Image.Image` - new image

## rasterImageOffset

[[find in source code]](../../blendmodes/imagetools.py#L24)

```python
def rasterImageOffset(
    image: Image.Image,
    size: Tuple[(int, int)],
    offsets: Tuple[(int, int)] = (0, 0),
):
```

Rasterise an image with offset to a given size

#### Arguments

- `image` *Image.Image* - pil image to draw
size (Tuple[int, int]): width, height as a tuple
   offsets (Tuple[int, int], optional): x, y offsets as a tuple.
   Defaults to (0, 0).

#### Returns

- `Image.Image` - new image
