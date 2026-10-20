## SciPy Constants

One of the useful features of SciPy is its large collection of
[constants](https://docs.scipy.org/doc/scipy/reference/constants.html).

Developers frequently need the values of various physical constants for
computations and conversions in their code.

### Accessing Constants

To access the constants in SciPy, use the `constants` module after importing
`scipy`...

```python
import scipy as sp

print("π =", sp.constants.pi)
```

... or just import the `constants` module itself

```python
from scipy import constants as sc

print("π =", sc.pi)
```

Output:

```
π = 3.141592653589793 
```

---

### So Many Constants...

I will forgo including all of the constants in these notes, but the
associated code file: [constants.py](./01_constants.py) includes examples
of many of them.

---
