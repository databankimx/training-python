## Tracing Recursive Calls

To understand how recursive calls can pile up on the stack, we can add a
bit of trace logging to our `factorial()` function:

```python
def factorial(n: int) -> int | None:
    """Calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    
    print(f"factorial({n}) called...")
    f = 1 if n < 2 else n * factorial(n - 1)
    print(f"factorial({n}) returns {f}...")
    return f
```

We can assume that before the function is called, the recursion stack is
empty.

Each time our function is called, it can either return a value or call itself,
and each call adds one instance to the recursion stack.

Using the two logging lines we've added, we can keep track of the stack count
`s` with two simple rules:

* When we print "factorial(*n*) called..." `s = s + 1`
* When we print "factorial(*n*) returns *f*..." `s = s - 1`

---

### Testing

Let's run a small test:

```python
n = 5
print(f"\n{n}! = {factorial(n)}")
```

Output:

```
factorial(5) called...
factorial(4) called...
factorial(3) called...
factorial(2) called...
factorial(1) called...
factorial(1) returns 1...
factorial(2) returns 2...
factorial(3) returns 6...
factorial(4) returns 24...
factorial(5) returns 120...

5! = 120
```

You can see that until we reach the base case `factorial(1)` we only add
calls to the stack, and after that, we remove them in the reverse order.

Based on this, we know that this function will place *n* recursive calls on 
the stack, and since we know that the maximum stack depth is 1,000, we know
that this function cannot handle any *n* greater than 999.

Given that Python is specifically designed to handle very large integers, this
suggests that even though we exactly patterned the real-world formula, our
recursive implementation is not a good design for this purpose.

---
