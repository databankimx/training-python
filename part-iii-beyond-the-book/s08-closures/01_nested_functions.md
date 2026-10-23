## Nested Functions

Inner functions, also known as nested functions, are functions 
that you define inside other functions.

In Python, this kind of function can read variables and names defined in the
enclosing function. The inner function sees the enclosing function's scope (its
environment), so it can use those values without them being passed in. Assigning
to one of those variables needs the `nonlocal` keyword, which a later lesson covers.

Inner functions have many uses, most notably as closure factories and 
decorator functions.

---

### Simple Example

This is an oversimplified example, where the outer function simply declares
and executes the inner function.

```python
def outer_function() -> None:
    """Executes the inner function"""
    def inner_function() -> None:
        print("Hello World!\n")
    inner_function()

outer_function()
```

Output:

```
Hello World!

```

---

### Example With Variable in Scope

In this example, we'll pass a value to the outer function. Although it is not
passed in turn to the inner function, the inner function will still have 
access to the variable.

```python
def outer_function(name: str) -> None:
    """Executes the inner function (sharing variable 'name')"""
    def inner_function() -> None:
        print(f"Hello {name.title()}!\n")
    inner_function()

outer_function("Scott")
```

Output:

```
Hello Scott!

```

---

### Functions as Arguments (Delegates)

We can pass a function as an argument to another function in Python.

Since functions are first-class objects in Python, we can define a function
that takes another function as an argument. The `Callable` type hint comes from
`collections.abc`:

```python
from collections.abc import Callable

def calculate(func: Callable, x: int, y: int) -> int:
    """Calls the given function with the given arguments"""
    return func(x, y)
```

Let's assume we have an existing function like this:

```python
def add(x: int, y: int) -> int:
    """Adds two numbers"""
    return x + y
```

We can then execute the `add()` function by passing it to `calculate()`:

```python
x, y = 2, 3
z = calculate(add, x, y)
print(f"{x} + {y} = {z}\n")
```

Output:

```
2 + 3 = 5

```

---

### Functions as Return Values

Since we can pass a function as an argument, it stands to reason that we can
also return them from functions.

Here, we have a function that creates and returns another function. This
type of function (where the result retains the locally scoped variables) is
also called a *closure*, which the closures lesson covers in detail.

```python
from collections.abc import Callable

def greeting(name: str) -> Callable:
    """Returns a function that greets a user"""
    def hello() -> None:
        print(f"Hello {name.title()}!\n")
    return hello
```

We can now call the function to create a new function with a static `name` 
argument:

```python
hello_scott = greeting("Scott")
hello_scott()
```

Output:

```
Hello Scott!

```

---
