## Dimensions in Arrays

In NumPy arrays, a *dimension* refers to a single level of depth in the
array.

If an array contains scalar values at every index, it is said to be 
one-dimensional.

Nested arrays (arrays where at least some values are arrays themselves)
are multidimensional.

Understanding the dimensional depth of an array is key to working with
NumPy.

The `ndarray` type (where we can now mention, the `nd` part stands for
n-dimensional) exposes a property `ndim` that contains the number of
dimensions in the array.

We'll review several different dimension types

---

### Scalar (Zero Dimensions)

In NumPy an `ndarray` can contain just a single value rather than a 
collection of them.

An array like this is called a *scalar* array or a 0-dimensional array.

Let's create one:

```python
import numpy as np

arr = np.array(42)
print(f"Scalar ({arr.ndim}-D):", type(arr).__name__, arr)
print(arr)
```

Output:

```
Scalar (0-D): ndarray
42
```

Notice how the calculated dimensions `arr.ndim` return `0`

---

### Unidimensional (One Dimension)

An array populated with a list or tuple of scalar values has one
dimension and is called a *unidimensional* array.

Here is an example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Unidimensional ({arr.ndim}-D):", type(arr).__name__)
print(arr)
```

Output:

```
Unidimensional (1-D): ndarray
[1 2 3 4 5]
```

As expected, NumPy tells us that this array has one dimension.

---

### Matrices (Two Dimensions)

Two-dimensional arrays (or *matrices* -- yes *matrixes* is also an
acceptable spelling) are arrays of arrays.

Here is where the NumPy `__repr__` choice of not displaying the separating
commas starts to make sense:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrix ({arr.ndim}-D):", type(arr).__name__)
print(arr)
```

Output:

```
Matrix (2-D): ndarray
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

---

### 3rd-Order Tensors (Three Dimensions)

At three (or more) dimensions, we refer to multidimensional arrays as
*tensors*. These can be a bit harder to wrap our minds around, but NumPy
helps by displaying them as meaningfully as possible.

I have snuck in an extra function for printing these out, but it's not
really germane to the topic at hand:

<details>
<summary>Ordinal Suffix Function</summary>

```python
def ordinal(n: int) -> str:
    """Get the ordinal suffix of a number"""
    if n // 10 % 10 != 1:
        # Logic
        if n % 10 == 1:
            return "st"
        if n % 10 == 2:
            return "nd"
        if n % 10 == 3:
            return "rd"
    return "th" 
```

</details>

```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
n = arr.ndim
print(f"{n}{ordinal(n)}-Order Tensor ({n}-D):", type(arr).__name__)
print(arr)
```

Output:

```
3rd-Order Tensor (3-D): ndarray
[[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
```

---

### Higher-Order Tensors (Four or More Dimensions)

Of course, it's possible to have higher-order tensors than three
dimensions.

Here's where it's useful to point out that we can specify the minimum
dimensionality of an array by adding the `ndmin` keyword argument to the
`array()` constructor call.

This way, if we initialize the array with fewer dimensions, NumPy will
force the array to have the specified minimum number of dimensions.

If you initialize the array with a greater number of dimensions,
`arr.ndim` will increase, as we're only setting a minimum.

```python
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)
n = arr.ndim
print(f"{n}{ordinal(n)}-Order Tensor ({n}-D):", type(arr).__name__)
print(arr)
```

Output:

```
5th-Order Tensor (5-D): ndarray
[[[[[1 2 3 4]]]]]
```

---
