## Nesting Lists in a Dictionary

It's often useful to nest one or more lists inside a dictionary. In the same way you nested
dictionaries in lists, you can give a dictionary's key a list as its value.

---

### A Property with Multiple Values

One common case is a property of a dictionary that describes an object, where the property can
hold more than one value. A pizza is a good example. Its crust has one value, but it can have
several toppings:

```python
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}
if pizza["toppings"]:
    print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
    for topping in pizza["toppings"]:
        print(f"\t{topping}")
else:
    print(f"You ordered a {pizza['crust']}-crust plain pizza")
```

Output:

```
You ordered a thick-crust pizza with the following toppings:
        mushrooms
        extra cheese
```

The `if pizza["toppings"]:` check works because an empty list is `False`. If there are no toppings,
the code takes the `else` path. We looked at that idea in lesson 5.6.

---

### Dictionary Values That Hold Lists

When a dictionary holds a collection of similar objects, each object can still have several values.
In that case, make each key's value a list:

```python
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell", "rust"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")
```

Output:

```
Jen's favorite languages are:
        Python
        Ruby

Sarah's favorite languages are:
        C

Edward's favorite languages are:
        Ruby
        Go

Phil's favorite languages are:
        Python
        Haskell
        Rust
```

---
