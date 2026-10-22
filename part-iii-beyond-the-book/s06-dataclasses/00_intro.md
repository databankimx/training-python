## Understanding Python Dataclasses

The dataclasses library was added in Python 3.7 as a utility tool for making 
classes whose primary purpose is storing data. It's part of the standard
library, so no installation is needed.

The `@dataclass` decorator automatically adds generated special methods such as
`__init__()`, `__repr__()`, and `__eq__()` to user-defined classes.

[Dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)

Dataclasses are like normal classes in Python, but they have some basic 
functions like instantiation, comparing, and printing the classes already 
implemented.

Syntax Notes:

We mark a class with the `@dataclass` decorator along with any of its 
optional arguments.

```
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, 
                          unsafe_hash=False, frozen=False)
    Parameters:
    - init: If true  __init__() method will be generated
    - repr: If true  __repr__() method will be generated
    - eq: If true  __eq__() method will be generated
    - order: If true  __lt__(), __le__(), __gt__(), and __ge__() methods will be generated.
    - unsafe_hash: If False __hash__() method is generated according to how eq and frozen are set
    - frozen: If true assigning to fields will generate an exception.
```

These are the arguments from Python 3.7. The `match_args`, `kw_only`, and `slots`
arguments were added in Python 3.10, and the later lessons use `match_args` and
`kw_only`, so those lessons need Python 3.10 or later.

---
