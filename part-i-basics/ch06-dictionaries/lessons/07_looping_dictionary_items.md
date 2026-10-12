## Looping Dictionary Items

Python provides multiple mechanisms for iterating over dictionaries. The
`items()` method returns a `dict_items` object containing a list of tuples in 
which each item contains:

* Key: tuple[0]
* Value: tuple[1]

```python
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
print(user.items())
```

Output:

```
dict_items([('username', 'efermi'), ('first', 'enrico'), ('last', 'fermi')])
```

---

### Accessing `items()` in a Loop

The most straightforward approach to iterating over the `items()` results is to
use multiple assignment to deconstruct the tuples:

```python
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user.items():
    print(f"Key:   {key}")
    print(f"Value: {value}\n")
```

Output:

```
Key:   username
Value: efermi

Key:   first
Value: enrico

Key:   last
Value: fermi
```

---

### Using Meaningful Names

We should avoid thinking that `key` and `value` are required. Instead it's
usually smart to use meaningful variable names when iterating over a
dictionary.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
```

Output:

```
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

---
