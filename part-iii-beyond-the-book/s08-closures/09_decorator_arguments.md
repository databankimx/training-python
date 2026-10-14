## Decorator Arguments

We can even design decorators that accept arguments.

---

### Example

Let's modify the `power()` function from our first closure example:

```python
def power(exp: int) -> callable:
    """Generates a decorator (applying a non-local value for the exponent)"""
    def _power(func: callable) -> callable:
        """Calls the inner function, passing the function to execute"""
        def _inner_power(*args: list[int]) -> int:
            """Executes the called function, modifying its value n to be n ** exp"""
            base = func(*args)
            return base ** exp
        return _inner_power
    return _power
```

We've wrapped an additional outer function layer around the original function.
This allows us to accept the exponent as an argument in the decorator.

---

### Usage

Here, instead of storing the closure in a variable, we'll use it to decorate 
another function definition.

```python
@power(2)
def square(n: int) -> int:
    """Square an integer (using a decorator function)"""
    return n

@power(3)
def cube(n: int) -> int:
    """Cube an integer (using a decorator function)"""
    return n
```

Note how the functions just return `n` without performing a computation. 
This is because the decorator's closure `_inner_power()` is doing the math.

---

### Testing

Let's test the functions:

```python
for n in range(1, 6):
    print(f"{n}² = {square(n):>2} : {n}³ = {cube(n):>3}")
```

Output:

```
1² =  1 : 1³ =   1
2² =  4 : 2³ =   8
3² =  9 : 3³ =  27
4² = 16 : 4³ =  64
5² = 25 : 5³ = 125
```

Now that's some powerful programming!

---

### Additional Arguments

We can also pass and perform work on additional arguments to the inner 
function:

Let's create a decorator to protect against division by zero:

```python
def smart_divide(func: callable) -> float|None:
    """Decorator to protect against division by zero"""
    def inner(a, b):
        print(f"I am going to divide {a} by {b}")
        if b == 0:
            print("Whoops! cannot divide by zero")
            return None
        return func(a, b)
    return inner
```

Then we can call a decorated function...

```python
@smart_divide
def divide(a: int, b: int) -> float:
    """Perform division (protected by decorator)"""
    return a / b

for tup in [(2, 5), (2, 0)]:
    x, y = tup
    z = divide(x, y)
    if z: print(f"Returned {z}")
    print()
```

Output:

```
I am going to divide 2 by 5
Returned 0.4

I am going to divide 2 by 0
Whoops! cannot divide by zero
```

---
