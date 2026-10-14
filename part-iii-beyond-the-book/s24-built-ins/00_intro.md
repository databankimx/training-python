## Built-In Functions and Modules

Python ships with many built-in functions and standard library modules. This
short lesson covers a few that are useful but easy to overlook. Each example
is a small script you can run on its own.

* [`the_id_function.py`](./the_id_function.py) - `id()` and memory addresses
* [`the_copy_module.py`](./the_copy_module.py) - `copy()` and `deepcopy()`
* [`the_setdefault_function.py`](./the_setdefault_function.py) - `setdefault()` for dictionaries
* [`pyperclip_to_clipboard.py`](./pyperclip_to_clipboard.py) - copying to and pasting from the clipboard
* [`shebang.py`](./shebang.py) - choosing which Python runs a script

---

### `id()`: Where an Object Lives

`id()` returns the memory address of an object. Python stores many strings
once and reuses them, so two variables with the same text can share an address:

```python
loc_1 = id("Hello World")
my_string = "Hello World"
loc_2 = id(my_string)      # usually the same address as loc_1
```

Changing a string creates a new object, so the address changes:

```python
my_string = "Hello World!"
loc_3 = id(my_string)      # a different address
```

---

### `copy()` and `deepcopy()`

Assigning one list to another makes a second name for the same list, not a
copy. `copy()` makes a new outer list, but any nested list is still shared
between the two:

```python
from copy import copy

original = [1, 2, [3, 4]]
shallow = copy(original)
original[2].append(5)
print(shallow)    # [1, 2, [3, 4, 5]] - the nested list changed too
```

`deepcopy()` copies the nested lists as well, so the two lists are fully
independent:

```python
deep = deepcopy(original)
```

Use `deepcopy()` whenever the list contains other lists or objects.

---

### `setdefault()`

`setdefault(key, value)` adds the key with the value only if the key is missing.
If the key already exists, it leaves the dictionary alone:

```python
my_dict = {"name": "fido", "age": 3}
my_dict.setdefault("animal", "dog")   # adds "animal": "dog"
my_dict.setdefault("animal", "cat")   # does nothing; "animal" already exists
```

---

### The Clipboard

The `pyperclip` library copies text to the system clipboard and reads it back.
Install it with `python -m pip install pyperclip`, then:

```python
import pyperclip

pyperclip.copy("Hello")
print(pyperclip.paste())   # Hello
```

---

### The Shebang Line

On Linux and macOS, a script whose first line starts with `#!` tells the system
which interpreter to run it with. `#! python3` asks for Python 3 specifically.
On Windows, the `py` launcher plays the same role.

---
