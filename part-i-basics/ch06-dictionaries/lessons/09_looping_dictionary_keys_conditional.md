## Conditional Handling with Dictionaries

Sometimes you want to perform some task on dictionary values only when a 
certain condition is met.

---

### Compare `keys()` Against a List

In this example, we loop all of the keys in the dictionary and print a
greeting, but we only add a comment to those that also appear in a list.

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

---

### Compare a List Against `keys()`

The reverse can also hold true. Perhaps we want to perform an action only if
a list element does not appear in the dictionary keys.

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
