## Caching with `lru_cache()`

A function that calls itself many times often computes the same values again and
again. `lru_cache()` saves each result the first time it's computed, and returns the
saved value for any later call with the same arguments.

This is the same idea as the memoized Fibonacci function in
[s02, lesson 13](../s02-recursion/13_fibonacci_memoized.md). There we stored each
result in a dictionary by hand. `lru_cache()` does that bookkeeping for us.

The code for this lesson is in [01_lru_cache.py](./01_lru_cache.py):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth Fibonacci number, using the cache for repeated calls"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
print(fib.cache_info())
```

---

### Applying the Decorator

Put `@lru_cache` above the function. The `maxsize=None` argument means the cache can
grow without limit. A number instead, such as `maxsize=128`, keeps only that many
recent results.

Without the cache, `fib(30)` would call `fib` more than a million times, because the
same smaller values are recomputed over and over.

---

### Reading the Cache Statistics

`cache_info()` reports how the cache was used:

Output:

```
832040
CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)
```

* `misses=31`: the values for `n` from 0 to 30 were each computed once.
* `hits=28`: the repeated calls were answered from the cache.
* `currsize=31`: 31 results are stored.

---

### Try It

Call `fib(40)` after `fib(30)`, and check how many new misses are added. Predict the
number before you run the code.

---
