## NumPy Set Operations

A set is like a list or array, except that it cannot contain duplicate
elements.

This is very like the definition of a set in mathematics. NumPy provides
functions to return only the set values from an array and to perform set
operations on arrays.

---

### Unique Values

The `unique()` function returns only one of each unique value in an array,
effectively making it behave like a set:

```python
import numpy as np

arr = np.array([1, 2, 3, 2, 1, 4, 5, 5, 6, 2, 3])
print(f"Original Array: {arr}")
print(f"Unique Values: {np.unique(arr)}")
```

Output:

```
Original Array: [1 2 3 2 1 4 5 5 6 2 3]
Unique Values: [1 2 3 4 5 6]
```

---

### Union

The union of two sets is a set containing each of the unique values in
both sets combined.

You can think of this being similar to the bitwise OR operation, only
operating memberwise instead of bitwise.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([3, 4, 5, 6])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Union: {np.union1d(arr_a, arr_b)}")
```

Output:

```
Array A: [1 2 3 4]
Array B: [3 4 5 6]
Union: [1 2 3 4 5 6]
```

---

### Intersection

The intersection of two sets is a set containing each of the unique values in common (appearing in both arrays).

You can think of this being similar to the bitwise AND operation, only
operating memberwise instead of bitwise.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([3, 4, 5, 6])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Intersection: {np.intersect1d(arr_a, arr_b)}")
```

Output:

```
Array A: [1 2 3 4]
Array B: [3 4 5 6]
Intersection: [3 4]
```

---

### Difference

The difference of two sets is a set containing each of the unique values in the first array but not in the second array.

You can think of this being similar to the bitwise XOR operation, only
operating memberwise instead of bitwise and ignoring unique members of the
second set.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([3, 4, 5, 6])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Difference: {np.setdiff1d(arr_a, arr_b)}")
```

Output:

```
Array A: [1 2 3 4]
Array B: [3 4 5 6]
Difference: [1 2]
```

---

### Symmetric Difference

The symmetric difference of two sets is a set containing each of the unique values either array that do not occur in the other.

You can think of this being similar to the bitwise XOR operation, only
operating memberwise instead of bitwise.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([3, 4, 5, 6])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Symmetric Difference: {np.setxor1d(arr_a, arr_b)}")
```

Output:

```
Array A: [1 2 3 4]
Array B: [3 4 5 6]
Symmetric Difference: [1 2 5 6]
```

---
