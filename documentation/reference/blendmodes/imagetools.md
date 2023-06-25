# Imagetools

[Blendmodes Index](../README.md#blendmodes-index) /
[Blendmodes](./index.md#blendmodes) /
Imagetools

> Auto-generated documentation for [blendmodes.imagetools](../../../blendmodes/imagetools.py) module.

- [Imagetools](#imagetools)
  - [rasterImageOA](#rasterimageoa)
  - [rasterImageOffset](#rasterimageoffset)
  - [renderWAlphaOffset](#renderwalphaoffset)

## rasterImageOA

[Show source in imagetools.py:11](../../../blendmodes/imagetools.py#L11)

#### Signature

```python
@deprecated(deprecated_in="2021.1", removed_in="", details="use renderWAlphaOffset")
def rasterImageOA(
    image: Image.Image,
    size: tuple[int, int],
    alpha: float = 1.0,
    offsets: tuple[int, int] = (0, 0),
) -> Image.Image:
    ...
```



## rasterImageOffset

[Show source in imagetools.py:21](../../../blendmodes/imagetools.py#L21)

#### Signature

```python
@deprecated(deprecated_in="2021.1", removed_in="", details="use renderWAlphaOffset")
def rasterImageOffset(
    image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image:
    ...
```



## renderWAlphaOffset

[Show source in imagetools.py:31](../../../blendmodes/imagetools.py#L31)

Render an image with offset and alpha to a given size.

#### Arguments

- `image` *Image.Image* - pil image to draw
size (tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
offsets (tuple[int, int], optional): x, y offsets as a tuple.
Defaults to (0, 0).

#### Returns

- `Image.Image` - new image

#### Signature

```python
def renderWAlphaOffset(
    image: Image.Image,
    size: tuple[int, int],
    alpha: float = 1.0,
    offsets: tuple[int, int] = (0, 0),
) -> Image.Image:
    ...
```


