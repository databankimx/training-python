## `id()`: Where an Object Lives

The built-in `id()` function returns the memory address of an object. In
CPython, that is the number used to identify the object while the program is
running.

The code for this lesson is in [the_id_function.py](./the_id_function.py):

```python
"""The id function"""

# In Python, the id() function returns the memory location where an
# object is stored

# Here I am stashing a string in memory
loc_1 = id("Hello World")
print(loc_1)

# Here, we put the same string into a variable
# Because Python uses a table of all stored string values to minimize
# memory use, this is at the same address
my_string = "Hello World"
loc_2 = id(my_string)
print(loc_2)

# When we change the value, however, even though it's the same variable,
# the string is at a new address
my_string = "Hello World!"
loc_3 = id(my_string)
print(loc_3)
```

---

### Equal Strings Can Share an Address

Python stores identical string constants once and reuses them. In the script,
`loc_1` and `loc_2` both refer to the text `"Hello World"`, so they print the
same number.

### A Changed Value Gets a New Address

Assigning `"Hello World!"` to `my_string` creates a different string object, with
a different address. The variable name is the same, but the object it refers to
has changed, so `loc_3` is different from `loc_2`.

---

### Output

The addresses depend on the machine and the run, so the numbers themselves will
differ. The pattern is what matters:

```
140711219617712
140711219617712
140711219619376
```

The first two numbers are the same, and the third is different.

---

### Note

Do not use `id()` to compare values. Use `==` to check whether two objects have
the same value, and `is` only to check whether they are the same object. The
[copy lesson](./the_copy_module.md) relies on that difference.

---
