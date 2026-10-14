## Indexing NumPy Arrays

Indices in NumPy arrays are mostly the same as indices in lists.

All indices start from 0, and when dealing with multiple dimensions,
we provide an index for each dimension in order from the 1st.

---

### Unidimensional Indices

In a one-dimensional array, indices are exactly the same as indices in 
Python lists.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print("1-D:")
print(arr, "\n")
print("arr[0] =", arr[0])
print("arr[1] =", arr[1])
print("arr[2] + arr[3] =", arr[2] + arr[3])
```

Output:

```
1-D:
[1 2 3 4]

arr[0] = 1
arr[1] = 2
arr[2] + arr[3] = 7
```

---

### Matrix Indices

For two-dimensional arrays, we can index the same way we do a
two-dimensional list giving two indexers, one for the first dimension and
a separate one for the second: `array[i_dim1][i_dim2]`

```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2-D:")
print(arr, "\n")

print("2nd element on 1st row: arr[0][1] =", arr[0][1])
print("5th element on 2nd row: arr[1][4] =", arr[1][4])
```

Output:

```
2-D:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]

2nd element on 1st row: arr[0][1] = 2
5th element on 2nd row: arr[1][4] = 10
```

---

#### NumPy-Style Indices

In NumPy, however, we're provided a simplified indexing form for
multidimensional arrays, where we can place comma-separated indices in a
single set of brackets :  
`array[i_dim1, i_dim2, ...]`

This indexing syntax is more readable, especially as we reach higher
dimensions.

```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2-D:")
print(arr, "\n")
    
print("2nd element on 1st row: arr[0, 1] =", arr[0, 1])
print("5th element on 2nd row: arr[1, 4] =", arr[1, 4])
```

Output:

```
2-D:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]

2nd element on 1st row: arr[0, 1] = 2
5th element on 2nd row: arr[1, 4] = 10
```

You can choose whichever indexing style you prefer, as both work 
identically with any NumPy array.

---

### Tensor Indices

Both styles of indexing are available at any depth of dimensions

```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D:")
print(arr, "\n")

print("arr[0][1][2] =", arr[0][1][2])
print("arr[0, 1, 2] =", arr[0, 1, 2])
```

Output:

```
3-D:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

arr[0][1][2] = 6
arr[0, 1, 2] = 6
```

---

### Omitting an Index

If you omit an index in a multidimensional array, the retrieved item will
be an array.

```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D:")
print(arr, "\n")

print("arr[1][1] =", arr[1][1])
print("arr[1, 1] =", arr[1, 1])
```

Output:

```
3-D:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

arr[1][1] = [10 11 12]
arr[1, 1] = [10 11 12]
```

---

### Negative Indices

NumPy indexing also supports negative indices.

```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D:")
print(arr, "\n")

print("arr[-1][-1] =", arr[-1][-1])
print("arr[-1, -1] =", arr[-1, -1])
```

Output:

```
3-D:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

arr[-1][-1] = [10 11 12]
arr[-1, -1] = [10 11 12]
```

---
