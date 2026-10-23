## Creating Functions with `partial()`

`partial(function, ...)` returns a new function with some arguments already filled in.
When you call the new function, you supply only the arguments that are left.

The code for this lesson is in [02_partial.py](./02_partial.py):

```python
from functools import partial

def power(base: int, exponent: int) -> int:
    """Raise base to the power of exponent"""
    return base**exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(5))
print(cube(3))
```

---

### Fixing an Argument by Name

`partial(power, exponent=2)` creates a function that always passes `exponent=2`. Calling
`square(5)` is the same as calling `power(5, exponent=2)`:

Output:

```
25
27
```

`cube(3)` is `power(3, exponent=3)`, which is 27.

---

### When to Use `partial()`

Use `partial()` when a function expects a callback with fewer arguments than you have
ready. For example, a sorting or mapping function might need one argument, while your
function needs two. Fixing the second argument with `partial()` gives you a function
that fits, without writing a new `def` for it.

> Note: Closures from [s08](../s08-closures/05_closures.md) also make a function that remembers
> values, but they capture variables from an enclosing function, and you write the inner
> function yourself. `partial()` takes an existing function and fixes some of its
> arguments, so you don't write any new code.

---

### Try It

Create a function `from_binary` from `int()` by fixing its `base` argument to `2`. Then
call it on `"1011"`. Predict the result before you run it.

---
