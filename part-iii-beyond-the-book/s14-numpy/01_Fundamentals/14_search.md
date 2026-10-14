## Searching Arrays

NumPy includes special functions to search for values in an array.

---

### Traditional Linear Search

Of course, we could eschew any new functionality and locate a value
by looping over every element of the array:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 6, 5, 4, 4])
print(f"Array: {arr}")
indices = []
n = 4
print(f"Search Value: {n}")
indices = np.array([i for i in range(len(arr)) if arr[i] == n])
print(f"Found {n} at indices:", np.array(indices))
```

Output:

```
Array: [1 2 3 4 6 5 4 4]
Search Value: 4
Found 4 at indices: [3 6 7]
```

---

### Searching Using `where`

NumPy exposes a `where` function that accepts an array and a condition
and returns a tuple the set(s) of indices where the condition is met 
in the array.

#### `where` by Value

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 6, 5, 4, 4])
print(f"Array: {arr}")
n = 4
print(f"Search Value: {n}")
indices = np.where(arr == n)
print(f"Found {n} at indices:", indices)
```

Output:

```
Array: [1 2 3 4 6 5 4 4]
Search Value: 4
Found 4 at indices: (array([3, 6, 7]),)
```

---

#### `where` by Formula

Of course the condition doesn't have to be matching a specific value.
Any expression that resolves to a boolean can be used.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f"Array: {arr}")
odds = np.where(arr % 2 == 1)
evens = np.where(arr % 2 == 0)
print(f"Found Odd values at indices:", odds)
print(f"Found Even values at indices:", evens)
```

Output:

```
Array: [1 2 3 4 5 6 7 8]
Found Odd values at indices: (array([0, 2, 4, 6]),)
Found Even values at indices: (array([1, 3, 5, 7]),)
```

---

### Searching with `searchsorted()`

Provided an array is sorted, a binary search is much faster than a 
linear search. NumPy exposes the `searchsorted()` method to perform
a search using the binary search algorithm and return the index where
a value exists.

> Important Note!
>
> It is up to the programmer to verify that the list is sorted before
> using the `searchsorted()` function.
>
> For this, I use a function like this one
>
> ```python
> def is_sorted(arr: np.ndarray) -> bool:
>     """Check if an array is sorted in ascending order"""
>     return np.all(np.diff(arr) >= 0)
> ```

The `searchsorted()` function accepts an optional argument,
`side="left|right"` (default `"left"`) that does the following:

`searchsorted()` returns an index where the search value can be inserted without affecting the sorted state of the array.

* `side="left"` returns the lowest such index
* `side="right"` returns the highest such index

---

#### Using `searchsorted()` with One Value

Here we'll perform a search with a single value

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 7, 8])
print(f"Array: {arr}")
if not is_sorted(arr):
    arr = np.sort(arr)
n = 7
print(f"Search Value: {n}")
l = np.searchsorted(arr, n)
r = np.searchsorted(arr, n, side="right")
print(f"Can insert {n} from index {l} to {r}")
```

Output:

```
Array: [1 2 3 4 5 6 7 7 8]
Search Value: 7
Can insert 7 from index 6 to 8
```

Value 7 occurs at indices 6 and 7, so we can safely insert another 7
at 6, 7, or 8 without affecting order.

---

#### Using `searchsorted()` with Multiple Values

We can pass a list of values to `searchsorted()` and find the valid
indices for all of them.

```python
import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 4, 6])
print(f"Array: {arr}")
if not is_sorted(arr):
    arr = np.sort(arr)
vals = [2, 4, 5]
print(f"Search Values: {np.array(vals)}")
l = np.searchsorted(arr, vals)
r = np.searchsorted(arr, vals, side="right")
for i in range(len(vals)):
    if l[i] == r[i]:
        print(f"Can insert {vals[i]} at index {l[i]}")
        continue
    print(f"Can insert {vals[i]} from index {l[i]} to {r[i]}")
```

Output:

```
Array: [1 2 2 3 4 4 4 6]
Search Values: [2 4 5]
Can insert 2 from index 1 to 3
Can insert 4 from index 4 to 7
Can insert 5 at index 7
```

Note that even though 5 does not appear in the array, `searchsorted()`
returns an index where it can be inserted safely.

---
