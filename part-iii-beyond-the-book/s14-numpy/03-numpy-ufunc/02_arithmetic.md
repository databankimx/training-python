## Arithmetic `ufunc` Functions

NumPy exposes `ufunc` functions for all of the standard arithmetic 
operations. The implementation of `ndarray` also implements overrides for
the arithmetic operations `__add__` and `__sub__`, e.g., so these 
functions can be accessed using the arithmetic operators as well.

There are two main differences between the NumPy implementations and the
standard Python implementations of these functions:

1. The NumPy `ufunc` functions operate on each index in the array
2. For the NumPy functions, all array arguments must share the same shape
   and data type.

We'll review an example of each arithmetic `ufunc` operation.

---

### Addition

For addition, NumPy provides the `np.add()` function we looked at in the
introduction.

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

print("Addition:")
print(f"arr_x:                {arr_x}")
print(f"arr_y:                {arr_y}")
print(f"np.add(arr_x, arr_y): {np.add(arr_x, arr_y)}")
print(f"arr_x + arr_y:        {arr_x + arr_y}")
```

Output:

```
Addition:
arr_x:                [10 20 30 40 50 60]
arr_y:                [4 5 6 7 8 9]
np.add(arr_x, arr_y): [14 25 36 47 58 69]
arr_x + arr_y:        [14 25 36 47 58 69]
```

---

### Subtraction

For subtraction, NumPy provides the `np.subtract()` function

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

print("Subtraction:")
print(f"arr_x:                     {arr_x}")
print(f"arr_y:                     {arr_y}")
print(f"np.subtract(arr_x, arr_y): {np.subtract(arr_x, arr_y)}")
print(f"arr_x - arr_y:             {arr_x - arr_y}")
```

Output:

```
Subtraction:
arr_x:                     [10 20 30 40 50 60]
arr_y:                     [4 5 6 7 8 9]
np.subtract(arr_x, arr_y): [ 6 15 24 33 42 51]
arr_x - arr_y:             [ 6 15 24 33 42 51]
```

---

### Multiplication

For multiplication, NumPy provides the `np.multiply()` function

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

print("Multiplication:")
print(f"arr_x:                     {arr_x}")
print(f"arr_y:                     {arr_y}")
print(f"np.multiply(arr_x, arr_y): {np.multiply(arr_x, arr_y)}")
print(f"arr_x * arr_y:             {arr_x * arr_y}")
```

Output:

```
Multiplication:
arr_x:                     [10 20 30 40 50 60]
arr_y:                     [4 5 6 7 8 9]
np.multiply(arr_x, arr_y): [ 40 100 180 280 400 540]
arr_x * arr_y:             [ 40 100 180 280 400 540]
```

---

### Division

For division, NumPy provides the `np.divide()` function.

For consistent printout, note the addition of the `np.set_printoptions()`
call using `"{:.2f}".format` to print all floats with two decimal places.

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

flt_fmt = "{:.2f}".format
np.set_printoptions(formatter={"float_kind": flt_fmt})

print("Division:")
print(f"arr_x:                   {arr_x}")
print(f"arr_y:                   {arr_y}")
print(f"np.divide(arr_x, arr_y): {np.divide(arr_x, arr_y)}")
print(f"arr_x / arr_y:           {arr_x / arr_y}")
```

Output:

```
Division:
arr_x:                   [10 20 30 40 50 60]
arr_y:                   [4 5 6 7 8 9]
np.divide(arr_x, arr_y): [2.50 4.00 5.00 5.71 6.25 6.67]
arr_x / arr_y:           [2.50 4.00 5.00 5.71 6.25 6.67]
```

---

### Integer Division

For integer division, NumPy provides the `np.floor_divide()` function.

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

print("Integer Division:")
print(f"arr_x:                         {arr_x}")
print(f"arr_y:                         {arr_y}")
print(f"np.floor_divide(arr_x, arr_y): {np.floor_divide(arr_x, arr_y)}")
print(f"arr_x // arr_y:                {arr_x // arr_y}")
```

Output:

```
Integer Division:
arr_x:                         [10 20 30 40 50 60]
arr_y:                         [4 5 6 7 8 9]
np.floor_divide(arr_x, arr_y): [2 4 5 5 6 6]
arr_x // arr_y:                [2 4 5 5 6 6]
```

---

### Remainder/Modulo

For remainder/modulo, NumPy provides two functions: `np.mod()` and 
`np.remainder()`

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

print("Remainder:")
print(f"arr_x:                      {arr_x}")
print(f"arr_y:                      {arr_y}")
print(f"np.mod(arr_x, arr_y):       {np.mod(arr_x, arr_y)}")
print(f"np.remainder(arr_x, arr_y): {np.remainder(arr_x, arr_y)}")
print(f"arr_x % arr_y:              {arr_x % arr_y}")
```

Output:

```
Remainder:
arr_x:                      [10 20 30 40 50 60]
arr_y:                      [4 5 6 7 8 9]
np.mod(arr_x, arr_y):       [2 0 0 5 2 6]
np.remainder(arr_x, arr_y): [2 0 0 5 2 6]
arr_x % arr_y:              [2 0 0 5 2 6]
```

---

### Integer Division and Remainder

For integer division and remainder calculation, NumPy provides the 
`np.divmod()` function.

```python
import numpy as np

arr_x = np.array([10, 20, 30, 40, 50, 60])
arr_y = np.array([4, 5, 6, 7, 8, 9])

print("Integer Division and Remainder:")
print(f"arr_x:                         {arr_x}")
print(f"arr_y:                         {arr_y}")
print("np.divmod(arr_x, arr_y):", end=" ")
for arr in np.divmod(arr_x, arr_y):
    print(arr, end=" ")
print()
```

Output:

```
Integer Division and Remainder:
arr_x:                  [10 20 30 40 50 60]
arr_y:                  [4 5 6 7 8 9]
np.divmod(arr_x, arr_y): [2 4 5 5 6 6] [2 0 0 5 2 6]
```

---

### Absolute Values

For absolute value calculation, NumPy provides the `np.abs()` and 
`np.absolute()` functions.

```python
import numpy as np

arr = np.array([-3, -2, -1, 0, 1, 2, 3])

print("Absolute Values:")
print(f"arr:              {arr}")
print(f"np.abs(arr):      {np.abs(arr)}")
print(f"np.absolute(arr): {np.absolute(arr)}")
```

Output:

```
Absolute Values:
arr:              [-3 -2 -1  0  1  2  3]
np.abs(arr):      [3 2 1 0 1 2 3]
np.absolute(arr): [3 2 1 0 1 2 3]
```

---
