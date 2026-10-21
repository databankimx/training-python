## Working with Global Variables

Global variables cause a lot of confusion, mostly because Python has a few rules about them that aren't obvious until something surprises you.

Global variables can simplify things when many functions need the same data. Before you rely on them, though, you need to know how Python treats names inside a function, or you'll spend an afternoon wondering why your change didn't stick.

The code for this lesson is in `15_bonus_global_variables.py`. It turns off a few Pylint warnings on purpose, because the lesson is about breaking the rules in a controlled way. Those comments stay in the code file, so you'll see them there rather than here.

---

### Accessing a Global Variable

If we only read a global variable, meaning we don't try to change it, we can use its name directly inside a function.

```python
adj = "awesome"

def use_global(use_adv: bool=False) -> None:
    """Use a global variable"""
    infix = f"{adv} " if use_adv else ""
    print(f"Python is {infix}{adj}\n")
```

Calling `use_global()` with the default `use_adv=False` prints:

```
Python is awesome
```

Notice that `adv` appears in the function, but it only gets evaluated when `use_adv` is `True`. That detail matters later.

---

### Modifying a Global Variable

Reading a global is easy. Changing one is where things get tricky.

#### A Failed Attempt to Modify a Global Variable

```python
adj = "awesome"

def try_to_modify_global() -> None:
    """Try (and fail) to modify a global variable"""
    adj = "fantastic"
    print(f"Python is {adj}")
```

Calling `try_to_modify_global()` prints:

```
Python is fantastic
```

But the global `adj` hasn't changed. When we assign a value to a name inside a function, Python creates a local variable with that name, even if a global of the same name already exists. The function's `adj` is a brand-new variable that disappears when the function ends, and the global `adj` is untouched.

That's the whole trick. Assignment inside a function creates a local by default.

---

#### Using the `global` Keyword to Modify a Global Variable

To change a global from inside a function, declare it first with the `global` keyword. That tells Python, "Don't create a local. I mean the one at the top of the file."

```python
adj = "awesome"

def modify_global() -> None:
    """Modify a global variable"""
    global adj
    adj = "super"
    print(f"Python is {adj}")
```

Calling `modify_global()` prints:

```
Python is super
```

Now the assignment changes the global itself. Any later call to `use_global()` will see the new value.

---

### Creating a Global Variable

The same `global` keyword lets a function create a brand-new global variable that didn't exist before.

```python
def create_global() -> None:
    """Create a global variable"""
    global adv
    adv = "really"
    print(f"Python is {adv} {adj}")
```

Calling `create_global()` prints:

```
Python is really super
```

Once `create_global()` has run, `adv` exists at the module level, so `use_global(use_adv=True)` can use it. Before that, calling `use_global(use_adv=True)` would raise a `NameError`. That's why the code in `main()` only passes `use_adv=True` after `create_global()` has run.

---

### Bonus: Using `nonlocal` with Nested Functions

Python also lets you define a function inside another function. When the inner function needs to change a variable belonging to the outer function, use `nonlocal`. It works like `global`, except it points at the enclosing function's variable instead of the module's.

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
    print(f"Outer: x = {x}, y = {y}\n")
```

Calling `use_nonlocal()` prints:

```
Outer: x = 1, y = 1
Inner: x = 2, y = 2
Outer: x = 2, y = 1
```

Because `inner()` declares `x` as `nonlocal`, its change reaches the outer function. The `y = 2` line in `inner()` has no `nonlocal` declaration, so Python creates a new local `y` for `inner()`, and the outer `y` stays at 1.

---

### Running the Whole Lesson

The code file calls each function in order from `main()`:

```python
def main() -> None:
    """Main function"""
    use_global()
    try_to_modify_global()
    use_global()
    modify_global()
    use_global()
    create_global()
    use_global(use_adv=True)
    use_nonlocal()

if __name__ == "__main__":
    main()
```

Running the file prints:

```
Python is awesome

Python is fantastic
Python is awesome

Python is super
Python is super

Python is really super
Python is really super

Outer: x = 1, y = 1
Inner: x = 2, y = 2
Outer: x = 2, y = 1
```

Read the output from top to bottom. The `fantastic` line comes and goes without touching the global. The `super` change sticks from then on. The `really` only appears once `create_global()` has made `adv` exist.

---

### Summary

- Reading a global from a function is fine.
- Assigning to a name inside a function creates a local, unless you declare it `global` first.
- Use `global` to change or create a module-level variable.
- Use `nonlocal` to change a variable in an enclosing function.
