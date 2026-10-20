## Using Dictionaries to Group Similar Objects

While it is common to use a dictionary to keep track of a group of traits
related to one object (as we'ce been doing thus far), dictionaries are often
used to store one property across multiple objects.

### Linking Users to a Property

In this example, we're storing a single property (favorite programming 
language) for each of a group of people.

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

---
