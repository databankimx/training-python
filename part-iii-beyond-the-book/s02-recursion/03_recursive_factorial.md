## Real-World Example: Recursively Computing a Factorial

A factorial (denoted as *n*!) is defined thus:

The product of all numbers from 1 to n (inclusive), given that n is 
non-negative.  
n! = 1 * 2 * 3 * ... * n (where 0! is defined as 1)

We can break this down into three cases:

* 0! = 1
* 1! = 1
* n! = n * (n - 1)!    for n > 1

Since the first two cases return the same value, we can treat them as a
single base case:  
0 <= n < 2

Since the remaining case can use a term `(n - 1)!` that moves toward the base
case, we have an obvious candidate for a recursive solution.

---

### Coding the Recursive Factorial Function

Here is an example of how we would code the recursive function:

```python
def factorial(n: int) -> int | None:
    """Calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)
```

We've accounted for the error case and base case with immediate returns and 
then mimicked the formula to provide a recursive path to iterate `n` toward
the base case, so we've met the criteria for our standard pattern.

> Note: This is by no means the most efficient method to compute a factorial,
> and it's vulnerable to the same issue where we'll overflow the recursion
> limit for any n > 1000. It's just an example of translating a recursive
> formula into a recursive Python function.

---

### Testing

We can test our code like this:

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

---
