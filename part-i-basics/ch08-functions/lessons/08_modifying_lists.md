## Modifying Lists with Functions

We've already seen how to move or remove list items with loops in top-level code.

Moving that work into functions often makes the code more versatile.

---

### Mutable and Immutable Types

Other languages often distinguish between arguments passed *by value* (the function gets a copy) and
arguments passed *by reference* (the function gets the original). Python doesn't fit either label
neatly. When you pass an argument, the function gets a reference to the same object. What happens next
depends on whether that object can be changed.

If a type is *immutable*, the object can't be changed after it's created. You can replace what a name
points to, but you can't alter the object itself. When your code appears to change an immutable value,
Python creates a new object and points the name at it. The original object is untouched.

So if a function receives an immutable value, it has a reference to the same object as the caller, but
it can't change that object. The caller's value is safe.

The following types are immutable in Python, among others:

* `int`
* `float`
* `complex`
* `tuple`
* `str` (strings)
* `bytes`

Every other common type is *mutable*, meaning it can be changed in place. A list is mutable. When you
pass a list to a function, the function gets a reference to that same list. Changes made to the list
inside the function change the original list too.

---

### Lists Are Mutable

> **Important gotcha:** this section highlights a common surprise. A function that changes a list it
> was given changes the caller's list too, even though the function never returns it.

Because lists are mutable, work done inside a function that changes a list changes the original list in
the calling code.

Notice that the `print_models()` function below doesn't have a `return` statement:

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
```

After this code runs, the original lists have changed, even though `print_models()` doesn't return
anything:

```python
my_unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
my_completed_models = []

print_models(my_unprinted_designs, my_completed_models)
show_completed_models(my_completed_models)
print(my_unprinted_designs)
```

Output:

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
[]
```

At the end, when we print `my_unprinted_designs`, the list is empty.

---

### Making Copies to Protect the Original Data

To keep the function from changing the original list, pass it a copy instead. For a list, the simplest
way to make a copy is a slice with neither end specified: `my_list[:]`.

Here's the same call, passing a copy:

```python
my_unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
my_completed_models = []

print_models(my_unprinted_designs[:], my_completed_models)
show_completed_models(my_completed_models)
print(my_unprinted_designs)
```

Output:

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
['phone case', 'robot pendant', 'dodecahedron']
```

The same work happens, but because the function received a copy, `my_unprinted_designs` is unchanged.

> **About the `.py` file:** it includes a `pause()` helper that waits for you to press Enter between the
> two runs, so you can compare the results.

---
