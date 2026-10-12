## A Word on Constants

There are many cases where you need a variable to contain a value that will
never be changed (the value stays the same throughout the program runtime).

This "variable that isn't variable" idea is called a *constant*.

### We Don't Have Constants

Python does not have a way to make a variable constant.

Although some data types are immutable (which means their values cannot be
modified), all can be replaced with a different value entirely.

### Indicating the Intent to be Constant

Because we cannot actually make a variable constant, we instead indicate to
other developers that the value should not be changed by naming the variable
in `ALL_CAPS_SNAKE_CASE`.

Code Sample:

Here, we are defining a constant value for *π* and then computing area of a 
circle based on two different values for the radius.

Because we never want the value of *π* to change, we name it `PI` instead of 
`pi`.

```python
PI = 3.14159

r = 2
print(f"A circle with radius {r} has an area of {PI * r ** 2}")

r = 3
print(f"A circle with radius {r} has an area of {PI * r ** 2}")
```

Output:

```
A circle with radius 2 has an area of 12.56636
A circle with radius 3 has an area of 28.27431
```

---

> **Python 3.13+:** A `Final` annotation from `typing` can hint that a
> variable should not be reassigned, and type checkers like `mypy` will
> flag violations. But this is still a convention enforced by tooling, not
> the language itself.

---
