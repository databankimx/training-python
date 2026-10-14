## Using a Lambda in a Closure

A closure is a function where every free variable (everything except 
parameters) used in its outer function is bound to a specific value 
defined in the enclosing scope of that function.

In effect, closures define the environment in which they run, and so can 
be called from anywhere.

---

### Traditional Closure

We've seen in the [Closures](../S08_Closures/01_nested_functions.md)
topic how to construct a closure using a traditional function:

```python
def outer_func_function(x: int) -> callable:
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
def outer_func_lambda(x: int) -> callable:
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
