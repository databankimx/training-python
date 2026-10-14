## What is Recursion?

Recursion occurs when a function calls itself. That may sound weird, but there
are many scenarios where a recursive algorithm is the most sensible approach to a problem, including:

* Sorting Algorithms
* Traversing Complex Data Structures Like Trees  
  and famously...
* The Fibonacci Sequence (ooh... foreshadowing)

---

### A Couple of Warnings about Recursion

As developers, we need to be careful how we structure a recursive function for
two main reasons:

1. Function calls get costly in terms of memory and CPU usage when we make a
   lot of them.
2. In Python, there is a maximum number of calls that can be on the recursion
   stack at a given time. By default, this is `1000`, and we can check the
   max recursion depth with the following code:

```python
import sys

print(f"Max recursion depth: {sys.getrecursionlimit()}")
```

Output:

```
Max recursion depth: 1000
```

---

We can change this value using the `sys.setrecursionlimit()` function, but
I recommend against this. If your recursive algorithm requires a depth of more
than 1000, you should redesign the algorithm, not the environment.

---

### Recursion Overflow

You must include in your function some condition that ends the recursion.
As you'll see in later lessons, we typically call this a *base case* (that
is, some condition where the function returns normally instead of calling
itself).

If you exceed the maximum recursion depth, your program will raise a
`RecursionError` exception.

Consider the code below, which lacks a base case. When executed, this function
will attempt to recurse forever (until the recursion stack is exhausted).

```python
def recursion_overflow() -> None:
    """Demonstrates exceeding max recursion depth"""
    recursion_overflow()

recursion_overflow()
```

Output:

```
Traceback (most recent call last):
  ... -- SNIP --

  File "...\01_recursion.py", line 4, in recursion_overflow
    recursion_overflow()
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
```

---

### A Little Setup

I have provided a special class known as a decorator in the following:

<details>
<summary>The CountCalls Class</summary>
<br>

In [count_calls.py](./count_calls.py)

```python
class CountCalls:
    """Class to allow counting the times a recursive function is called"""

    def __init__(self, func: callable):
        """Initialize"""
        self._count = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        """Magic method override to add to counter and execute function"""
        self._count += 1
        return self._func(*args, **kwargs)
    
    @property
    def call_count(self):
        """Number of times the recursive function has been called"""
        return self._count
```

</details>
<br>

This class can be applied to any recursive function as a decorator as follows,
giving the function a property `call_count` that represents the number of 
times the function was called while processing the recursive algorithm.

```python
from count_calls import CountCalls

@CountCalls
def recursive_function():
    ...

count = recursive_function.call_count
```

---
