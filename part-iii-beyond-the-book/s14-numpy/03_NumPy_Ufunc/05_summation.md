## Summation

A common misconception in computation is conflating addition with 
summation.

When we add arrays, the members are added at each index. When we perform
summation, however, the members are summed together across the array.

So, if we had two arrays [1, 2, 3] and [4, 5, 6]:

* Adding results in [5, 7, 9]
* Summation results in [6, 15] or 21 depending on the axis of summation.

---

### Review: Adding Two Arrays

Recall that when we add arrays, we see member-wise addition:

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
print("Adding:")
print(f"arr_a:                {arr_a}")
print(f"arr_b:                {arr_b}")
print(f"np.add(arr_a, arr_b): {np.add(arr_a, arr_b)}")
```

Output:

```
Adding:
arr_a:                [1 2 3 4]
arr_b:                [5 6 7 8]
np.add(arr_a, arr_b): [ 6  8 10 12]
```

---

### Summing an Array

Summation of a single array will always result in a scalar value equivalent
to the sum of all members in the array.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print("Summation:")
print(f"Array:                {arr}")
print(f"np.sum(arr):          {np.sum(arr)}")
```

Output:

```
Summation:
Array:                [1 2 3 4]
np.sum(arr):          10
```

---

### Summing Two Arrays on the Y Axis

Wen we sum on the Y axis (`axis=0` - default), we obtain the sum of the
sums of the arrays.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
print("Summation (y-Axis):")
print(f"arr_a:                {arr_a}")
print(f"arr_b:                {arr_b}")
print(f"np.sum(arr_a, arr_b): {np.sum([arr_a, arr_b])}")
```

Output:

```
Summation (y-Axis):
arr_a:                [1 2 3 4]
arr_b:                [5 6 7 8]
np.sum(arr_a, arr_b): 36
```

---

### Summing Two Arrays on the X Axis

Wen we sum on the X axis (`axis=1`), we obtain an array containing the
sums of the arrays.

```python
import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
print("Summation (x-Axis):")
print(f"arr_a:                {arr_a}")
print(f"arr_b:                {arr_b}")
print(f"np.sum(arr_a, arr_b): {np.sum([arr_a, arr_b], axis=1)}")
```

Output:

```
Summation (x-Axis):
arr_a:                [1 2 3 4]
arr_b:                [5 6 7 8]
np.sum(arr_a, arr_b): [10 26]
```

---

### Cumulative Summation

In cumulative summation each element in the resulting array is the sum of
the array up to that element's index but ignoring higher indices.

If we perform a cumulative summation on the array `[1, 2, 3, 4]`

We compute it like this:

|index|computation|result|
|:-:|-|-:|
|0|1|1|
|1|1 + 2|3|
|2|1 + 2 + 3|6|
|3|1 + 2 + 3 + 4|10|

Which results in `[1, 3, 6, 10]`

. . . . . . . . . .

NumPy provides the `cumsum()` function for cumulative summation:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print("Cumulative sum:")
print(f"Array:                {arr}")
print(f"np.cumsum(arr):       {np.cumsum(arr)}")
```

Output:

```
Cumulative sum:
Array:                [1 2 3 4]
np.cumsum(arr):       [ 1  3  6 10]
```

---
