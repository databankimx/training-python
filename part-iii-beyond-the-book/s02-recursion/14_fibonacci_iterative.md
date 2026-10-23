## Do I Have To Use Recursion?

Short answer: No.

For any recursive algorithm, there is always an equivalent iterative version
(using a loop, e.g.). Sometimes it needs an explicit stack, as we saw with the
nested lists, and sometimes the iterative algorithm may be much more complicated.

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
    return values[n]
```

For consistency, we'll test this algorithm with the same value: `n = 40`

```python
n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
Calculated F(40) = 102,334,155
call_count = 1
```

The `call_count` is 1 because there's no recursion. The decorator sees only the
one call, and the loop does all of the work.

The time grows in direct proportion to *n*, since the loop runs once for each
step. The list also holds every value up to `F(n)`, so memory grows with *n* too.
For `n = 40`, the run is effectively instant.

> Tip: the list keeps every value, but this algorithm only needs the last two.
> A version that keeps just two values uses constant memory:
>
> ```python
> def fibonacci(n: int) -> int:
>     """Return the nth Fibonacci number, keeping only two values"""
>     a, b = 0, 1
>     for _ in range(n):
>         a, b = b, a + b
>     return a
> ```

---
