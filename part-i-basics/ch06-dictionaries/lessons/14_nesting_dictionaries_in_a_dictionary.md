## Nesting Dictionaries in a Dictionary

Sometimes the values in a dictionary are themselves dictionaries. That fits best when each value
has several different properties, rather than several instances of the same kind of thing.

---

### Properties as Dictionary Values

Suppose you use a username as the key, and each value holds that user's details. A list won't work
well here, because each detail has a name. A dictionary nested as each key's value describes the
users most clearly:

> Warning! Be careful how deeply you nest dictionaries. The deeper the nesting, the harder the code
> is to read.

```python
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    print(f"\tName: {full_name.title()}")
    print(f"\tLocation: {user_info['location'].title()}")
```

Output:

```
Username: aeinstein
        Name: Albert Einstein
        Location: Princeton

Username: mcurie
        Name: Marie Curie
        Location: Paris
```

---

### Looking Up a Nested Value

You don't always need a loop. To reach a value inside a nested dictionary, chain the keys, one
level at a time:

```python
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
print(users["aeinstein"]["first"])
```

Output:

```
albert
```

The first key picks out the inner dictionary, and the second key picks out the value inside it. The
same pattern works for any number of levels, as long as each key exists.

---
