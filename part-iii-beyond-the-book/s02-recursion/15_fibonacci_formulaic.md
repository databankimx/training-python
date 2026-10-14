## Any Other Options?

There's a mathematical formula to compute an approximation of a Fibonacci
number, that will allow us to reduce the number of operations to just a few
calculations, where the number of computations doesn't increase at all as
*n* gets larger.

> Warning: Because this computes an approximation for any `n > 50`, the 
> returned answer may be incorrect, so only use this for relatively small
> values of *n*.

Formulae:  
`φ = (1 + √5) / 2` (φ is the golden ratio)  
`F(n) = (φⁿ - (1-φ)ⁿ) / (φ - (1-φ))`  (φ is used in calculating F(n))

---

### The Code

```python
from count_calls import CountCalls

PHI = (1 + 5 ** 0.5) / 2

@CountCalls
def fibonacci(n):
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    return int((PHI ** n - (1 - PHI) ** n) / (PHI - (1 - PHI)))
```

As before, we'll test this algorithm with the same value: `n = 40`

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

Even though we're only making one call, we're still doing the a similar 
amount of work (since the loop iterates *n* times), but it does eliminate
recursion.

---
