## Comparing Performance

> When you assume that your approach is the correct one without testing,
> you're always wrong.  
> &nbsp;&nbsp;&nbsp;&nbsp;~me

From our small battery of test cases, it's impossible to identify the best
choice. Yes, our iterative approach allowed us to deal with numbers larger
than our recursive algorithm, but that doesn't mean it performs better.

What if, for the numbers it supports, the recursive algorithm is faster?

> Spoiler: It's not

But what if it was? How would we know?

Unlike typical testing, performance requires us to compute how long it takes
to arrive at a solution, not just that the solution is correct.

For factorial computation, let's compare four approaches:

* Our recursive algorithm
* Out iterative algorithm
* An algorithm that uses `functools.reduce()`
    * We did not cover this, but when you search for options to recursive
      functions, you'll run into it as a common approach
* Python's `math.factorial()` function

See [comparing_performance.py](./06_comparing_performance.py) for full code 
including all algorithms and test script.

---

### The Algorithms

#### Recursive

For recall, here is our recursive algorithm:

```python
def factorial_rec(n: int) -> int | None:
    """Recursively calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    if n < 2:
        return 1
    return n * factorial_rec(n - 1)
```

---

#### Iterative

For recall, here is our iterative algorithm:

```python
def factorial_iter(n: int) -> int | None:
    """Iteratively calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
```

---

#### Using `functools.reduce()`

Here is an implementation leveraging the `reduce()` function from the
`functools` library

```python
from functools import reduce

def factorial_red(n: int) -> int | None:
    """Calculate the factorial of n using `reduce()`"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
```

---

#### Using `math.factorial`

Here is an implementation leveraging the built-in `factorial()` function from the `math` library

```python
def factorial_def(n: int) -> int | None:
    """Calculate the factorial of n using `math.factorial()`"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    return factorial(n)
```

---

### Timing the Tests

What we need to do is to test each function calculating the same value a
large number of times (to ensure we get a valid average rather than a one-off
very slow or very fast result).

We could just independently call each function, checking the time before and
after, but that would be a lot of redundant code, so let's create a function
that takes our functions as an argument and performs the tests.

```python
from time import perf_counter_ns

def check_performance(func: callable, n: int, r: int) -> int:
    """Evaluate how long it takes to calculate n! r times"""
    start = perf_counter_ns()
    for _ in range(r):
        func(n)
    end = perf_counter_ns()
    return end - start
```

For this purpose, I have chosen to use the `time.perf_counter_ns()` function,
since nanosecond resolution should be more than enough accuracy for this
comparison.

Each time you call `perf_counter_ns()` it provides the current time to
nanosecond precision, so the duration necessary for our repeated tests is
just the time at the start subtracted from the time at the end.

---

### Testing

Now, to test the code, we'll need to select a value to compute, a number of 
times to test, and which function to run. In Python, all function are
first-class objects, so we can easily pass them as variable.

Here's my testing code:

> Note, we're dividing the duration by a billion in order to convert
> nanoseconds to seconds.

```python
n = 10
repeat = 1_000_000
functions = {
    "Recursive": factorial_rec,
    "Iterative": factorial_iter,
    "Using functools.reduce()": factorial_red,
    "Using math.factorial()": factorial_def
}
    print(f"Testing {n}! {repeat:,} times for each algorithm...")
for name, func in functions.items():
    dur = check_performance(func, n, repeat) / 1_000_000_000
    print(f"\n{name}:\n{dur} sec")
```

Output:

```
Testing 10! 1,000,000 times for each algorithm...

Recursive:
1.0567457 sec

Iterative:
0.5848271 sec

Using functools.reduce():
0.8232688 sec

Using math.factorial():
0.0436922 sec
```

---

### Conclusions

It turns out that our iterative function is about twice as fast as our
recursive function and measurably faster than the `reduce()` alternative as
well.

That said, it's clear that it's pretty inefficient overall, since Python's
`math.factorial()` is more than ten times faster.

That's because the `math.factorial()` method is:

1. A very well optimized algorithm based on decades of research
2. Implemented in C, not in Python itself

Ignoring that, however, since most problems we solve won't be (or at least
shouldn't be) ones for which Python has ready-made functions, we can conclude
that our iterative approach is the best of the implementations we tried.

That doesn't make it the best possible algorithm, just the best we tested.

But the important thing is that we can say that on the basis of performance
testing, not because we assumed it would be the best.

---
