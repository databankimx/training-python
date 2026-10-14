## Slicing Arrays

Much like lists, arrays can be sliced to return a discrete part of the
array.

---

### Slicing One-Dimensional Arrays

Slices on one-dimensional arrays are identical to list slices.

* We indicate a slice instead of an index like this: `[start:end]`
* We can also define the step, like this: `[start:end:step]`
* If we omit start it defaults to `0`
* If we omit end it defaults to `len(array)`
* If we omit step it defaults to `1`

#### Simple Slices

Here are some examples of simple slices

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print("1 to 5", arr[1:5])
print("4 to end", arr[4:])
print("start to 4", arr[:4])
```

Output:

```
[1 2 3 4 5 6 7]
1 to 5 [2 3 4 5]
4 to end [5 6 7]
start to 4 [1 2 3 4]
```

---

#### Negative-Index Slices

Of course, slices support negative indices

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print("-3 to -1", arr[-3:-1])
```

Output:

```
[1 2 3 4 5 6 7]
-3 to -1 [5 6]
```

---

#### Slice Copies

Here is an example of the "copy" shorthand using a slice"

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print("copy", arr[::])
```

Output:

```
[1 2 3 4 5 6 7]
copy [1 2 3 4 5 6 7]
```

---

#### Stepped Slices

As with lists, you can specify the step size in a slice.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print("1 to 5 - every other", arr[1:5:2])
print("copy - every other", arr[::2])
```

Output:

```
1 to 5 - every other [2 4]
copy - every other [1 3 5 7]
```

---

### Slicing Two-Dimensional Arrays

Slice indexing becomes a little more complicated with multiple
dimensions.

The syntax is: `[d1_index_or_slice, d2_index_or_slice, ...]`

So, for example:

```python
# This means give D2 items 1, 2, and 3 from D1 arrays 0 and 1
slc = arr[:2, 1:4]
```

That probably doesn't remove much of the mystery, so let's look at a few
examples:

```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print("indices 1 to 3 from first array", arr[1, 1:4])
print("index 2 from first two arrays", arr[0:2, 2])
print("indices 1 to 3 from first two arrays")
print(arr[0:2, 1:4])
```

Output:

```
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
indices 1 to 3 from first array [7 8 9]
index 2 from first two arrays [3 8]
indices 1 to 3 from first two arrays
[[2 3 4]
 [7 8 9]]
```

It's messy, but it makes sense once you use it for a while.

---
