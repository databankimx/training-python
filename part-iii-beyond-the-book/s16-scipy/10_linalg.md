## Linear Algebra

Many scientific and data problems come down to solving a system of linear
equations, such as `3x + 2y = 5` and `x + 2y = 5`. NumPy can handle small
problems. SciPy's `scipy.linalg` module adds a fuller set of tools.

The code for this lesson is in [10_linalg.py](./10_linalg.py).

---

### Solving a System of Equations

Write the system as a matrix `A` of coefficients and a vector `b` of results.
`linalg.solve()` returns the vector `x` that makes `A x = b` true:

```python
import numpy as np
from scipy import linalg

a = np.array([[3.0, 2.0], [1.0, 2.0]])
b = np.array([5.0, 5.0])
x = linalg.solve(a, b)
print(f"Solution x = [{x[0]:.2f} {x[1]:.2f}]")
```

Output:

```
Solution x = [0.00 2.50]
```

Check the answer by substituting it back: `3(0) + 2(2.5) = 5` and
`0 + 2(2.5) = 5`.

---

### Determinant

The determinant is a single number that describes a square matrix. It is zero
when the matrix has no unique solution to a system of equations.

```python
from scipy import linalg

print(f"Determinant = {linalg.det(a):.4f}")
```

Output:

```
Determinant = 4.0000
```

For a 2 by 2 matrix, the determinant is `3 × 2 − 2 × 1 = 4`.

---

### Inverse

The inverse of a matrix, written `A⁻¹`, undoes the matrix. Multiplying a matrix by
its inverse gives the identity matrix.

```python
inv = linalg.inv(a)
print(f"Inverse = [[{inv[0, 0]:.2f} {inv[0, 1]:.2f}]")
print(f"           [{inv[1, 0]:.2f} {inv[1, 1]:.2f}]]")
```

Output:

```
Inverse = [[0.50 -0.50]
           [-0.25 0.75]]
```

Solving with `solve()` is usually better than computing the inverse and then
multiplying, because it's faster and more accurate.

---

### Try It

Change `b` to `[4.0, 3.0]` and predict the solution before you run the code.
Then substitute your answer back into both equations to check it.

---
