## Nesting Dictionaries in a Dictionary

Lastly, it can be useful to nest additional dictionaries within a dictionary
when the multiple values themselves are different properties instead of just
multiple instances of one characteristic.

---

### Properties as Dictionary Values

Consider the scenario where you are using a username as a key in a dictionary,
and the values are the user details. A list of values won't do in this case.

For scenarios like this, nesting a dictionary as each key's value most
accurately describes the objects.

> Warning! Be careful how deep dictionaries are nested, as this pattern can
> result in less readable code.

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
