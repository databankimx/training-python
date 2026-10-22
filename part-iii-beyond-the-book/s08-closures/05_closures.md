## Closures

Closures are a powerful but underused feature of many programming 
languages including Python.

A closure is a dynamically generated function created and returned by 
another function.

What makes a closure particularly powerful is that it captures the 
environment in which it was generated. This means that a closure has access to
the locally scoped free variables* from its outer function even after that
function has finished executing.

\* A *free* variable is a name that an inner function uses but that belongs to
an enclosing function's scope. It isn't one of the inner function's own parameters
or local variables.

> Formal Definition:  
> A closure is a persistent local variable scope (the combination of a 
> function  bundled together (enclosed) with references to its surrounding 
> state (the lexical environment)).

---

### Defining a Closure

In Python, functions are first-class objects, which means that they can be
passed to and returned from functions.

When you return an inner function object, the interpreter packs the function 
along with its containing environment or closure.

The function object keeps references to the enclosing variables that it uses. It
doesn't keep a copy of everything in the containing scope.

To define a closure, you need to take three steps:

1. Create an inner function.
2. Reference variables from the enclosing function.
3. Return the inner function.

As an example, we will create a function that will generate closures that
raise a given value to a static power (defined by the outer function).

```python
from collections.abc import Callable

def generate_power(exponent: int) -> Callable:
    """Closure factory (creates a new closure each time it is called)"""
    def power(base: int) -> int:
        """Inner function will be created with the exponent known"""
        return base ** exponent
    return power
```

Notice how the inner `power()` function captures the `exponent` parameter from
the outer function.

---

### Instantiating and Using a Closure

We can create an instance of the closure and test it like this:

```python
squared = generate_power(2)
for n in range(1, 6):
    print(f"{n}² = {squared(n)}")
```

Output:

```
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
```

---

### Multiple Closures

The outer function can be used to generate multiple closures. Each call to
`generate_power()` creates its own `exponent` variable, so each closure has its own
value.

The code file calls `squared()`, then `cubed()`, then `squared()` again, printing a
heading before each set of results. The headings are left out of the output here:

```python
squared = generate_power(2)
for n in range(1, 6):
    print(f"{n}² = {squared(n)}")

cubed = generate_power(3)
for n in range(1, 6):
    print(f"{n}³ = {cubed(n)}")

for n in range(1, 6):
    print(f"{n}² = {squared(n)}")
```

Output:

```
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
1³ = 1
2³ = 8
3³ = 27
4³ = 64
5³ = 125
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
```

Generating the `cubed()` closure doesn't affect `squared()`. The two closures
refer to different `exponent` variables, each created by a separate call to
`generate_power()`.

The closure refers to the variable, not to a fixed copy of its value. So if the
outer function's variable changed later (through `nonlocal`, for example), the
closure would see the change.

---
