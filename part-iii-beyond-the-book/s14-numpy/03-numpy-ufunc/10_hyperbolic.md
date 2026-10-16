## Hyperbolic Functions

NumPy exposes the hyperbolic functions as well:

* `sinh()`
* `cosh()`
* `tanh()`
* `arcsinh()`
* `arccosh()`
* `arctanh()`

We'll handle these just like we did in the previous examples:

```python
import numpy as np

def print_out(txt: str, lbl: str, lst: list[int], arr: np.ndarray) -> None:
    print(f"{txt.title()}:")
    for d, r in zip(lst, arr):
        if round(d) == 0: d = 0.0
        if round(r) == 0: r = 0.0
        if r > 1000000: r = np.inf
        if isinstance(d, int):
            print(f"{lbl}({d:>3}) = {r:>5.2f}")
        else:
            print(f"{lbl}({d:>6.2f}) = {r:>5.2f}")
    print()

deg = [45, 90, 135, 180, 225, 270, 315, 360]
rad = np.radians(deg)
s = np.sinh(rad)
print_out("hyperbolic sine", "sinh", deg, s)
c = np.cosh(rad)
print_out("hyperbolic cosine", "cosh", deg, c)
t = np.tanh(rad)
print_out("hyperbolic tangent", "tanh", deg, t)
a_s = np.arcsinh(s)
print_out("hyperbolic arcsine", "arcsinh", s, a_s)
a_c = np.arccosh(c)
print_out("hyperbolic arccosine", "arccosh", c, a_c)
a_t = np.arctanh(t)
print_out("hyperbolic arctangent", "arctanh", t, a_t)
```

Output:

```
Hyperbolic Sine:
sinh( 45) =  0.87
sinh( 90) =  2.30
sinh(135) =  5.23
sinh(180) = 11.55
sinh(225) = 25.37
sinh(270) = 55.65
sinh(315) = 122.07
sinh(360) = 267.74

Hyperbolic Cosine:
cosh( 45) =  1.32
cosh( 90) =  2.51
cosh(135) =  5.32
cosh(180) = 11.59
cosh(225) = 25.39
cosh(270) = 55.66
cosh(315) = 122.08
cosh(360) = 267.75

Hyperbolic Tangent:
tanh( 45) =  0.66
tanh( 90) =  0.92
tanh(135) =  0.98
tanh(180) =  1.00
tanh(225) =  1.00
tanh(270) =  1.00
tanh(315) =  1.00
tanh(360) =  1.00

Hyperbolic Arcsine:
arcsinh(  0.87) =  0.79
arcsinh(  2.30) =  1.57
arcsinh(  5.23) =  2.36
arcsinh( 11.55) =  3.14
arcsinh( 25.37) =  3.93
arcsinh( 55.65) =  4.71
arcsinh(122.07) =  5.50
arcsinh(267.74) =  6.28

Hyperbolic Arccosine:
arccosh(  1.32) =  0.79
arccosh(  2.51) =  1.57
arccosh(  5.32) =  2.36
arccosh( 11.59) =  3.14
arccosh( 25.39) =  3.93
arccosh( 55.66) =  4.71
arccosh(122.08) =  5.50
arccosh(267.75) =  6.28

Hyperbolic Arctangent:
arctanh(  0.66) =  0.79
arctanh(  0.92) =  1.57
arctanh(  0.98) =  2.36
arctanh(  1.00) =  3.14
arctanh(  1.00) =  3.93
arctanh(  1.00) =  4.71
arctanh(  1.00) =  5.50
arctanh(  1.00) =  6.28
```

---
