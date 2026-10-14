## Splitting Arrays

Splitting arrays is just the opposite of joining. We can take an array
and break it down into multiple arrays containing its component elements.

NumPy provides the `array_split()` method to perform these tasks:

---

### Splitting a 1D Array

When we split a 1D array, it will be split into multiple 1D arrays.

The syntax is:

```python
result = array_split(array, n)
```

Where `n` is the number of resulting arrays to split it into.

If we start with an array containing four elements, like this:

```python
arr = np.array([1, 2, 3, 4])
```

And we split it into two arrays

```python
result = np.array_split(arr, 2)
```

We can expect that in the end, we have a list containing two arrays, like
this:

```
result is [array([1, 2]), array([3, 4])]
```

---

#### Splitting 1D Array into Equal Parts

Here's a full example of splitting a 1D array into equal parts:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Original array:\n{arr}")
new_arr = np.array_split(arr, 3)
print(f"\nSplit array:\n{new_arr}")
```

Output:

```
Original array:
[1 2 3 4 5 6]

Split array:
[array([1, 2]), array([3, 4]), array([5, 6])]
```

---

#### Splitting 1D Array into Unequal Parts

When an array cannot be split into equal parts (for example, if we split
a six-element array into four arrays), the imbalances will be included
in the lowest index result arrays.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Original array:\n{arr}")
new_arr = np.array_split(arr, 4)
print(f"\nSplit array:\n{new_arr}")
```

Output:

```
Original array:
[1 2 3 4 5 6]

Split array:
[array([1, 2]), array([3, 4]), array([5]), array([6])]
```

---

#### Splitting 1D Array into More Parts than Total Elements

If we split an array into more parts than it contains elements, it will
create extra empty arrays (with the appropriate data type assigned).

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(f"Original array:\n{arr}")
new_arr = np.array_split(arr, 5)
print(f"\nSplit array:\n{new_arr}")
```

Output:

```
Original array:
[1 2 3 4]
Split array:
[array([1]), array([2]), array([3]), array([4]), array([], dtype=int64)]
```

---

### Splitting 2D Arrays

When we split two-dimensional arrays, just like joining, we need to 
specify the axis on which we will split (default: `axis=0`).

To get things to format nicely in the lesson output, I had to get a 
little sneaky in printing by creating this function:

```python
import numpy as np

def print_2d(arr: list[np.ndarray]) -> None:
    """Print out 2D split results"""
    print(f"\nSplit array:\n[")
    for ar in arr:
        print(f" array({','.join(str(ar).splitlines())})")
    print("]")
```

---

#### Splitting 2D Arrays by Column (`axis=0`)

Here is an example where we're splitting a 2D array by columns:

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(f"Original array:\n{arr}")
new_arr = np.array_split(arr, 3)
print_2d(new_arr)
```

Output:

```
Original array:
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]

Split array:
[
 array([[1 2], [3 4]])
 array([[5 6], [7 8]])
 array([[ 9 10], [11 12]])
]
```

---

#### Splitting 2D Arrays by Row (`axis=1`)

Here is an example where we're splitting a 2D array by rows:

```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print(f"Original array:\n{arr}")
new_arr = np.array_split(arr, 3, axis=1)
print_2d(new_arr)
```

Output:

```
Original array:
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]

Split array:
[
 array([[ 1], [ 3], [ 5], [ 7], [ 9], [11]])
 array([[ 2], [ 4], [ 6], [ 8], [10], [12]])
 array([])
]
```

---

### Horizontal Splitting with `hsplit()`

Just link with joins, we have a shorthand for splitting horizontally:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(f"Original array:\n{arr}")
new_arr = np.hsplit(arr, 3)
print_2d(new_arr)
```

Output:

```
Original array:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [13 14 15]
 [16 17 18]]

Split array:
[
 array([[ 1], [ 4], [ 7], [10], [13], [16]])
 array([[ 2], [ 5], [ 8], [11], [14], [17]])
 array([[ 3], [ 6], [ 9], [12], [15], [18]])
]
```

---

### Vertical Splitting with `vsplit()`

... and vertically:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(f"Original array:\n{arr}")
new_arr = np.vsplit(arr, 3)
print_2d(new_arr)
```

Output:

```
Original array:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [13 14 15]
 [16 17 18]]

Split array:
[
 array([[1 2 3], [4 5 6]])
 array([[ 7  8  9], [10 11 12]])
 array([[13 14 15], [16 17 18]])
]
```

---
