## Iterating over Arrays with `nditer()`

As we saw in the last lesson, iterating over NumPy arrays can quickly 
become awkward as the number of dimensions rises.

NumPy exposes a function `nditer()` to simplify array iteration.

We can see how much it helps us by reviewing some examples.

---

### Iterating over All Elements in a Three-Dimensional Array

Using Python `for` loops, we had to nest `n` loops (where `n` is the 
number of dimensions).

Here, using the `nditer()` function, all that nesting is taken care of
for us.

```python
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"Array:\n{arr}\n\nEach element:")
for n in np.nditer(arr):
    print(n)
```

Output:

```
Array:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]

Each element:
1
2
3
4
5
6
7
8
```

---

### Changing Element Data Types

The `nditer()` function accepts a keyword argument `op_dtypes`, which
allows the developer to specify a data type (using the NumPy 
abbreviations) into which each element will be converted during iteration.

For example, `op_dtypes="S"` specified that the elements should be 
converted to strings.

Conversions do not occur in-place (the array is not altered). Instead, the
converted values are stored in a dedicated memory buffer. In order to
enable this memory space, we add `flags=["buffered"]` to the call.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(f"Array:\n{arr}\n\nElements as strings:")
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["U"]):
    print("..." + x + "...")
```

Output:

```
Array:
[1 2 3]

Elements as strings:
...1...
...2...
...3...
```

Note how we were able to concatenate the values with strings after the
conversions.

---

### Different Step Sizes Per Dimension

The `nditer()` function allows us to specify slice-stepping per dimension
while iterating.

In this example, we'll include each item in the first dimension but only
evaluate every other item in the second dimension arrays.

```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"Array:\n{arr}\n\nDifferent step sizes:")
for n in np.nditer(arr[:, ::2]):
    print(n)
```

Output:

```
Array:
[[1 2 3 4]
 [5 6 7 8]]

Different step sizes:
1
3
5
7
```

---

### Enumerated Iteration

NumPy exposes another function `ndenumerate()` that performs an enumerated
iteration over the array.

Unlike normal enumeration, because there may be multi-dimensional indices,
the index values are returned as tuples.

#### Enumerating a 1D Array

Let's look at an example with a one-dimensional array.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(f"Array:\n{arr}\n\nEnumerated 1D Iteration:")
for idx, x in np.ndenumerate(arr):
    print(idx, x)
```

Output:

```
Array:
[1 2 3]

Enumerated 1D Iteration:
(0,) 1
(1,) 2
(2,) 3
```

---

#### Enumerating a 2D Array

We can see the usefulness of index tuples when we examine an example with 
a two-dimensional array.

```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"Array:\n{arr}\n\nEnumerated 2D Iteration:")
for idx, x in np.ndenumerate(arr):
    print(idx, x)
```

Output:

```
Array:
[[1 2 3 4]
 [5 6 7 8]]

Enumerated 2D Iteration:
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
```

---
