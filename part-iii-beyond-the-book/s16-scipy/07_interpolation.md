## Interpolation

*Interpolation* estimates values between points that you already know. If you
know the values at x = 1 and x = 2, interpolation estimates the values at 1.33
and 1.66.

Interpolation is useful in several situations:

* **Imputation**: filling in missing values in a data set
* **Smoothing**: turning a set of discrete points into a continuous curve

SciPy provides these tools in the `scipy.interpolate` module. The code for this
lesson is in [07_interpolation.py](./07_interpolation.py).

---

### Linear Interpolation

`interp1d()` takes the known x and y values and returns a function. You call
that function with new x values to get the estimated y values:

```python
import numpy as np
from scipy.interpolate import interp1d

xs = np.arange(10)
ys = 2 * xs + 1
func = interp1d(xs, ys)
print(func(2.1))
```

Output:

```
5.2
```

The known points lie on the line `y = 2x + 1`, so the estimate is exact.

> Note: The new x values must fall within the range of the known x values. The
> function above accepts x values from 0 to 9. Passing 10 or -1 raises an error.

---

### Spline Interpolation

Linear interpolation joins the points with straight lines. A *spline* instead
fits a smooth curve through the points. The curve is made of *piecewise*
polynomial pieces, which means each section uses a different formula.

```python
from scipy.interpolate import UnivariateSpline

xs = np.arange(10)
ys = xs ** 2 + np.sin(xs) + 1
func = UnivariateSpline(xs, ys)
print(func(2.5))
```

The estimates do not match the true values closely. By default, `UnivariateSpline`
smooths the curve, so it does not pass exactly through the known points. Compare
the estimates with the true values in the script's output. Passing `s=0` forces
the curve through every known point, which gives exact interpolation at the known
points.

---

### Radial Basis Functions

`Rbf()` builds the interpolation from radial basis functions. A radial basis
function depends only on the distance from a fixed reference point. The `Rbf()`
function takes the same kind of input as `UnivariateSpline()`, and it returns a
callable function in the same way.

```python
from scipy.interpolate import Rbf

func = Rbf(xs, ys)
print(func(2.5))
```

Rbf interpolation works well with scattered points and with more than one
input dimension, which makes it more flexible than the one-dimensional methods
above.

---

### Try It

Run the script, which prints the estimated and actual values side by side for
the spline and radial basis methods. Then change the known points so they no
longer follow a simple curve, and see how well each method follows them.

---
