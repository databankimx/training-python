## A Word on Constants

Many programs need a variable that holds a value which should never change
during the program's lifetime. This "variable that isn't variable" is called
a *constant*.

---

### Python Does Not Have Constants

Python has no mechanism to enforce that a variable cannot be changed.
Although some data types are immutable (their contents cannot be modified),
all variables can be rebound to a different value entirely.

---

### Indicating the Intent to be Constant

Because we cannot truly make a variable constant, we instead signal to other
developers that the value should not be changed by naming it in
`ALL_CAPS_SNAKE_CASE`.

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
