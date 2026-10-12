## Ch 2 - Lesson 8: Numbers

So far, we've been looking at strings and displaying output to the user.
While this is important, the main feature of a computer is that is, well,
***computes***.

Computations require us to have the ability to work with numbers instead of 
strings.

---

### Numeric Data Types

Python provides three types of numbers:

* integer (`int`)
* floating-point decimal (`float`)
* complex numbers (`complex`)

The language also provides three constructor (casting) functions to convert
to numeric types (typically from strings).

* `int(x)` converts `x` to an integer
* `float(x)` converts `x` to a floating-point decimal
* `complex(r, i)` converts `r` and `i` to a complex number where
    * `r` is the real number part
    * `i` is the imaginary part (default value is `0`)

---

### Built-In Numeric Functions

Additionally, Python includes several built-in functions for working with 
numbers:

* `abs(x)` calculates the absolute value of `x`
* `divmod(x, y)` calculates:
    * The integer division of `x / y` and
    * The remainder `x % y`
* `pow(x, x)` calculates `x` to the power of `y`
* `c.conjugate()` calculates the conjugate of a complex number `c`

---

### Supported Arithmetic Operators

Python provides the standard set of arithmetic operators you find in most
programming languages, as well as a couple that are less common.

|||||
|-|-|-|-|
|Operator|Meaning|Example(s)|Notes|
|+|add|`3 + 2` -> `5`||
|-|subtract|`3 - 2` -> `1`||
|*|multiply|`3 * 2` -> `6`||
|/|divide|`3 / 2` -> `1.5`||
|||`4 / 2` -> `2.0`|Division always returns a float|
|**|exponent|`3 ** 2` -> `9`||
|//|integer division|`3 // 2` -> `1`|Drops the decimal part after dividing|
|%|modulo|`3 % 2` -> `1`|Remainder|
|||||

---

### Operator Precedence

OK - We're going to travel back in time to pre-algebra class...

Python adheres to the PEMDAS order of operations when performing arithmetic
operations.

This means that operations higher on the list below are performed before 
items lower on the list.

* [**P**]arentheses (and other grouping symbols)
* [**E**]xponents
* [**M**]ultiplication and [**D**]ivision
* [**A**]ddition and [**S**]ubtraction

Within the same precedence, operations are performed from left to right.

---

So, following PEMDAS precedence, consider the following operation:

`3 + 2 * 4`

Multiplication has a higher precedence than addition, so it is performed
first (`2 * 4` -> `8`), making the expression the same as:

`3 + 8` which yields `11`

---

However, if we include grouping, which has higher precedence than
multiplication, like this:

`(3 + 2) * 4`

The operation in parentheses is performed first (`3 + 2` -> `5`), making 
the expression the same as:

`5 * 4` which yields `20`

---

### A note on Python Integers

Integers in Python are not fixed-size like they are in other languages.
Because of this, the maximum value for a Python integer is limited only by 
the available system RAM.

---
