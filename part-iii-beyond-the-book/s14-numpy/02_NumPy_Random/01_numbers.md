## Generating Random Numbers

There are many scenarios where generating a random number (or a group of
random numbers) is necessary in code.

The `numpy.random` library provides mechanisms for generating random 
numbers and arrays of random numbers.

---

### Generate a Random Integer

Generating a random integer in NumPy with the `random.randint()` function
is identical to using the standard `random` library.

```python
from numpy import random

min, max = 1, 100
x = random.randint(min, max + 1)
print(f"Random integer ({min} to {max}):\n{x}")
```

Output:

```
Random integer (1 to 100):
73
```

---

### Generate a Random Floating-Point Number

Similarly, using `random.rand()` function works as it did in the standard
`random` library.

```python
from numpy import random

x = random.rand()
print(f"Random floating-point number (0 to 1):\n{x:.2}")
```

Output:

```
Random floating-point number (0 to 1):
0.21
```

---

### Generating Arrays of Random Integers

Where the NumPy `random` library excels is in its ability to generate
arrays of random numbers.

---

#### 1D Array of Random Integers

To generate an array of random integers, we add an extra argument to the
`randint()` function: `size=n` (where *n* is the number of elements in a 
1D array).

```python
from numpy import random

ar_sz = 5
min, max = 1, 100
arr = random.randint(1, 101, ar_sz)
print(f"Random 1D int array ({min} to {max})", end=" ")
print(f"size: ({ar_sz}):\n{arr}")
```

Output:

```
Random 1D int array (1 to 100) size: (5):
[92  9 36 87 91]
```

---

#### 2D Array of Random Integers

We can generate a multidimensional array by providing a tuple to the
`size` argument.

```python
from numpy import random

ar_sz = (5, 3)
min, max = 1, 100
arr = random.randint(1, 101, size=ar_sz)
print(f"Random 2D int array ({min} to {max})", end=" ")
print(f"size: {ar_sz}:\n{arr}")
```

Output:

```
Random 2D int array (1 to 100) size: (5, 3):
[[ 93  85 100]
 [ 77  96  42]
 [ 28  79  36]
 [ 76  27  46]
 [ 44  71  83]]
```

---

### Generating Arrays of Random Floating-Point Numbers

The `rand()` function also accepts the `size` argument to generate
arrays of random floating-point numbers.

---

#### 1D Array of Random Floating-Point Numbers

Here's an example of a 1D random array of floats:

```python
from numpy import random

ar_sz = 5
arr = random.rand(ar_sz)
print(f"Random 1D float array", end=" ")
print(f"size: ({ar_sz}):\n{arr}")
```

Output:

```
Random 1D float array size: (5):
[0.98715549 0.36045883 0.98392484 0.69405782 0.7886433 ]
```

---

#### 2D Array of Random Floating-Point Numbers

Here's an example of a 2D random array of floats:

```python
from numpy import random

ar_sz = (5, 3)
arr = random.rand(*ar_sz)
print(f"Random 1D float array", end=" ")
print(f"size: {ar_sz}:\n{arr}\n")
```

Output:

```
Random 2D float array size: (5, 3):
[[0.43249298 0.77054268 0.53013784]
 [0.19433243 0.72105973 0.12617421]
 [0.39710772 0.99608305 0.29911744]
 [0.16619186 0.6244653  0.28504293]
 [0.11437847 0.35674426 0.2621795 ]]
```

---

### Choosing Random Numbers

Just like the standard `random.choice()`, NumPy's `random` module
exposes a `choice()` function.

The NumPy implementation adds the ability to both generate arrays and
to use arrays as the source data to choose among.

---

### Choosing a Random Number

Given a list or array of values, the `random.choice()` function can
randomly select an element:

```python
import numpy as np
from numpy import random

arr = np.array(range(1, 101))
x = random.choice(arr)
print(f"Random element from array (1 to 100):\n{x}")
```

Output:

```
Random element from array (1 to 100):
57
```

---

### Choosing a 1D Array of Random Numbers

Here's an example using `random.choice()` to populate a 1D array with
random data from a source array:

```python
import numpy as np
from numpy import random

arr = np.array(range(1, 101))
ar_sz = 5
new_arr = random.choice(arr, size=ar_sz)
print(f"Random array of {ar_sz} elements from array (1 to 100):")
print(f"{new_arr}")
```

Output:

```
Random array of 5 elements from array (1 to 100):
[45 50 66 88 75]
```

---

### Choosing a 2D Array of Random Numbers

Here's an example using `random.choice()` to populate a 2D array with
random data from a source array:

```python
import numpy as np
from numpy import random

arr = np.array(range(1, 101))
ar_sz = (5, 3)
new_arr = random.choice(arr, size=ar_sz)
print(f"Random array of {ar_sz} elements from array (1 to 100):")
print(f"{new_arr}")
```

Output:

```
Random array of (5, 3) elements from array (1 to 100):
[[100  23  13]
 [ 48   2  81]
 [ 70  87  32]
 [ 67  49  69]
 [ 72  34  33]]
```

---
