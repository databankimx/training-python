## A Naive Fibonacci Algorithm

Because its formula is already expressed in recursive terms, we can easily
create an algorithm where we simply translate the formula into code:

---

### The Code

```python
from count_calls import CountCalls

@CountCalls
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (naive algorithm)"""
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

We'll test our code on a relatively challenging number (for this algorithm
anyway): `n = 40`

```python
n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

> **Warning:** This code can take several minutes to run, depending on your
> computer. Run it only when you're ready to wait.

Output:

```
Calculated F(40) = 102,334,155
call_count = 331,160,281
```

It took a long time, and over 300 million recursive calls, to compute
`F(40) = 102,334,155`.

Why did it take so long?

---

### Wasted Recursive Calls

The big problem is that we made the exact same calculations many times. Let's
take a look at a simpler example `F(5)` and see where the wasted calls come 
in.

Only when `n < 2` does a call return a value without spawning additional
calls.

The initial call spawns two recursive calls

* `F(5) = F(4) + F(3)` (+2 calls)

Each of those two calls spawns two more

* `F(4) = F(3) + F(2)` (+2 calls)
* `F(3) = F(2) + F(1)` (+2 calls)

Looking at those four new calls, only one immediately resolves:

* `F(3) = F(2) + F(1)` (+2 calls)
* `F(2) = F(1) + F(0)` (+2 calls)
* `F(2) = F(1) + F(0)` (+2 calls)
* `F(1) = 1`

Then, we have to resolve six additional calls:

* `F(2) = F(1) + F(0)` (+2 calls)
* `F(1) = 1`
* `F(1) = 1`
* `F(0) = 0`
* `F(1) = 1`
* `F(0) = 0`

We still have two more calls:
* `F(1) = 1`
* `F(0) = 0`

Looking at all of the resolved calls, we get:  
`F(5) = 1 + 1 + 1 + 0 + 1 + 0 + 1 + 0 = 5`

And it took us 15 calls to the function to figure that out, but when we list
out the values of *n* passed to the function and how many times each was
passed, we see:

|*n*|calls|
|:-:|:-:|
|5|1|
|4|1|
|3|2|
|2|3|
|1|5|
|0|3|

We calculated `F(3)` twice, and `F(2)` three times, and so on.

We're wasting calls recalculating values we've already computed, and that
problem gets more severe the larger *n* becomes.

The number of calls grows exponentially. For this algorithm, the number of calls
for `F(n)` is `2 × F(n+1) - 1`. Since Fibonacci numbers grow by a factor of about
1.618 each step, that's roughly `1.618ⁿ` calls. A check against the output above:
`2 × F(41) - 1 = 2 × 165,580,141 - 1 = 331,160,281`.

Surely we can do better...

---
