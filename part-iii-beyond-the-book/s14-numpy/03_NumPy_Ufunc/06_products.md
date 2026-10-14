## Computing Array Products

Like summation, product computation is different from multiplication.

When we multiply two arrays, the elements are multiplied member-wise, but
when we compute a product, we multiply all of the elements by each other
to reach a result.

So, if we had two arrays [1, 2, 3] and [4, 5, 6]:

* Multiplying results in [4, 10, 12]
* Product computation results in [6, 120] or 720 depending on the axis of 
  computation.

---

### Review: Multiplying Two Arrays

Recall that when we multiply arrays, we see member-wise multiplication.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
print("Multiplying:")
print(f"arr_a:                     {arr_a}")
print(f"arr_b:                     {arr_b}")
print(f"np.multiply(arr_a, arr_b): {np.multiply(arr_a, arr_b)}")
```

Output:

```
Multiplying:
arr_a:                     [1 2 3 4]
arr_b:                     [5 6 7 8]
np.multiply(arr_a, arr_b): [ 5 12 21 32]
```

---

### Computing the Product of an Array

Computing the product of a single array will always result in a scalar 
value equivalent to multiplying all the elements together.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print("Array Product:")
print(f"Array:                       {arr}")
print(f"np.prod(arr):                {np.prod(arr)}")
```

Output:

```
Array Product:
Array:                       [1 2 3 4]
np.prod(arr):                24
```

---

### Computing the Product of Two Arrays on the Y Axis

When we compute the product of two arrays on the Y Axis (`axis=0` - 
default), we receive the product of the products of the arrays.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
print("Product (y-Axis):")
print(f"arr_a:                       {arr_a}")
print(f"arr_b:                       {arr_b}")
print(f"np.prod([arr_a, arr_b]):     {np.prod([arr_a, arr_b])}")
```

Output:

```
Product (y-Axis):
arr_a:                       [1 2 3 4]
arr_b:                       [5 6 7 8]
np.prod([arr_a, arr_b]):     40320
```

---

### Computing the Product of Two Arrays on the X Axis

When we compute the product of two arrays on the X Axis (`axis=1`), we receive an array containing the products of the arrays.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
print("Product (x-Axis):")
print(f"arr_a:                       {arr_a}")
print(f"arr_b:                       {arr_b}")
print(f"np.prod([arr_a, arr_b]):     {np.prod([arr_a, arr_b])}")
```

Output:

```
Product (x-Axis):
arr_a:                       [1 2 3 4]
arr_b:                       [5 6 7 8]
np.prod([arr_a, arr_b]):     [  24 1680]
```

---

### Cumulative Products

When computing a cumulative product each element in the resulting array is 
the product of the array up to that element's index but ignoring higher 
indices.

If we perform a cumulative product on the array `[1, 2, 3, 4]`

We compute it like this:

|index|computation|result|
|:-:|-|-:|
|0|1|1|
|1|1 * 2|2|
|2|1 * 2 * 3|6|
|3|1 * 2 * 3 * 4|24|

Which results in `[1, 3, 6, 24]`

. . . . . . . . . .

NumPy provides the `cumprod()` function for cumulative products:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print("Cumulative product:")
print(f"Array:                       {arr}")
print(f"np.cumprod(arr):             {np.cumprod(arr)}\n")
```

Output:

```
Cumulative product:
Array:                       [1 2 3 4]
np.cumprod(arr):             [ 1  2  6 24]
```

---
