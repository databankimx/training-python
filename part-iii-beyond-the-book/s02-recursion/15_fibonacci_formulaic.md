## Any Other Options?

There's a mathematical formula to compute a Fibonacci number directly, without
computing the earlier terms. It reduces the work to a few calculations, and the
number of operations doesn't grow with *n*.

> Warning: this formula uses floating-point arithmetic, and the rounding error
> grows as *n* gets larger. For large values of *n*, the answer can be wrong.
> Check the result against the iterative version before you trust it.

Formulae:  
`φ = (1 + √5) / 2` (φ is the golden ratio)  
`F(n) = (φⁿ - (1-φ)ⁿ) / (φ - (1-φ))`  (φ is used in calculating F(n))

---

### The Code

```python
from count_calls import CountCalls

PHI = (1 + 5 ** 0.5) / 2

@CountCalls
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    return round((PHI ** n - (1 - PHI) ** n) / (PHI - (1 - PHI)))
```

We use `round()` rather than `int()`. The formula's result should be very close to
a whole number. `int()` truncates, so a result that falls just below the true
value would give one less than the correct answer. `round()` picks the nearest
whole number, which is what we want here.

As before, we'll test this algorithm with the same value: `n = 40`

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

Even though we're only making one call, the formula still relies on
floating-point arithmetic, which becomes approximate for large *n*. It does
eliminate recursion entirely.

---
