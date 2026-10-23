## Conditional Handling with Dictionaries

Sometimes you want to do something with dictionary values only when a certain condition is met.

---

### Comparing `keys()` Against a List

In this example, we loop over every key in the dictionary and print a greeting for each one. For
the people in our `friends` list, we also print an extra message about their favorite language.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
friends = ["phil", "sarah"]
for name in favorite_languages:
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")
```

Output:

```
Hi Jen!
Hi Sarah!
        Sarah, I see you love C.
Hi Edward!
Hi Phil!
        Phil, I see you love Python.
```

> **About the Pylint warning:** the `.py` file disables `consider-using-dict-items`. Pylint raises it
> because the loop looks up each value inside the loop, and it suggests looping over `items()` instead.
> That's a style suggestion, not an error. Both versions are correct. The loop here is written to
> show each step clearly, so the `.py` file turns the warning off.

---

### Comparing a List Against `keys()`

The reverse can also be useful. Perhaps you want to do something only when a name in a list
doesn't appear among the dictionary's keys.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
people = ["phil", "sarah", "erin", "jen", "edward"]
for person in people:
    if person not in favorite_languages:
        print(f"{person.title()}, please take the languages poll.")
```

Output:

```
Erin, please take the languages poll.
```

---
