## Ch 2 - Lesson 8: Numbers

So far we have been looking at strings and displaying output to the user.
The main feature of a computer is that it *computes*, and that requires
working with numbers.

---

### Numeric Data Types

Python provides three types of numbers:

- integer (`int`)
- floating-point decimal (`float`)
- complex numbers (`complex`)

And three casting functions to convert to numeric types:

- `int(x)` - converts `x` to an integer
- `float(x)` - converts `x` to a floating-point decimal
- `complex(r, i)` - creates a complex number with real part `r` and imaginary part `i` (default `0`)

---

### Built-In Numeric Functions

| Function | Description |
|-|-|
| `abs(x)` | Absolute value of `x` |
| `divmod(x, y)` | Integer division and remainder of `x / y` |
| `pow(x, y)` | `x` to the power of `y` |
| `c.conjugate()` | Conjugate of complex number `c` |

---

### Supported Arithmetic Operators

| Operator | Meaning | Example | Notes |
|-|-|-|-|
| `+` | add | `3 + 2` -> `5` | |
| `-` | subtract | `3 - 2` -> `1` | |
| `*` | multiply | `3 * 2` -> `6` | |
| `/` | divide | `3 / 2` -> `1.5` | Always returns a float |
| | | `4 / 2` -> `2.0` | Even when the result is whole |
| `**` | exponent | `3 ** 2` -> `9` | |
| `//` | integer division | `3 // 2` -> `1` | Drops the decimal part |
| `%` | modulo | `3 % 2` -> `1` | Remainder |

---

### Operator Precedence

Python follows PEMDAS order of operations:

- **P**arentheses (and other grouping symbols)
- **E**xponents
- **M**ultiplication and **D**ivision
- **A**ddition and **S**ubtraction

Within the same precedence level, operations are performed left to right.

```python
print(3 + 2 * 4)    # 11 - multiplication first
print((3 + 2) * 4)  # 20 - parentheses first
```

---

### A Note on Python Integers

Integers in Python are not fixed-size like they are in many other languages.
The maximum value for a Python integer is limited only by available system RAM.

---
