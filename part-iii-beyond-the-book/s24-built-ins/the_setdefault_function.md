## `setdefault()`

`setdefault(key, value)` is a dictionary method. It adds the key with the value
only when the key is missing. If the key is already there, it leaves the
dictionary unchanged.

The code for this lesson is in
[the_setdefault_function.py](./the_setdefault_function.py):

```python
from pprint import pprint


def add_missing_key_example() -> None:
    """Add a key with setdefault() when the key is missing"""
    my_dict = {"name": "fido", "age": 3}
    print(my_dict)

    # This will add the default value like my_dict["animal"] = dog
    my_dict.setdefault("animal", "dog")
    print(my_dict)


def keep_existing_value_example() -> None:
    """Show that setdefault() leaves an existing key unchanged"""
    my_dict = {"name": "fido", "age": 3}
    my_dict.setdefault("animal", "dog")

    # But, while my_dict["animal"] = cat would overwrite the value for key = animal, this will not
    my_dict.setdefault("animal", "cat")
    print(my_dict)


def pprint_example() -> None:
    """Pretty-print a dictionary with one key per line"""
    my_dict = {"name": "fido", "age": 3, "animal": "dog"}

    # While we're here, let's demonstrate pretty-print
    pprint(my_dict, width=1)
```

---

### Adding a Missing Key

The first `setdefault()` call adds `"animal": "dog"`, because `animal` is not in
the dictionary yet.

### Keeping an Existing Value

The second call uses `"cat"`, but it does nothing, because `animal` already has
the value `"dog"`. Compare this with `my_dict["animal"] = "cat"`, which would
overwrite the value.

---

### Output

```
{'name': 'fido', 'age': 3}
{'name': 'fido', 'age': 3, 'animal': 'dog'}

{'name': 'fido', 'age': 3, 'animal': 'dog'}

{'age': 3,
 'animal': 'dog',
 'name': 'fido'}
```

The last block is `pprint()`. With `width=1`, it puts each key on its own
line. It also sorts the keys alphabetically, which is its default behavior.

---

### A Common Use

`setdefault()` is useful when you want to group values by a key. You can add
an empty list the first time a key appears, and then append to it:

```python
groups = {}
groups.setdefault("fruit", []).append("apple")
groups.setdefault("fruit", []).append("pear")
```

---
