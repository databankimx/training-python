## Keeping Metadata with `wraps()`

A decorator usually returns a new function, called `wrapper` here. Without help,
that new function takes the place of the original, so its name and docstring are lost.
`wraps()` copies them over.

The code for this lesson is in [04_wraps.py](./04_wraps.py):

```python
from functools import wraps

def logged(func):
    """Print a message before calling the decorated function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Log the call, then run the original function"""
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

@logged
def greet(name: str) -> str:
    """Return a greeting for the given name"""
    return f"Hello, {name}"

print(greet("Ana"))
print(greet.__name__)
print(greet.__doc__)
```

---

### Calling the Decorated Function

`logged` prints a line, then runs the original function and returns its result:

Output:

```
calling greet
Hello, Ana
```

---

### Checking the Name and Docstring

Because `wraps(func)` is applied to `wrapper`, the new function reports the original
name and docstring:

Output:

```
greet
Return a greeting for the given name
```

Without `@wraps(func)`, `greet.__name__` would be `wrapper`, and the docstring would be
the one written for `wrapper`. Tools such as help() and debuggers rely on these values,
so `wraps()` should be used in almost every decorator.

> Note: `wrapper` is a closure, because it uses `func` from the enclosing `logged()`
> function. [s08](../s08-closures/08_decorators.md) explains closures and decorators in
> more detail, including how the `@logged` line is applied to `greet`.

---

### Try It

Remove the `@wraps(func)` line and run the script again. Predict the output of the
last two `print()` calls before you run it.

---
