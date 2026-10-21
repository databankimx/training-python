## Numbers

So far, we've been looking at strings and displaying output to the user.
That's useful, but the main thing a computer does is *compute*.

To compute anything, we need to work with numbers instead of strings.

---

### Numeric Data Types

Python provides three types of numbers:

* integer (`int`)
* floating-point decimal (`float`)
* complex numbers (`complex`)

The language also provides three constructor (casting) functions to convert
to numeric types, usually from strings:

* `int(x)` converts `x` to an integer
* `float(x)` converts `x` to a floating-point decimal
* `complex(r, i)` converts `r` and `i` to a complex number, where
    * `r` is the real part
    * `i` is the imaginary part (the default value is `0`)

---

### Built-In Numeric Functions

Python also includes several built-in functions for working with numbers:

* `abs(x)` returns the absolute value of `x`
* `divmod(x, y)` returns a pair of values (a tuple):
    * the integer division of `x / y`, and
    * the remainder, `x % y`
* `pow(x, y)` returns `x` raised to the power of `y`
* `c.conjugate()` returns the conjugate of a complex number `c`

---

### Supported Arithmetic Operators

Python has the standard set of arithmetic operators you'll find in most
programming languages, plus a couple that are less common.

| Operator | Meaning | Example(s) | Notes |
|-|-|-|-|
| `+` | add | `3 + 2` -> `5` | |
| `-` | subtract | `3 - 2` -> `1` | |
| `*` | multiply | `3 * 2` -> `6` | |
| `/` | divide | `3 / 2` -> `1.5` | |
| | | `4 / 2` -> `2.0` | Division always returns a float |
| `**` | exponent | `3 ** 2` -> `9` | |
| `//` | integer division | `3 // 2` -> `1` | Rounds down (see below) |
| `%` | modulo | `3 % 2` -> `1` | The remainder |

#### A closer look at `//`

Integer division rounds *down*, toward negative infinity. For positive numbers,
that looks like "drop the decimal part." For negative numbers, it doesn't:

```python
print(7 // 2)    # 3
print(-7 // 2)   # -4, not -3
```

The `-7 // 2` result surprises most people the first time. Keep it in mind
whenever negative numbers are involved.

---

### Operator Precedence

Okay, we're going back to pre-algebra class.

Python follows the PEMDAS order of operations when it evaluates arithmetic.
Operations higher on the list run before the ones below them:

* [**P**]arentheses (and other grouping symbols)
* [**E**]xponents
* [**M**]ultiplication and [**D**]ivision
* [**A**]ddition and [**S**]ubtraction

Operators with the same precedence run from left to right, with one exception.
Exponents group from right to left, so `2 ** 3 ** 2` means `2 ** (3 ** 2)`, which
is `2 ** 9`, or `512`. Read it left to right and you'd get `64`. Python won't
agree with you.

---

So, following PEMDAS, consider this expression:

`3 + 2 * 4`

Multiplication comes before addition, so it runs first (`2 * 4` -> `8`), which
turns the expression into:

`3 + 8`, which yields `11`

---

Now add some grouping, which outranks multiplication:

`(3 + 2) * 4`

The parentheses run first (`3 + 2` -> `5`), which turns the expression into:

`5 * 4`, which yields `20`

---

### A Note on Python Integers

> Integers in Python are not fixed-size, like they are in many other languages.
> The largest integer you can make is limited only by the memory your computer
> has available.

---

