## Reshaping an Array

NumPy exposes a function `reshape()` that can change the shape of an 
array.

The `reshape()` function accepts arguments defining the number of elements
at each dimension.

---

### One to Two Dimensions

Here is an example where we will reshape a one-dimensional array into a
two-dimensional array.

We'll start with a one-dimensional array:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Original 1D array:\n{arr}\n")
```

Output:

```
Original 1D array:
[ 1  2  3  4  5  6  7  8  9 10 11 12]
```

This array has 12 elements total. When reshaping, keep in mind that the
shapes must be homogeneous at each dimension.

This means that if we have:

* f = number of first-dimension elements
* s = number of second-dimension elements (per array)

Then it must be the case that:

* f * s = 12

The possible two-d shapes then are:

* (1, 12) or (12, 1)
* (2, 6) or (6, 2)
* (3, 4) or (4, 3)

Choosing one, we can test reshaping:

```python
# -- SNIP --

new_arr = arr.reshape(4, 3)
print(f"Reshaped 2D array:\n{new_arr}")
print(f"Shape = {new_arr.shape}")
```

Output:

```
Original 1D array:
[ 1  2  3  4  5  6  7  8  9 10 11 12]

Reshaped 2D array:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
Shape = (4, 3)
```

---

### One to Three Dimensions

Of course, we're not limited to reshaping to a matrix. We can reshape to
any dimensional depth.

Here's an example reshaping to three dimensions:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Original 1D array:\n{arr}")
new_arr = arr.reshape(2, 3, 2)
print(f"Reshaped 3D array:\n{new_arr}")
print(f"Shape = {new_arr.shape}")
```

Output:

```
Original 1D array:
[ 1  2  3  4  5  6  7  8  9 10 11 12]

Reshaped 3D array:
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
Shape = (2, 3, 2)
```

---

### Unknown Dimension Shapes

If a dimension's shape is unknown, we can specify a value of `-1` for
that dimension.

Numpy will then calculate the shape of the remaining dimension.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Original 1D array:\n{arr}")
new_arr = arr.reshape(2, 2, -1)
print(f"Reshaped 3D array:\n{new_arr}")
print(f"Shape = {new_arr.shape}")
```

Output:

```
Original 1D array:
[ 1  2  3  4  5  6  7  8  9 10 11 12]

Reshaped 3D array:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
Shape = (2, 2, 3)
```

---

### Flattening Arrays

Of course, we can also reduce dimensions. When reducing to a single
dimension, we refer to this as *flattening*.

We can accomplish this by either:

* Calling `reshape()` with only one dimension value  
  or
* Calling `flatten()`

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(f"Original 2D array:\n{arr}\n")

new_arr = arr.reshape(-1)
print(f"Reshaped 1D array:\n{new_arr}")
print(f"Shape = {new_arr.shape}\n")

new_arr = arr.flatten()
print(f"Flattened 1D array:\n{new_arr}")
print(f"Shape = {new_arr.shape}\n")
```

Output:

```
Original 2D array:
[[1 2]
 [3 4]
 [5 6]]

Reshaped 1D array:
[1 2 3 4 5 6]
Shape = (6,)

Flattened 1D array:
[1 2 3 4 5 6]
Shape = (6,)
```

---
