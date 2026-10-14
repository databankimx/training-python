## Iterating over an Array with a `for` Loop

Iterating over an array means going through its elements one by one.

As we deal with multi-dimensional arrays in NumPy, we can do this using 
Python's basic `for` loop.

---

### Iterating over a One-Dimensional Array

This process is pretty straightforward with a one-dimensional array:

```python
import numpy as np

arr = np.array([1, 2, 3])
print(f"1D Array:\n{arr}\n\nLooping...")
for el in arr:
    print(el)
```

Output:

```
1D Array:
[1 2 3]

Looping...
1
2
3
```

---

### Iterating over a Two-Dimensional Array

However, when we get to a multidimensional array, this approach only
evaluates the first dimension.

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr}\n\nLooping...")
for el in arr:
    print(el)
```

Output:

```
2D Array:
[[1 2 3]
 [4 5 6]]

Looping...
[1 2 3]
[4 5 6]
```

---

### Iterating over All Elements in a Two-Dimensional Array

If we want to traverse a two-dimensional array element-by-element, we must
loop over the elements within each row in addition to looping the rows
themselves:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr}\n\nLooping rows...")
for row in arr:
    print(f" Looping elements in row...")
    for el in row:
        print(f"  {el}")
```

Output:

```
2D Array:
[[1 2 3]
 [4 5 6]]
Looping rows...
 Looping elements in row...
  1
  2
  3
 Looping elements in row...
  4
  5
  6
```

Nesting loops is typically not a best practice, but that wasn't too
difficult.

---

### Element-Wise Iteration at Higher Dimensions

Once you have more then two dimensions, these nested loops start to become cluttered and difficult to follow:

```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"3D Array:\n{arr}\n\nLooping pages...")
for page in arr:
    print(f" Looping rows in page...")
    for row in page:
        print(f"  Looping elements in row...")
        for el in row:
            print(f"   {el}")
```

Output:

```
3D Array:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

Looping pages...
 Looping rows in page...
  Looping elements in row...
   1
   2
   3
  Looping elements in row...
   4
   5
   6
 Looping rows in page...
  Looping elements in row...
   7
   8
   9
  Looping elements in row...
   10
   11
   12
```

There's got to be a better way!

---
