## Discrete Difference Computation

Like products and summation, computing discrete differences is not the 
same as array subtraction.

When we subtract across two arrays, we perform member-wise subtractions by
index of `array1[i] - array2[i]`.

When we perform difference computation:

* Along one array, we compute `array[i+1] - array[i]` at each index
* Across two arrays
    * Along the y-axis, we compute `array2[i] - array1[i]` at each index  
      This is essentially the opposite of array subtraction
    * Along the x-axis, we compute each array separately (by the one-array
      rule above) and return an array containing the two difference arrays

---

### Review: Array Subtraction

Let's review the behavior of array subtraction:

```python
import numpy as np

arr_a = np.array([3, 9, 6, 1, 4])
arr_b = np.array([5, 8, 7, 2, 0])

print("Subtraction:")
print(f"arr_a:  {arr_a}")
print(f"arr_b:  {arr_b}")
print("np.subtract(arr_a, arr_b):")
print(f"{np.subtract(arr_a, arr_b)}")
```

Output:

```
Subtraction:
arr_a:  [3 9 6 1 4]
arr_b:  [5 8 7 2 0]
np.subtract(arr_a, arr_b):
[-2  1 -1 -1  4]
```

---

### Differences along One Array

If we have an array like this: `arr = [1, 2, 4, 7]` and we compute the discrete
differences, the process looks like this:

`arr[1] - arr[0]` = 2 - 1 = 1  
`arr[2] - arr[1]` = 4 - 2 = 2  
`arr[3] - arr[2]` = 7 - 4 = 3

There is no `arr[4]`, so we don't subtract `arr[3]` from anything.  
This yields `[1, 2, 3]`

Let's see that in action:

```python
import numpy as np

arr = np.array([3, 9, 6, 1, 4])

print("Difference:")
print(f"arr:    {arr}")
print("np.diff(arr):")
print(f"{np.diff(arr)}")
```

Output:

```
arr:    [3 9 6 1 4]
np.diff(arr):
[ 6 -3 -5  3]
```

---

### Computing *n*th-Degree Differences

Difference computation can be performed recursively by adding the `n` 
argument to the `diff()` call.

The process looks like this:

Let's say we have `arr = [1, 2, 4, 7]` and we pass `n = 3`

1. We already know that `diff(arr)` yields `[1, 2, 3]`
    * This is the first-degree difference
2. The process now acts as though we called `diff([1, 2, 3])`
    * This yields a second-degree difference of `[1, 1]`
3. On the third (and final, since `n = 3`) pass, we perform `diff([1, 1])`
    * This yields `[0]`

At this point, not further recursions could be performed, so we would need
a longer array in order to pass a higher value for `n`.

```python
import numpy as np
from utility_functions import ord_suffix

arr = np.array([3, 9, 6, 1, 4])

print("Higher-Degree Difference:")
print(f"arr:    {arr}")
for i in range(len(arr) - 1):
    print("...")
    r = i + 1
    print(f"np.diff(arr, n={r}):")
    print(f"{r}{ord_suffix(r)}-degree: {np.diff(arr, n=r)}")
```

Output:

```
Higher-Degree Difference:
arr:    [3 9 6 1 4]
...
np.diff(arr, n=1):
1st-degree: [ 6 -3 -5  3]
...
np.diff(arr, n=2):
2nd-degree: [-9 -2  8]
...
np.diff(arr, n=3):
3rd-degree: [ 7 10]
...
np.diff(arr, n=4):
4th-degree: [3]
```

---

### Difference across Two Arrays (y-Axis)

Along the y-axis, when we compute differences, we're essentially performing
subtractions in reverse. The second array is treated as though it were the
[i + 1] index.

```python
import numpy as np

arr_a = np.array([3, 9, 6, 1, 4])
arr_b = np.array([5, 8, 7, 2, 0])

print("Difference (y-Axis):")
print(f"arr_a:  {arr_a}")
print(f"arr_b:  {arr_b}")
print("np.diff([arr_a, arr_b], axis=0):")
print(f"{np.diff([arr_a, arr_b], axis=0)}")
```

Output:

```
Difference (y-Axis):
arr_a:  [3 9 6 1 4]
arr_b:  [5 8 7 2 0]
np.diff([arr_a, arr_b], axis=0):
[[ 2 -1  1  1 -4]]
```

Note, that even though we have only one array of differences when 
computing along the y-axis, this still returns an array of arrays.

---

### Difference across Two Arrays (x-Axis)

Along the x-axis, we treat each array as if it were being processed
separately.

So `diff([arr_a, arr_b], axis=1)` = `np.array([diff(arr_a), diff(arr_b)])`

```python
import numpy as np

arr_a = np.array([3, 9, 6, 1, 4])
arr_b = np.array([5, 8, 7, 2, 0])

print("Difference (x-Axis):")
print(f"arr_a:  {arr_a}")
print(f"arr_b:  {arr_b}")
print("np.diff([arr_a, arr_b], axis=1):")
print(f"{np.diff([arr_a, arr_b], axis=1)}")
```

Output:

```
Difference (x-Axis):
arr_a:  [3 9 6 1 4]
arr_b:  [5 8 7 2 0]
np.diff([arr_a, arr_b], axis=1):
[[ 6 -3 -5  3]
 [ 3 -1 -5 -2]]
```

---
