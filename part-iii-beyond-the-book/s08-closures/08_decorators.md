## Decorators

One especially powerful use of closures is the creation of function 
decorators.

A decorator is a function that takes in another function (and its arguments),
performs some tasks, and then executes the passed function (and potentially
performs additional tasks after it executes).

---

### Example

As an example, let's create a decorator that reports the function's arguments
as a debugging task.

```python
def debug(func: callable) -> callable:
    """Print out debug information when another function is called"""

    def _debug(*args, **kwargs):
        """Inner function to perform the work on the decorated function"""
        result = func(*args, **kwargs)
        print(f"{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}")
        return result

    return _debug
```

The `debug()` function accepts a callable function as its sole parameter.

It then creates and returns a closure that executes its passed function while
logging the function arguments.

---

### Usage and Testing

We can now wrap a function in a decorator using this syntax:  
`new_func = decorator_name(function)`

```python
def sum(a: int, b: int) -> int:
    """Sum two numbers"""
    return a + b

total = debug(sum)

total(1, 2)
total(3, b=4)
```

... we'll see the debug information along with the function results.

Output:

```
sum(args: (1, 2), kwargs: {}) -> 3
sum(args: (3,), kwargs: {'b': 4}) -> 7
```

---

#### Decorating with `@`

Alternately, we simply add `@decorator_name` to the definition of any 
function.

```python
@debug
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

And now, when we call the decorated function...

```python
add(5, 6)
add(7, b=8)
```

... we'll see the debug information along with the function results.

Output:

```
add(args: (5, 6), kwargs: {}) -> 11
add(args: (7,), kwargs: {'b': 8}) -> 15
```

---

### Real-World Example: Timer

One place where I like to use a decorator function is when I want to time
how long a function takes to complete its work.

To do this, I create a decorator function that reports the execution time
like this:

```python
import timeit

def timer(func: callable) -> callable:
    """Time the execution of a decorated function"""

    def _timer(*args, **kwargs):
        """Write out elapsed time of function execution"""
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        end = timeit.default_timer()
        delta = end - start

        if delta > 60: ex_time = f"{int(delta // 60)} m : {round(delta % 60, 4)} s"
        elif delta * 1_000_000 < 1: ex_time = f"{round(delta * 1_000_000_000, 4)} ns"
        elif delta * 1_000 < 1: ex_time = f"{round(delta * 1_000_000, 4)} µs"
        elif delta < 1: ex_time = f"{round(delta * 1000, 4)} ms"
        else: ex_time = f"{round(delta, 4)} s"        
        print(f"Execution Time: {ex_time}")

        return res
    
    return _timer
```

---

#### Using the Timer Function

Let's test this using our `fibonacci()` function from the recursion topic.

```python
def fibonacci(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]
```

Since that's a recursive function, and we don't want to time each call separately, we'll create a wrapping function to use the `@timer` decorator.

```python
@timer
def run_fibonacci(n: int) -> int:
    """ Wrap the fibonacci call with a timer"""
    return fibonacci(n)
```

Now, calling `run_fibonacci()` ...

```python
n = 50
print(f"F({n}) = {run_fibonacci(n):,}")
```

... gives us this:

Output:

```
Execution Time: 30.3 µs
F(50) = 12,586,269,025
```

Pretty cool...

---

### Chaining Decorators

You can stack two decorators on a single function to chain their results,
with the decorators executing in the reverse order in which they are applied.

```python
@timer
@debug
def run_fibonacci(n: int) -> int:
    """ Wrap the fibonacci call with a timer"""
    return fibonacci(n)

n = 50
print(f"F({n}) = {run_fibonacci(n):,}")
```

Output:

```
run_fibonacci(args: (50,), kwargs: {}) -> 12586269025
Execution Time: 347.8 µs
F(50) = 12,586,269,025
```

---
