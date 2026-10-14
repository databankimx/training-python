## Array Shape

The *shape* of a Numpy array contains the count of elements in each 
dimension.

The counts are returned as a tuple.

---

### Two Dimensional Array Shape

Let's look at a simple example of the shape of a 2D array:

```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("array:")
print(arr)
print("shape", arr.shape)
```

Output:

```
array:
[[1 2 3 4]
 [5 6 7 8]]
shape (2, 4)
```

We can see that in the first dimension, there are two elements, each of
which is an array.

In the second dimension, each array contains four elements.

---

### Shape Errors

You cannot create a NumPy array with a non-homogeneous shape. This means 
that at any dimension, all arrays must be of the same shape themselves.

Consider a scenario where we have two one-dimensional arrays:

```python
import numpy as np

arr_1 = np.array([1, 2, 3])
print(f"{arr_1} has shape {arr_1.shape}")
arr_2 = np.array([4, 5])
print(f"{arr_2} has shape {arr_2.shape}")
```

Output:

```
[1 2 3] has shape (3,)
[4 5] has shape (2,)
```

The shapes of the arrays are different, which is fine for separate arrays.

However, if we try to add them as elements in a 2D array, we receive a
ValueError.

```python
# -- SNIP --
arr = np.array([arr_1, arr_2])
```

Output:

```
Traceback (most recent call last):
  File "\07_shape.py", line 12, in shape_error
    arr = np.array([[1, 2, 3], [4, 5]])
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: setting an array element with a sequence.
The requested array has an inhomogeneous shape after 1 dimensions.
The detected shape was (2,) + inhomogeneous part.
```

Because both arrays would exist at the same dimension, Numpy rejects the
array due to their different shapes.

---

### Higher Dimension Shapes

Let's have a look at a couple of examples with higher dimensions:

#### 3D array:

```python
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D array:")
print(arr)
print("shape", arr.shape, "\n")
```

Output:

```
3D array:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
shape (2, 2, 2)
```

---

#### 5D array:

```python
arr = np.array([1, 2, 3, 4], ndmin=5)
print("5D array:")
print(arr)
print("shape", arr.shape, "\n")
```

Output:

```
5D array:
[[[[[1 2 3 4]]]]]
shape (1, 1, 1, 1, 4)
```

---
