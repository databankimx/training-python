## Trigonometric Functions

NumPy provides a collection of `ufunc` functions to compute various 
trigonometry values.

There are a couple of items we should be aware of before we start digging 
into the trig functions, since most of them take their arguments and/or
return values in radians:

* `numpy.pi`: The constant ***π*** - see
  [NumPy Constants](https://numpy.org/doc/stable/reference/constants.html)
* `numpy.radians()`: Convert degrees to radians (alias: `numpy.deg2rad()`)
* `numpy.degrees()`: Convert radians to degrees (alias: `numpy.rad2deg()`)

Quick math review: 360 degrees = 2π radians

Let's see that in action:

```python
import numpy as np

lst = [45, 90, 135, 180, 225, 270, 315, 360]
for d, r in zip(lst, np.radians(lst)):
    print(f"{d:>3}° = {r / np.pi:.2f}πᶜ")
```

Output:

```
Degrees to Radians:
 45° = 0.25πᶜ
 90° = 0.50πᶜ
135° = 0.75πᶜ
180° = 1.00πᶜ
225° = 1.25πᶜ
270° = 1.50πᶜ
315° = 1.75πᶜ
360° = 2.00πᶜ
```

---

### Hypotenuse of a Right Triangle

We're all familiar with the Pythagorean Theorem, which states that the
square of the hypotenuse of a right triangle is equal to the sum of the
squares of the other two sides, or more simply: `a² + b² = c²`

NumPy provides the `hypot()` function to perform this calculation:

```python
import numpy as np

base, perp = 3.0, 4.0
hyp = np.hypot(base, perp)
print(f"For legs {base} and {perp}, hypotenuse = {hyp}")
```

Output:

```
For legs 3.0 and 4.0, hypotenuse = 5.0
```

---

### Sine, Cosine, and Tangent

NumPy exposes functions for the standard trigonometric functions:

* `sin()`: Calculates the sine of an angle (given in radians)
* `cos()`: Calculates the cosine of an angle (given in radians)
* `tan()`: Calculates the tangent of an angle (given in radians)

I'll use a separate function to print out the results of each:

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
            print(f"{lbl}({d:>5.2f}) = {r:>5.2f}")
    print()
```

```python
import numpy as np

deg = [45, 90, 135, 180, 225, 270, 315, 360]
rad = radians(deg)
s = np.sin(rad)
print_out("sine", "sin", lst, s)
c = np.cos(rad)
print_out("cosine", "cos", lst, c)
t = np.tan(rad)
print_out("tangent", "tan", lst, t)
```

Output:

```
Sine:
sin( 45) =  0.71
sin( 90) =  1.00
sin(135) =  0.71
sin(180) =  0.00
sin(225) = -0.71
sin(270) = -1.00
sin(315) = -0.71
sin(360) =  0.00

Cosine:
cos( 45) =  0.71
cos( 90) =  0.00
cos(135) = -0.71
cos(180) = -1.00
cos(225) = -0.71
cos(270) =  0.00
cos(315) =  0.71
cos(360) =  1.00

Tangent:
tan( 45) =  1.00
tan( 90) =   inf
tan(135) = -1.00
tan(180) =  0.00
tan(225) =  1.00
tan(270) =   inf
tan(315) = -1.00
tan(360) =  0.00
```

---

### Arcsine, Arccosine, and Arctangent

NumPy also exposes the inverse trigonometric functions:

* `arcsine()`
* `arccosine()`
* `arctangent()`

These take the results (in radians) from the previous functions.

```python
# -- SNIP --

a_s = np.arcsin(s)
print_out("arcsine", "arcsin", s, a_s)
a_c = np.arccos(c)
print_out("arccosine", "arccos", c, a_c)
a_t = np.arctan(t)
print_out("arctangent", "arctan", c, a_t)
```

Output:

```
Arcsine:
arcsin( 0.71) =  0.79
arcsin( 1.00) =  1.57
arcsin( 0.71) =  0.79
arcsin( 0.00) =  0.00
arcsin(-0.71) = -0.79
arcsin(-1.00) = -1.57
arcsin(-0.71) = -0.79
arcsin( 0.00) =  0.00

Arccosine:
arccos( 0.71) =  0.79
arccos( 0.00) =  1.57
arccos(-0.71) =  2.36
arccos(-1.00) =  3.14
arccos(-0.71) =  2.36
arccos( 0.00) =  1.57
arccos( 0.71) =  0.79
arccos( 1.00) =  0.00

Arctangent:
arctan( 0.71) =  0.79
arctan( 0.00) =  1.57
arctan(-0.71) = -0.79
arctan(-1.00) =  0.00
arctan(-0.71) =  0.79
arctan( 0.00) =  1.57
arctan( 0.71) = -0.79
arctan( 1.00) =  0.00
```

---
