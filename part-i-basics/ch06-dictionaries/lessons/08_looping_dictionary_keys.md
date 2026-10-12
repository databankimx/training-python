## Looping Dictionary Keys

Sometimes it's not necessary to enumerate all of the values in a dictionary.
It can be sufficient or even sometimes favorable to obtain just a list of the
keys.

Python provides the `keys()` method, which returns a dict_keys object, which 
contains list of dictionary keys.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print(favorite_languages.keys())
```

Output:

```
dict_keys(['jen', 'sarah', 'edward', 'phil'])
```

---

### Loping over the `keys()`

Like the `items()` you can easily iterate over the dictionary's `keys()`

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())
```

Output:

```
Jen
Sarah
Edward
Phil
```

---

### `keys()` as the Dictionary Default

When you refer to a dictionary as an iterable item, using `in` either for a 
loop or for a condition, the default behavior is to return the `keys()`, so
this loop returns the same results as the previous example.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages:
    print(name.title())
```

Output:

```
Jen
Sarah
Edward
Phil
```

---
