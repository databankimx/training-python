## Real-World Example: Iteratively Computing a Factorial

For any recursive solution, there is at least one alternative means of solving
the same problem iteratively (using a loop instead of recursion).

As programmers, this means that we should not assume that a recursive solution
is desireable just because it is feasible.

---

### Our `factorial()` Function without Recursion

Here's an example of how we could code our `factorial()` function using an
iterative algorithm instead of recursion.

```python
def iterative_factorial(n: int) -> int:
    """Calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
```

See how we implement a loop to handle the repeated multiplication rather than
a function call.

---

### Testing

Let's test the function:

```python
for n in range(10):
    print(f"{n}! = {factorial(n)}")
```

Output:

```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
```

We got exactly the same results as we did from our recursive function, so it
appears we've solved the same problem.

---

### Why Change It?

Given that we've only solved the same problem, why should we change this from
the recursive solution to an iterative one?

Well, the answer is that we can run this:

```python

```

Output:

```
4027896473371708673172461363569269897050 --SNIP-- 000
```

This 2,571-character monster proves that we can use our iterative algorithm
for numbers greater than we are able to support using our recursive approach.

---
