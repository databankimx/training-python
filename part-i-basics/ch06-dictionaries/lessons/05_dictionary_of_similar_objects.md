## Using Dictionaries to Group Similar Objects

Earlier, we used a dictionary to hold several traits of one object, like an alien's color and
points. Dictionaries are just as useful for the opposite job: storing one property for many
objects.

### Linking Users to a Property

In this example, each person is a key, and the property we care about is their favorite
programming language:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
name = "phil"
language = favorite_languages[name].title()
print(f"{name.title()}'s favorite language is {language}.")
```

Output:

```
Phil's favorite language is Python.
```

Looking up one person by name is easy. Looking through everyone's answers takes a loop, and
we'll get to looping over dictionaries in lessons 6.7 through 6.9.

---

