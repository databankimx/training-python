## Nesting Lists in a Dictionary

In the same vein as dictionaries nested in lists, it's often useful to nest
one or more lists in a dictionary.

---

### A Property of a Dictionary that has Multiple Values

One common example of this is where one or more properties os a dictionary 
that describes an object can have multiple values.

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

---

### Dictionary Elements with Multiple Values

In the scenario where we are using a dictionary as a collection of like 
objects, it is still possible for each one to have multiple values. In this
case, we can make the value for each key a list.

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
