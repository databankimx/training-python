## Dispatching by Type with `singledispatch()`

`singledispatch()` turns a function into one that chooses a different implementation
based on the type of its first argument. The default version handles any type. You
add more versions with `.register()`.

The code for this lesson is in [05_singledispatch.py](./05_singledispatch.py):

```python
from functools import singledispatch

@singledispatch
def describe(_value: object) -> str:
    """Describe any value that has no specific handler"""
    return "something"

@describe.register(int)
def _(_value: int) -> str:
    """Describe an integer"""
    return "an integer"

@describe.register(list)
def _(value: list) -> str:
    """Describe a list by its length"""
    return f"a list of {len(value)} items"

print(describe(3))
print(describe([1, 2]))
print(describe("hi"))
```

---

### Calling the Dispatched Function

Each call goes to the version registered for the argument's type. Any type without a
registration falls back to the default:

Output:

```
an integer
a list of 2 items
something
```

`3` is an `int`, and `[1, 2]` is a `list`. The string `"hi"` has no registration, so
the default version runs.

---

### Why the Functions Are Named `_`

Each registered version is a separate function, but only the registration matters, so
each one is named `_`. The name `describe` stays bound to the dispatching function. The default and
`int` versions take the value without using it, so their parameter is named
`_value`. Pylint warns about unused arguments, but it ignores names that start with
an underscore.

---

### When to Use `singledispatch()`

Use it when the behavior depends on the type of one argument, and you want each type's
code in its own function. For checks on several arguments, or on values rather than
types, a normal `if` statement is usually clearer.

---

### Try It

Register a version for `str` that returns the number of characters, and call
`describe("hi")` again. Predict the new output before you run it.

---
