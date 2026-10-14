## Do I Have To Use Recursion?

Short answer: No.

For any recursive algorithm, there is always a way to complete the same task
iteratively (using a loop, e.g.) without needing recursion. Sometimes, though,
the iterative algorithm may be much more complicated.

That's not the case with the Fibonacci Sequence, so here is an iterative
solution (in the interest of completeness):

---

### The Code

```python
from count_calls import CountCalls

@CountCalls
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (iterative algorithm)"""
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]
```

For consistency, we'll test this algorithm with the same value: `n = 40`

```python
n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
F(40) = 102,334,155
call_count =  1
```

This completes in milliseconds, regardless how large *n* is (provided you have
enough memory to hold the resulting value for `F(n)`)

---
