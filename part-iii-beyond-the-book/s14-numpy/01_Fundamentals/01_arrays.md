## Creating NumPy Arrays

The fundamental type in NumPy is is the `ndarray`. There are a number of
methods to create a NumPy array.

One fundamental difference between an `ndarray` and a `list` is that the
`ndarray` can only contain a single data type (or nested arrays of that
data type).

---

### Create from a List

The constructor can create a NumPy array from a list passed as its 
argument.

> Note the alias `np` used in the import
>
> This is a customary alias used by many programmers when using NumPy

```python
import numpy as np

lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print("List:", lst, type(lst))
print("Array:", arr, type(arr))
```

Output:

```
List: [1, 2, 3, 4, 5] <class 'list'>
Array: [1 2 3 4 5] <class 'numpy.ndarray'>
```

Note that unlike a `list`, the `__repr__` for `ndarray` does not separate
the numbers with commas. That might not make much sense now, but it will
when we start looking at multidimensional arrays and matrices.

---

### Create from a Tuple

Likewise, we can pass a tuple instead of a list.

```python
import numpy as np

tpl = (1, 2, 3, 4, 5)
arr = np.array(tpl)
print("Tuple:", tpl, type(tpl))
print("Array:", arr, type(arr))
```

Output:

```
Tuple: (1, 2, 3, 4, 5) <class 'tuple'>
Array: [1 2 3 4 5] <class 'numpy.ndarray'>
```

---
