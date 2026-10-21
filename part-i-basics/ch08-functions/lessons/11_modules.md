## Importing Code from Modules

In Python, a *module* is simply a file of code that another file can import and use. For this lesson,
we have an external module saved as [pizza.py](./pizza.py), which contains this code:

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

So this module exposes one function: `make_pizza()`.

---

### Importing the Module

To bring everything the module exposes into the current file, use the syntax `import module_name`, where
`module_name` is the file name without its extension.

So, in our example, we'd write:

```python
import pizza
```

---

#### Calling a Function from the Imported Module

To call a function from an imported module, use the syntax `module_name.function_name()`.

```python
pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green pepper")
```

Output:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper
```

---

### Importing a Function from the Module

You can import a single function from a module, without importing the whole module, with the syntax
`from module import function`.

In our case, that looks like this:

```python
from pizza import make_pizza
```

Then you can call the function directly, without the module name:

```python
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper")
```

Output:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper
```

---

### Importing Multiple Functions from the Module

You can import several functions from the same module:

```python
from module import function1, function2, ...
```

You can also import everything the module exposes with an asterisk:

```python
from module import *
```

This works, but it's generally discouraged. The asterisk hides where each name came from, and it can
quietly replace names you already have. PEP 8, the official style guide, recommends naming the
functions you need instead.

---

### Giving an Imported Module or Function an Alias

The `as` keyword gives an imported module or function a shorter name:

```python
import pizza as p
from pizza import make_pizza as mp
```

Then you can use the alias anywhere you'd use the original name:

```python
p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green pepper")
mp(16, "pepperoni")
mp(12, "mushrooms", "green pepper")
```

Output:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper

Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper
```

---

> **About the Pylint comments:** the `.py` file puts the `from ... import` lines below the first `import`,
> and Pylint flags that as `wrong-import-position`. It also flags importing the same module twice under
> different names as `reimported`. The comments turn those warnings off, because the examples are meant to
> show each import style side by side. The `#NOSONAR` comment on one line serves the same purpose for the
> code-quality scanner. In a real program, you'd normally keep one import style.

---

