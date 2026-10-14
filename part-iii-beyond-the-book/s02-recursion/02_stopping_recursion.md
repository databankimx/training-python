## Stopping Recursion

A recursive pattern must be designed such that it will eventually stop making 
recursive calls.

A typical pattern includes the following:

* One or more *base cases* that are directly resolvable without the 
  need for further recursion.
* Logic such that each recursive call moves the solution progressively closer 
  to one of these base cases.

---

### Example

Consider this recursive function:

```python
from time import sleep

def countdown(n: int) -> bool:
    """Counts down to zero"""
    if n < 0:
        print("Cannot count down from a negative number!")
        return False
    if n == 0:
        print("Liftoff!")
        return True
    print(n)
    sleep(0.5)
    return countdown(n - 1)
```

Here, we have two base cases:

* When `n` is negative, we identify an error case and immediately return
  `False` without further recursion.
* When `n` is zero, we identify the success case and immediately return
  `True` without further recursion.

In the condition where `n > 0` we make a recursive call, but we decrement `n`,
while progresses us towards the base case of `n == 0`.

---

### Testing

That meets both criteria for our standard pattern, so this function should eventually stop.

We can test it with code like this:

```python
# -- SNIP --

n = 3
if countdown(n):
    print("\nrecursions complete...")
else:
    print("\nrecursions failed!")
```

Output:

```
3
2
1
Liftoff!

recursions complete...
```

As expected, we reach the base case, and the recursion halts.

---

### Vulnerabilities

I intentionally selected a small value `n = 3` for this.

What would happen if I wanted to count down from `n = 3_000` instead?

```python
# -- SNIP --

n = 3_000
if countdown(n):
    print("\nrecursions complete...")
else:
    print("\nrecursions failed!")
```

Output:

```
3000
2999

-- SNIP --

2006
2005
Traceback (most recent call last):

-- SNIP --
[Previous line repeated 992 more times]
  File "...\02_stopping_recursion.py", line 11, in countdown
    print(n)
RecursionError: maximum recursion depth exceeded while calling a Python object
```

Even though we have a base case and progressively move toward it, our 
algorithm is poorly designed for large numbers.

We would probably be better off using an iterative algorithm with a loop 
instead of recursion for this task.

> Rule of thumb:
> 
> If a recursive design will fail for some reasonably sized input value, 
> then you should probably either:
>
> * Improve the algorithm  
>   or
> * Not use recursion at all

---
