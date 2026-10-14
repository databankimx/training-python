## Array Permutations

A permutation refers to an arrangement of elements.

For example: `[3, 2, 1]` is a permutation of `[1, 2, 3]` and vice-versa.

The `numpy.random` library provides two functions for permuting arrays:
`shuffle()` and `permutation()`

---

### Shuffling an Array

Just like the `shuffle()` function in the standard `random` library, the
NumPy implementation modifies the array in-place into dome random
permutation of the original order.

```python
import numpy as np
from numpy import random

arr = np.array(range(1, 11))
print(f"Original Array: {arr}")
random.shuffle(arr)
print(f"Shuffled Array: {arr}")
print(f"Original Array: {arr}")
```

Output:

```
Original Array: [ 1  2  3  4  5  6  7  8  9 10]
Shuffled Array: [ 8 10  1  4  6  7  5  9  3  2]
Original Array: [ 8 10  1  4  6  7  5  9  3  2]
```

---

### Permuting an Array

NumPy's `permutation()` function creates a new array containing a
random permutation of the original order but does not modify the original
array.

```python
import numpy as np
from numpy import random

arr = np.array(range(1, 11))
print(f"Original Array: {arr}")
new_arr = random.permutation(arr)
print(f"Permuted Array: {new_arr}")
print(f"Original Array: {arr}")
```

Output:

```
Original Array: [ 1  2  3  4  5  6  7  8  9 10]
Permuted Array: [10  9  3  2  5  6  8  4  7  1]
Original Array: [ 1  2  3  4  5  6  7  8  9 10]
```

---
