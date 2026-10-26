## Numerical Integration

Integration finds the area under a curve. Some curves have a formula you can
integrate by hand. Many do not, and in data science the function often comes from
measurements, so we estimate the area numerically.

SciPy provides these tools in the `scipy.integrate` module. The code for this
lesson is in [09_integrate.py](./09_integrate.py).

---

### Integrating a Function with `quad()`

`quad()` takes a function and the lower and upper limits of integration. It
returns two values: the estimated integral, and an estimate of the error.

```python
from scipy.integrate import quad

def square(x: float) -> float:
    return x ** 2

value, error = quad(square, 0, 1)
print(f"Integral of x² from 0 to 1 = {value:.4f}")
```

Output:

```
Integral of x² from 0 to 1 = 0.3333
```

The exact answer is 1/3, which the estimate matches to four decimal places.

---

### Integrating a Built-in Function

Any function that takes one number and returns one number can be integrated.
Here we integrate the sine function from 0 to π:

```python
import math
from scipy.integrate import quad

value, _ = quad(math.sin, 0, math.pi)
print(f"Integral of sin(x) from 0 to π = {value:.4f}")
```

Output:

```
Integral of sin(x) from 0 to π = 2.0000
```

The exact answer is 2. The underscore discards the error estimate, which we
don't need here.

---

### Checking the Error

The second value from `quad()` is an estimate of how far the result could be from
the true answer. For smooth functions over a finite range, the estimate is very small.
Check it when you're unsure whether the result is reliable.

```python
print(f"Estimated error is small: {error < 1e-10}")
```

Output:

```
Estimated error is small: True
```

---

### Try It

Integrate `x³` from 0 to 2. The exact answer is 4. Compare your result with
the exact value, and check how small the error estimate is.

---
