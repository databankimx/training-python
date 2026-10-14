## Sorting Arrays

The NumPy `ndarray` exposes its own `sort()` method, which includes
some advanced features for sorting multidimensional arrays.

---

### Sorting 1D Arrays Numerically

Like regular Python sorting, NumPy supports sorting numerically:

```python
import numpy as np

arr = np.array([3, 1, 2, 5, 4])
print("Original array:", arr)
sorted_arr = np.sort(arr)
print("Sorted array:  ", sorted_arr)
```

Output:

```
Original array: [3 1 2 5 4]
Sorted array:   [1 2 3 4 5]
```

---

### Sorting 1D Arrays Alphabetically

Like regular Python sorting, NumPy supports sorting lexically:

```python
import numpy as np

arr = np.array(["banana", "cherry", "apple"])
print("Original array:", arr)
sorted_arr = np.sort(arr)
print("Sorted array:  ", sorted_arr)
```

Output:

```
Original array: ['banana' 'cherry' 'apple']
Sorted array:   ['apple' 'banana' 'cherry']
```

---

### Sorting 2D Arrays

When sorting a multidimensional array, the internal arrays are sorted,
not all the scalar values across all internal arrays:

```python
import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])
print("Original array:\n", arr, "\n")
sorted_arr = np.sort(arr)
print("Sorted array:\n", sorted_arr)
```

Output:

```
Original array:
 [[3 2 4]
 [5 0 1]]

Sorted array:
 [[2 3 4]
 [0 1 5]]
```

---
