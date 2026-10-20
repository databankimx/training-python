## Decorating a Lambda

We saw in the section covering closures that we can create a decorator
function that wraps another function in some additional work.

For example:

```python
def trace(func: callable) -> callable:
    def _trace(*args, **kwargs):
        print(f"[TRACE] func: {func.__name__}, args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return _trace
```

If we want to decorate some other function with this functionality, we
would indicate it like this:

```python
@trace
def add_two(x: int) -> int:
    return x + 2

print(add_two(3))
```

Output:

```
[TRACE] func: add_two, args: (3,), kwargs: {}
5
```

However, we don't have to decorate a function. We could instead pass a
lambda to the decorator function.

---

### Calling a Decorator with a Lambda

Here, we'll pass a simple lambda to the decorator function:

```python
print((trace(lambda x: x + 2))(3))
```

Output:

```
[TRACE] func: <lambda>, args: (3,), kwargs: {}
5
```

---
### Calling a Decorator with a Higher-Order Function and Lambda

We can also use the decorator function to trace the behavior of a lambda 
that is used by a higher-order function.

```python
print(list(map(trace(lambda x: x * 2), range(3))))
```

Output:

```
[TRACE] func: <lambda>, args: (0,), kwargs: {}
[TRACE] func: <lambda>, args: (1,), kwargs: {}
[TRACE] func: <lambda>, args: (2,), kwargs: {}
[0, 2, 4]
```

---
