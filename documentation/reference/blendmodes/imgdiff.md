# Imgdiff

[Blendmodes Index](../README.md#blendmodes-index) / [Blendmodes](./index.md#blendmodes) / Imgdiff

> Auto-generated documentation for [blendmodes.imgdiff](../../../blendmodes/imgdiff.py) module.

- [Imgdiff](#imgdiff)
  - [image_diff](#image_diff)
  - [image_diff_array](#image_diff_array)
  - [is_equal](#is_equal)
  - [is_x_diff](#is_x_diff)

## image_diff

[Show source in imgdiff.py:103](../../../blendmodes/imgdiff.py#L103)

Compare two images and return the difference as a value between 0 and 1, or
if percentage: 0 and 100.

For example, a black and white image compared in 'RGB' mode would
return a value of 100, which would then be checked if its between
`cmp_diff - tolerance` and `cmp_diff + tolerance`

:param Image.Image img1in: image 1 to compare
:param Image.Image img2in: image 2 to compare

#### Arguments

- `compare_mode` *str* - how should the pillow images be compared? eg RGBA, RGB, L etc
param bool percentage: are we comparing in percentage mode vs 0-1 mode?

#### Returns

Type: *float*
value representing how different the images are

Example Use
-----------

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> res = image_diff(img1, img2, compare_mode="RGB")
>>> int(res)
33
```

```python
>>> img1 = Image.new("RGB", (100, 100), "white")
>>> img2 = Image.new("RGB", (100, 100), "black")
>>> image_diff(img1, img2, compare_mode="RGB")
100.0
```

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> res = image_diff(img1, img2, compare_mode="L")
>>> int(res)
18
```

#### Signature

```python
def image_diff(
    img1in: Image.Image,
    img2in: Image.Image,
    compare_mode: str = "RGBA",
    percentage: bool = True,
) -> float: ...
```



## image_diff_array

[Show source in imgdiff.py:147](../../../blendmodes/imgdiff.py#L147)

Compare two images and return difference between 0, and 1.
Supports both PIL Images and NumPy arrays.

Both images must be in the same mode/ shape

:param Image.Image | np.ndarray img1in: image 1 to compare
:param Image.Image | np.ndarray img2in: image 2 to compare

#### Returns

Type: *float*
value representing how different the images are. between 0, and 1

Example Use
-----------

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> res = image_diff(img1, img2)
>>> int(res)
25
```

```python
>>> img1 = Image.new("RGB", (100, 100), "white")
>>> img2 = Image.new("RGB", (100, 100), "black")
>>> image_diff(img1, img2)
75.0
```

#### Signature

```python
def image_diff_array(
    img1in: Image.Image | np.ndarray, img2in: Image.Image | np.ndarray
) -> float: ...
```



## is_equal

[Show source in imgdiff.py:56](../../../blendmodes/imgdiff.py#L56)

Compare two images and return True/False if the image is within `tolerance` of
`cmp_diff`.

For example, a black and white image compared in 'RGB' mode would
return a value of 100, which would then be checked if its between
`cmp_diff - tolerance` and `cmp_diff + tolerance`

:param Image.Image img1in: image 1 to compare
:param Image.Image img2in: image 2 to compare

#### Arguments

- `compare_mode` *str* - how should the pillow images be compared? eg RGBA, RGB, L etc
param float tolerance: what tolerance should we accept on any inequality?
param bool percentage: are we comparing in percentage mode vs 0-1 mode?

#### Returns

Type: *bool*
if the images are equal with a given tolerance

Example Use
-----------

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> is_equal(img1, img2, compare_mode="RGB", tolerance=1)
False
```

```python
>>> img1 = Image.new("RGB", (100, 100), "white")
>>> img2 = Image.new("RGB", (100, 100), "black")
>>> is_equal(img1, img2, compare_mode="RGB", tolerance=1)
False
```

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> is_equal(img1, img2, compare_mode="L", tolerance=1)
False
```

#### Signature

```python
def is_equal(
    img1in: Image.Image,
    img2in: Image.Image,
    compare_mode: str = "RGBA",
    tolerance: float = 0,
    percentage: bool = True,
): ...
```



## is_x_diff

[Show source in imgdiff.py:6](../../../blendmodes/imgdiff.py#L6)

Compare two images and return True/False if the image is within `tolerance` of
`cmp_diff`.

For example, a black and white image compared in 'RGB' mode would
return a value of 100, which would then be checked if its between
`cmp_diff - tolerance` and `cmp_diff + tolerance`

:param Image.Image img1in: image 1 to compare
:param Image.Image img2in: image 2 to compare

#### Arguments

- `compare_mode` *str* - how should the pillow images be compared? eg RGBA, RGB, L etc
- `cmp_diff` *float* - how 'unequal' should the images be? 0 for identical, 1 (or 100)
for completely different (eg black + white in L mode)
param float tolerance: what tolerance should we accept on the inequality?
param bool percentage: are we comparing in percentage mode vs 0-1 mode?

#### Returns

Type: *bool*
True/False if the images are within `tolerance` of
`cmp_diff`.

Example Use
-----------

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=33, tolerance=1)
True
```

```python
>>> img1 = Image.new("RGB", (100, 100), "white")
>>> img2 = Image.new("RGB", (100, 100), "black")
>>> is_x_diff(img1, img2, compare_mode="RGB", cmp_diff=100, tolerance=1)
True
```

```python
>>> img1 = Image.new("RGB", (100, 100), "red")
>>> img2 = Image.new("RGB", (100, 100), "blue")
>>> is_x_diff(img1, img2, compare_mode="L", cmp_diff=18, tolerance=1)
True
```

#### Signature

```python
def is_x_diff(
    img1in: Image.Image,
    img2in: Image.Image,
    compare_mode: str = "RGBA",
    cmp_diff: float = 0,
    tolerance: float = 0,
    percentage: bool = True,
) -> bool: ...
```