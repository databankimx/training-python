## NumPy Universal Functions `ufunc`

NumPy exposes `ufuncs` (Universal Functions) that operate directly on the
`ndarray` object.

A ufunc can drastically improve performance when working with large arrays
and array-like objects by *vectorizing* iterative algorithms.

The *vectorization* process converts iterative processes (like `for` 
loops) into vector-based operations. Since modern CPUs are optimized for
vector operations, this not only reduces instruction complexity, but better
leverages hardware advances.

Additionally, `ufuncs` expose broadcasting and additional methods like 
`reduce`, `accumulate`, etc. that are very helpful for computation and 
can accept extra arguments such as:

* `where`: boolean array or condition defining how the operations should 
  take place
* `dtype`: defines the return type of elements
* `out`: defines the array where the return value is copied

---

### Where Do We Use `ufuncs`

They typically implement functionality that could be reproduced without
NumPy, for example:

Given two lists, if we want to create a third list containing the sums of
the elements at each index, we could...

---

#### Use the Traditional Python `zip` Function:

Without NumPy, we can accomplish the task iteratively, using a `for` loop
over the `list[tuple]` returned by `zip()`

```python
lx = [1, 2, 3, 4]
ly = [5, 6, 7, 8]
lz = []
for x, y in zip(lx, ly):
    lz.append(x + y)
print("Traditional Zip:")
print(f"List X: {lx}")
print(f"List Y: {ly}")
print(f"Result: {lz}\n")
```

Output:

```
Traditional Zip:
List X: [1, 2, 3, 4]
List Y: [5, 6, 7, 8]
Result: [6, 8, 10, 12]
```

That works fine, but we can simplify this and...

---

### Use the NumPy `add` Function:

With NumPy, we can abstract both the `zip` and the `for` loop into a 
vectorized operation using the `add()` ufunc.

```python
import numpy as np

lx = [1, 2, 3, 4]
ly = [5, 6, 7, 8]
az = np.add(lx, ly)
print("NumPy Add:")
print(f"List X: {lx}")
print(f"List Y: {ly}")
print(f"Result: {az}\n")
```

Output:

```
NumPy Add:
List X: [1, 2, 3, 4]
List Y: [5, 6, 7, 8]
Result: [ 6  8 10 12]
```

Or, we can even...

---

### Use the NumPy `add` Function on Arrays:

One thing that the traditional `zip()` process cannot do is perform the
same task using arrays as the source data instead of lists. The ufunc 
`add()` allows us to do that:

```python
import numpy as np

ax = np.ndarray([1, 2, 3, 4])
ay = np.ndarray([5, 6, 7, 8])
az = np.add(lx, ly)
print("NumPy Add Arrays:")
print(f"Array X: {lx}")
print(f"Array Y: {ly}")
print(f"Result: {az}\n")
```

Output:

```
NumPy Add Arrays:
Array X: [1 2 3 4]
Array Y: [5 6 7 8]
Result: [ 6  8 10 12]
```

---
