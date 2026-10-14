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

For consistency, we'll test this improved algorithm with the same value: 
`n = 40`

```python
n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
F(40) = 102,334,155
call_count =  79
```

This time, our call finished in under a second and only required 79 calls: 
once to store each number and once to retrieve it to get to the next number.

As *n* increases, `2 * n` becomes a lot smaller than `2ⁿ`. We're now getting
answers in linear time.

> Note: One interesting tidbit about Python is that if we initialize a mutable
> variable as a default value in a function signature, it will only 
> initialize one time. If I call this function again, after I have already 
> used it once, the memo will still contain the previous calculation's 
> values, so it becomes more efficient the more it is used during the 
> program's execution.

---
