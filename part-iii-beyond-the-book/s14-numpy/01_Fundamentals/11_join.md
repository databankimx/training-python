## Joining Arrays

As you can imagine, merging (or joining) arrays can get complicated when
dealing with multiple dimensions.

NumPy implements a collection of functions for merging arrays with an
extensive set of options for how the arrays are joined.

---

### Joining Arrays with `concatenate()`

The `concatenate()` method joins two arrays based on the axis (dimension)
indicated.

With `concatenate()`, the resulting array is of the same dimensionality
as the input arrays.

---

#### Concatenating 1D Arrays

The simplest example is merging two one-dimensional arrays into one
one-dimensional array.

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}\nArray 2: {arr2}")
arr = np.concatenate((arr1, arr2))
print(f"\nJoined 1D Array: {arr}")
```

Output:

```
Array 1: [1 2 3]
Array 2: [4 5 6]

Joined 1D Array: [1 2 3 4 5 6]
```

---

#### Concatenating 2D Arrays

When we have two-dimensional arrays, we need to specify on which axis
we are joining them. If omitted, the default is `axis=0` (join along
columns).

##### Axis = 0

```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
arr = np.concatenate((arr1, arr2))
print(f"\nJoined 2D Array (by column):\n{arr}")
```

Output:

```
Array 1:
[[1 2]
 [3 4]]
Array 2:
[[5 6]
 [7 8]]

Joined 2D Array (by column):
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

. . . . . . . . . .

##### Axis = 1

```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
arr = np.concatenate((arr1, arr2), axis=1)
print(f"\nJoined 2D Array (by row):\n{arr}")
```

Output:

```
Array 1:
Array 1:
[[1 2]
 [3 4]]
Array 2:
[[5 6]
 [7 8]]

Joined 2D Array (by row):
[[1 2 5 6]
 [3 4 7 8]]
```
---

### Joining Arrays with `stack()`

Unlike `concatenate()`, the `stack()` method joins the input arrays as
separate elements in an additional dimension.

---

#### Stacking 1D Arrays

When we stack two one-dimensional arrays, the result is a single, 
two-dimensional array. The shape of the resulting array, however, is
dependent on which axis we set.

---

##### Axis = 0

With `axis=0` (the default), the two arrays will be unchanged and will
become elements 0 and 1 in the first dimension with the second dimension
being their existing contents.

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}\nArray 2: {arr2}")
arr = np.stack((arr1, arr2))
print(f"\nStacked 2D Array (by row):\n{arr}")
```

Output:

```
Array 1: [1 2 3]
Array 2: [4 5 6]

Stacked 2D Array (by row):
[[1 2 3]
 [4 5 6]]
```

. . . . . . . . . .

##### Axis = 1

With `axis=1`, the resulting arrays in the first dimension will contain 
the values from the two arrays grouped by index: `[arr1[0], arr2[0]]` and
so on.

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}\nArray 2: {arr2}")
arr = np.stack((arr1, arr2), axis=1)
print(f"\nStacked 2D Array (by row):\n{arr}")
```

Output:

```
Array 1: [1 2 3]
Array 2: [4 5 6]

Stacked 2D Array (by column):
[[1 4]
 [2 5]
 [3 6]]
```

---

### Horizontal Stacking with `hstack()`

Horizontal stacking using the `hstack()` function is identical to 
stacking along rows.

---

#### Horizontal Stacking 1d Arrays

Here is an example using `hstack()` with 1D arrays:

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}\nArray 2: {arr2}")
arr = np.hstack((arr1, arr2))
print(f"\nHorizontally Stacked 1D Array:\n{arr}")
```

Output:

```
Array 1: [1 2 3]
Array 2: [4 5 6]

Horizontally Stacked 1D Array:
[1 2 3 4 5 6]
```

---

#### Horizontal Stacking 2d Arrays

Here is an example using `hstack()` with 2D arrays:

```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
arr = np.hstack((arr1, arr2))
print(f"\nHorizontally Stacked 2D Array:\n{arr}")
```

Output:

```
Array 1:
[[1 2]
 [3 4]]
Array 2:
[[5 6]
 [7 8]]

Horizontally Stacked 2D Array:
[[1 2 5 6]
 [3 4 7 8]]
```

---

### Vertical Stacking with `vstack()`

Vertical stacking `vstack()` is shorthand for stacking by column:

---

#### Vertically Stacking 1D Arrays

Here is an example using `vstack()` with 1D arrays:

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}\nArray 2: {arr2}")
arr = np.vstack((arr1, arr2))
print(f"\nVertically Stacked 2D Array:\n{arr}")
```

Output:

```
Array 1: [1 2 3]
Array 2: [4 5 6]

Vertically Stacked 2D Array:
[[1 2 3]
 [4 5 6]]
```

---

#### Vertically Stacking 2D Arrays

Here is an example using `vstack()` with 2D arrays:

```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
arr = np.vstack((arr1, arr2))
print(f"\nVertically Stacked 2D Array:\n{arr}")
```

Output:

```
Array 1:
[[1 2]
 [3 4]]
Array 2:
[[5 6]
 [7 8]]

Vertically Stacked 2D Array:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

---

### Depth Stacking with `dstack()`

Depth stacking is based on the shape (number of elements) in the stacked
arrays.

---

#### Depth Stacking 1D Arrays

Here is an example of `dstack()` with 1D arrays:

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(f"Array 1: {arr1}\nArray 2: {arr2}")
arr = np.dstack((arr1, arr2))
print(f"\nDepth Stacked 3D Array:\n{arr}")
```

Output:

```
Array 1: [1 2 3]
Array 2: [4 5 6]

Depth Stacked 3D Array:
[[[1 4]
  [2 5]
  [3 6]]]
```

The resulting array is three-dimensional because the initial arrays
contain three elements each.

---

#### Depth Stacking 2D Arrays

Here is an example of `dstack()` with 2D arrays:

```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
arr = np.dstack((arr1, arr2))
print(f"\nDepth Stacked 3D Array:\n{arr}")
```

Output:

```
Array 1:
[[1 2]
 [3 4]]
Array 2:
[[5 6]
 [7 8]]
Depth Stacked 3D Array:
[[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]]
```

Here, the shape is interpreted twice, as each dimension has a shape of
two element, resulting in a 3D array of 2x2 matrices.

---
