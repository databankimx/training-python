## Using Underscores in Names

Python has some conventions for the use of underscores in naming:

---

### Leading Underscore: `_name`

The use of a single leading underscore as in `_name` is a way for a developer 
to indicate to others that a variable should be treated as private (not to be
modified outside the class, e.g.).

* This convention is mostly ignored by the Python interpreter. However:
    * When declared in a module and imported by another file:
        * It will not be included when using `from module import *`
        * It will be included when using `import module`

---

### Trailing Underscore: `name_`

Use of a single trailing underscore as in `name_` is typically an indicator 
that the name would otherwise conflict with a Python reserved word.

For example, you might name a variable `class_`

**List of Python Reserved Words**
||||||||||
|-|-|-|-|-|-|-|-|-|
|`False`|`def`|`if`|`raise`|`None`|`del`|`import`|`return`|`True`|
|`elif`|`in`|`try`|`and`|`else`|`is`|`while`|`as`|`except`|
|`lambda`|`with`|`assert`|`finally`|`nonlocal`|`yield`|`break`|`for`|`not`|
|`class`|`from`|`or`|`continue`|`global`|`pass`||||
|`async`|`await`|||||||

---

### Stand-Alone Underscore: `_`

A single underscore by itself `_` is used in context to create a temporary 
variable that cannot be used outside the context.

For example:

```python
# Loop ten times without any need to care about which iteration
for _ in range(10):
    # Do something
```

or

```python
# Skip unimportant values in multiple assignment:
var1, _, _, var2, _ = ["important", "meh", "meh", "important", "meh"]
```

---

### Leading Double-Underscore: `__name`

This is used when implementing name mangling for class attributes to make them
more difficult to access directly.

```python
class MyClass:
    def __init__(self):
        self.__name = "value"

# You would need to know the mangled name to access that attribute:
thing = MyClass()

# This works
thing._MyClass__name = "new value"

# This doesn't
thing.__name = "new value"
```

---

### Leading and Trailing Double-Underscores: `__name__`

These are used for "magic" or "dunder" methods and attributes such as:

* `__init__()` is the class constructor
* `__name__` is the script name attribute
* `__str__()` and `__repr__()` are commonly overridden magic methods

While we *could* create our own dunder methods, this nomenclature is reserved 
for future use in Python, so we probably shouldn't.

---

