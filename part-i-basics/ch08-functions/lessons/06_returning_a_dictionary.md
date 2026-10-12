## Returning Dictionaries from Functions

One of the more repetitive things you can do in code is creating dictionaries
that contain a common set of keys (say for defining the description of a
person).

Functions (since they're intended to prevent exactly this type of redundant 
code) are a great way to encapsulate constructing these objects.

---

### Constructing a Dictionary

Here's a simple dictionary-generating function.

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

Like the other functions, we can refine this to add versatility by including an
optional argument.

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician1 = build_person("jimi", "hendrix", age = 27)
print(musician1)
musician2 = build_person("jimi", "hendrix")
print(musician2)
```

Output:

```
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
{'first': 'jimi', 'last': 'hendrix'}
```

---
