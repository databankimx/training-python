## The `functools` Module

The `functools` module provides tools for working with functions: caching their
results, creating new functions from existing ones, reducing a sequence to one
value, and making decorators behave well.

Each lesson in this chapter covers one tool:

* [Caching with `lru_cache()`](./01_lru_cache.md): remember results so repeated calls are fast
* [Creating Functions with `partial()`](./02_partial.md): fix some arguments of a function
* [Reducing a Sequence with `reduce()`](./03_reduce.md): combine many values into one
* [Keeping Metadata with `wraps()`](./04_wraps.md): keep a decorated function's name and docstring
* [Dispatching by Type with `singledispatch()`](./05_singledispatch.md): choose a function by argument type

The examples import each tool by name:

```python
from functools import lru_cache, partial, reduce, wraps, singledispatch
```

---
