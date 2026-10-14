## Logarithms

Many statistical computations require the use of logarithms.

We should recall that the logarithm of a number, given a specified base,
is the exponent to which that base must be raised to yield the number.

if **x = log<sub>b</sub>(n)** then **b<sup>x</sup> = n**

For example: **log₂(8) = 3**, since **2³ = 8**

NumPy provides functions for logarithms with bases:

* 2 
* 10
* *e* (the *natural* log)

As with the other `ufunc` functions, these can be executed on a scalar or 
on an array, and in the latter case will perform the computation 
member-wise across the array.

---

### Computing log₂(array)

Let's compute the base 2 log of the numbers in an array:

Note: We're introducing a new function `arange()` that works just like the
standard `range()` function but returns an array (`ndarray`)

We'll use the `np.log2()` function to compute the logarithms.

```python
import numpy as np

flt_fmt = "{:.2f}".format
np.set_printoptions(formatter={"float_kind": flt_fmt})

arr = np.arange(1, 11)
print(f"Array: {arr}")
print(f"Log₂:  {np.log2(arr)}")
```

Output:

```
Array: [ 1  2  3  4  5  6  7  8  9 10]
Log₂:  [0.00 1.00 1.58 2.00 2.32 2.58 2.81 3.00 3.17 3.32]
```

---

### Computing log<sub>10</sub>(array)

Let's compute the base 10 log of the numbers in an array:

We'll use the `np.log10()` function to compute the logarithms.

```python
import numpy as np

flt_fmt = "{:.2f}".format
np.set_printoptions(formatter={"float_kind": flt_fmt})

arr = np.arange(1, 11)
print(f"Array: {arr}")
print(f"Log₂:  {np.log10(arr)}")
```

Output:

```
Array: [ 1  2  3  4  5  6  7  8  9 10]
Log₁₀: [0.00 0.30 0.48 0.60 0.70 0.78 0.85 0.90 0.95 1.00]
```

---

### Computing logₑ(array)

Let's compute the base *e* (or "natural") log of the numbers in an array:

We'll use the `np.log()` function to compute the logarithms.

```python
import numpy as np

flt_fmt = "{:.2f}".format
np.set_printoptions(formatter={"float_kind": flt_fmt})

arr = np.arange(1, 11)
print(f"Array: {arr}")
print(f"Log₂:  {np.log(arr)}")
```

Output:

```
Array: [ 1  2  3  4  5  6  7  8  9 10]
Logₑ:  [0.00 0.69 1.10 1.39 1.61 1.79 1.95 2.08 2.20 2.30]
```

---

### Logs of Other Bases

NumPy does not provide any function to take log at any base, so we can use 
the `frompyfunc()` along with `math.log()` to create a custom `ufunc` for
handling other bases:

```python
import numpy as np
from math import log

nplog = np.frompyfunc(log, 2, 1) # Custom ufunc

flt_fmt = "{:.2f}".format
np.set_printoptions(formatter={"float_kind": flt_fmt})

arr = np.arange(1, 11)
print(f"Array: {arr}")

logs = nplog(arr, 3)
print("Log₃: ", end=" [")
for n in logs:
    print(f"{n:.2f}", end=" ")
print("\b]")
```

Output:

```
Array: [ 1  2  3  4  5  6  7  8  9 10]
Log₃:  [0.00 0.63 1.00 1.26 1.46 1.63 1.77 1.89 2.00 2.10]
```

---
