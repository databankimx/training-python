## Returning Dictionaries from Functions

Creating dictionaries that share the same set of keys is one of the more repetitive things you can do
in code. For example, you might describe several people with the same fields.

Functions are a good way to avoid that kind of repetition. Put the work of building the dictionary in a
function, and call it whenever you need one.

---

### Constructing a Dictionary

Here's a simple function that builds a dictionary:

```python
def build_person_simple(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person_simple("jimi", "hendrix")
print(musician)
```

Output:

```
{'first': 'jimi', 'last': 'hendrix'}
```

---

### Refining the Returned Dictionary

As with the other functions, we can make this more versatile by adding an optional argument.

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    # Check for None, not for truthiness: an age of 0 is valid, and `if age:` would skip it
    if age is not None:
        person["age"] = age
    return person

musician1 = build_person("jimi", "hendrix", age=27)
print(musician1)
musician2 = build_person("jimi", "hendrix")
print(musician2)
```

Output:

```
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
{'first': 'jimi', 'last': 'hendrix'}
```

> **Why `is not None` and not `if age`?** Zero is falsy in Python, so `if age:` treats an age of `0` as
> missing. A newborn can be zero years old, so the check should ask whether a value was given at all.
> `is not None` asks exactly that.

> **About the `.py` file:** it includes a `pause()` helper that waits for you to press Enter between
> the examples, so you can read each result before the next one appears.

---

