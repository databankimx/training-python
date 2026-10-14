## Using an Inner Function to Limit Redundancy

In the section covering [recursion](../S02_Recursion/01_what_is_recursion.md),
we covered the computation of a factorial as an example of a recursive 
function defined thus:

```python
def factorial(n: int) -> int | None:
    """Calculate the factorial of n"""
    print(f"Validate input ({n})...")
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    print(f"factorial called with {n}...")
    if n < 2:
        return 1
    return n * factorial(n - 1)
```

This function is wasteful, since it validates the input every time it is
called.

```python
n = 5
print(f"{n}! = {factorial(n)}")
```

Output:

```
Validate input (5)...
factorial called with 5...
Validate input (4)...
factorial called with 4...
Validate input (3)...
factorial called with 3...
Validate input (2)...
factorial called with 2...
Validate input (1)...
factorial called with 1...
5! = 120
```

Realistically, we only need to validate the input number once, because after
that, we're just counting down to the base case.

How can we eliminate these redundant checks?

---

### Eliminate Redundant Checks with an Inner Function

If we move all of the recursive computation to an inner function, we can still
validate the input, but once validated, that step won't be called again:

```python
def factorial(n: int) -> int | None:
    """Calculate the factorial of n (n!)"""
    print(f"Validate input ({n})...")
    if not isinstance(n, int) or n < 0:
        print(f"Invalid input [{n}]! Must be a non-negative integer.")
        return None
    
    def inner_factorial(n: int) -> int:
        print(f"inner_factorial called with {n}...")
        if n < 2:
            return 1
        return n * inner_factorial(n - 1)
    
    return inner_factorial(n)
```

Using this we can test that our implementation is correct and only validates once:

```python
n = 5
print(f"{n}! = {factorial(n)}")
```

Output:

```
Validate input (5)...
inner_factorial called with 5...
inner_factorial called with 4...
inner_factorial called with 3...
inner_factorial called with 2...
inner_factorial called with 1...
5! = 120
```

---
