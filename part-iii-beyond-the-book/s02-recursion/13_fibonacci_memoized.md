## Storing Previously Computed Values (Memoization)

That's not a typo, by the way, *memoization* is a process of storing the
previously computed values in a *memo* (short for *memorandum* - Latin: "to
be remembered") and then retrieving existing values instead of recomputing them.

Let's come up with a way to store the computed values as we go and improve our
function.

---

### The Code

```python
from count_calls import CountCalls

@CountCalls
def fibonacci(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]
```

> Note: the code file turns off Pylint's `dangerous-default-value` warning for
> the `cache` default. That comment stays in the code file. The default is
> deliberate, as explained below.

For consistency, we'll test this improved algorithm with the same value: 
`n = 40`

```python
n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
Calculated F(40) = 102,334,155
call_count = 79
```

This time, our call finished in under a second and only required 79 calls.
Each new value makes two calls: one that goes deeper to compute the next value,
and one that finds a value already in the cache.

For this algorithm, the call count is 2n − 1. Since that grows in direct
proportion to *n*, we're now getting answers in linear time. Compare that with
the roughly 331 million calls of the naive version.

> Note: One common gotcha in Python is that a mutable default value, such as
> a dictionary in a function signature, is created only once, when the function
> is defined. Here that's exactly what we want. The memo is shared across calls,
> so if we call this function again after using it once, the memo still holds
> the previous values, and it becomes more efficient the more it is used during
> the program's execution.
>
> The Part I bonus lesson on
> [mutable default values](../../part-i-basics/ch08-functions/lessons/16_bonus_mutable_defaults.md)
> explains the gotcha in more detail.

Because the memo lives in the default argument, `call_count` also keeps growing
across calls, the same as in lesson 11.

### Python's Built-In Option

Since Python 3.9, the standard library has a decorator that does this kind of
memoization for you: `functools.cache`.

```python
from functools import cache

@cache
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (memoized by functools.cache)"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

In practice, this is usually the better choice. The hand-written version above
shows the idea behind it.

---
