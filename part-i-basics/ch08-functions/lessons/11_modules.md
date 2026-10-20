## Importing Code from Modules

In Python, a *module* is a functional collection of code outside the current
file. For this lesson, we have an external module saved as
[pizza.py](./pizza.py) containing the following code:

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

So this module exposes one function: `make_pizza()`

---

### Importing the Module

To bring all of the code exposed by the module into scope for use in the 
current file, we use the syntax: `import module_name`, where `module_name` is
the external filename without its extension.

So, in our example, we would call

```python
import pizza
```

---

#### Calling a Function from the Imported Module

To call a function from a module we have imported, we use the syntax:
`module_name.function_name()`.

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

We can import a function (or functions) from a module without importing the
entire module itself with the following syntax: `from module import function`

In our case, this takes the following form:

```python
from pizza import make_pizza
```

We can then call the imported function directly, without specifying the module
name.

```python
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper")
```

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper
```

---

### Importing Multiple Functions from the Module

We can also import multiple functions from the module using the following:

```python
from module import function1, function2, ...
```

Or we can import all functions exposed by the module like so:

```python
from module import *
```

---

### Giving an Imported Module or Function an Alias

Using the `as` keyword, we can provide an alias to an imported module or 
function.

```python
import pizza as p
from pizza import make_pizza as mp
```

Then, in our code, we can substitute the aliases whenever we are referring to
the imported item.

```python
p.make_pizza(12, "mushrooms", "green pepper")
mp(12, "mushrooms", "green pepper")
```

Output:

```
Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper

Making a 12-inch pizza with the following toppings:
- mushrooms
- green pepper
```

---
