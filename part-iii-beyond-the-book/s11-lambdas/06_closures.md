## Using a Lambda in a Closure

A closure is a function that keeps references to variables from its enclosing
scope, so it can still use them after the outer function has returned.

In effect, a closure carries its environment with it, so it can be called after
the outer function has finished, wherever it has been passed.

---

### Traditional Closure

We've seen in the [Closures](../s08-closures/05_closures.md)
lesson how to construct a closure using a traditional function:

```python
from collections.abc import Callable

def outer_func_function(x: int) -> Callable:
    y = 4
    def inner_func(z: int) -> int:
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func_function(i)
    print(f"closure({i + 5}) = {closure(i + 5)}")
```

Output:

```
closure(5) = 9
closure(6) = 11
closure(7) = 13
```

---

### Lambda Closure

But there's no reason that a closure cannot be a lambda instead. Here is
the same closure reworked to return a lambda instead of a traditional
function.

```python
from collections.abc import Callable

def outer_func_lambda(x: int) -> Callable:
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func_lambda(i)
    print(f"closure({i + 5}) = {closure(i + 5)}")
```

Output:

```
closure(5) = 9
closure(6) = 11
closure(7) = 13
```

---
