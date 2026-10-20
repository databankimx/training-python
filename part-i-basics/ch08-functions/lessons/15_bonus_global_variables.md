## Working with GLobal Variables

There can often be confusion about how we work with global variables in
Python.

While global variables are often useful for simplifying function signatures
where many functions use the same data, we need to understand how they work
in order to implement them effectively.

---

### Accessing a Global Variable

If we only use a global variable (that is, we're not attempting to modify
its value), we can simply access the global variable by name.

```python
adj = "awesome"

def use_global() -> None:
    """Use a global variable"""
    print(f"Python is {adj}") 

use_global()
```

Output:

```
Python is awesome
```

---

### Modifying a Global Variable

However, when we're modifying a global variable, it's not as straightforward

#### A Failed Attempt to Modify a Global Variable

```python
adj = "awesome"

def use_global() -> None:
    """Use a global variable"""
    print(f"Python is {adj}") 

def fail_modify_global() -> None:
    """Fail to modify a global variable"""
    adj = "fantastic"
    print(f"Python is {adj}")

fail_modify_global()
use_global()
```

Output:

```
Python is fantastic
Python is awesome
```

When we assign a value to a variable name in a function, Python's default
behavior is to create a local variable, even if a global of the same name
exists.

So when we assign the new value `"fantastic"` to the variable `adj`, it is
assigned to a local variable, and when we call the global again, it has not
been modified.

---

#### Using the `global` Keyword to Modify a Global Variable

In order to access and modify a global variable from within a function, we
must first locally declare the variable using the `global` keyword.

```python
adj = "awesome"

def use_global() -> None:
    """Use a global variable"""
    print(f"Python is {adj}") 

def modify_global() -> None:
    """Modify a global variable"""
    global adj
    adj = "super"
    print(f"Python is {adj}")

modify_global()
use_global()
```

Output:

```
Python is super
Python is super
```

Now, when we assigned the value to a variable declared as `global`, it did
modify the global variable itself.

---

### Creating a Global Variable

We can also create a completely new global variable from within a function
using the same `global` syntax we used when modifying an existing global.

```python
adj = "awesome"

def use_global() -> None:
    """Use a global variable"""
    if adv:
        print(f"Python is {adv} {adj}") 
    else:
        print(f"Python is {adj}") 

def create_global() -> None:
    """Create a global variable"""
    global adv
    adv = "really"
    print(f"Python is {adv} {adj}")

create_global()
use_global()
```

Output:

```
Python is really super
Python is really super
```

---

### Bonus: Using `nonlocal` with Nested Functions

We haven't discussed nested functions yet, but Python supports declaring
functions within a function.

When a variable is declared in an outer function, we can access it from an
inner function using the `nonlocal` keyword.

```python
def use_nonlocal(x: int=1, y: int=1) -> None:
    """Use a nonlocal variable"""
    print(f"Outer: x = {x}, y = {y}")
    def inner():
        nonlocal x
        x += 1
        y = 2
        print(f"Inner: x = {x}, y = {y}")
    inner()
    print(f"Outer: x = {x}, y = {y}")

use_nonlocal()
```

Output:

```
Outer: x = 1, y = 1
Inner: x = 2, y = 2
Outer: x = 2, y = 1
```

In the inner function, we declared `x` as `nonlocal`, so when we modified
its value, it modified the value in the outer function.

However, when we set the value of y in the inner function, it had no effect
on the outer `y` value, because we did not declare it as `nonlocal`, so it
was scoped locally to the inner function.

---
