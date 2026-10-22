## Example: Computing a Factorial Iteratively

For any recursive solution, there is at least one alternative means of solving
the same problem iteratively (using a loop instead of recursion).

As programmers, this means that we should not assume that a recursive solution
is desirable just because it is feasible.

---

### Our `factorial()` Function without Recursion

Here's an example of how we could code our `factorial()` function using an
iterative algorithm instead of recursion.

```python
def iterative_factorial(n: int) -> int | None:
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
a function call. Because the loop doesn't add a new frame to the recursion
stack for each step, the recursion limit doesn't apply here.

---

### Running It

Let's test the function:

```python
for n in range(10):
    print(f"{n}! = {iterative_factorial(n)}")
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
print(iterative_factorial(1000))
```

> Note: this call is commented out in `main()` in the code file. Uncomment it
> to see the output below.

Output:

```
4023872600770937 --SNIP-- 000
```

This 2,568-digit monster proves that we can use our iterative algorithm
for numbers greater than we are able to support using our recursive approach.

Python integers aren't limited to a fixed size, so the result grows as large as
memory allows. The only real limit is how long the multiplication takes.

---
