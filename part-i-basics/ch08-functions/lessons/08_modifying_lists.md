## Modifying Lists with Functions

We previously looked at moving or removing list elements using loops in 
top-down code.

This is another case where migrating the work steps to functions can result
in more versatile code.

---

### Getting a Little Technical (Mutable vs Immutable) Types

In some programming languages, we focus on the difference between variables 
that are passed to functions by value and variables that are passed by 
reference, where value variables pass copies of the variable but reference
variables pass the memory address of the variable itself, meaning that
changes to the variable in the function affect the original variable that was
passed.

In Python, all variables are passed by reference, but we still have to draw a 
distinction between variables that are passed as copies versus those that
share the original with the function.

The rule in has to do with the mutability of the data type.

If a type is *immutable*, this means that the object containing the type
cannot be modified (mutated) after it is initialized. The object can be 
replaced but not altered.

This means that when your code performs a task that would modify a variable
containing an immutable type, the memory address is changed, and the new
value is placed at the new address. The value at the original address does
not change.

When an immutable type is passed to a function, the function receives a copy
of the value.

The following types are immutable in Python:

* `int`
* `float`
* `tuple`
* `complex`
* `string`
* `bytes`

All other data types are *mutable* (able to be modified/mutated). When a 
variable containing a mutable type (like a `list`) is passed to a function, 
the function receives the memory address of the original variable, not a copy.

So modifications to the variable in the function affect the original
variable itself.

---

### Lists are Mutable

Because lists are mutable, if we pass them to functions, work performed 
inside the function modified the original variable in the calling location.

Note how the `print_models()` function below does not include a `return`.

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

Here, after executing, the original lists will have changed, even without a
`return`.

```python
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
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

At the end, when we print `unprinted_designs`, the list is now empty.

---

### Making Copies to Prevent Mutating the Original Data

To prevent mutating the original variable, we can pass a copy rather than
the variable itself. With a list, the easy way to create a copy is to use
a slice without either end bound:

```copy = my_list[:]```

Calling the same functions as before, but passing a copy has different
results.

```python
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
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

The same work took place, but because we passed a copy, `unprinted_designs` is
unchanged.

---
