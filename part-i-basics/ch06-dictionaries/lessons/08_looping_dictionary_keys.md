## Looping Dictionary Keys

Sometimes you don't need every value in a dictionary. A list of just the keys might be all you
want, or it might be easier to work with.

The `keys()` method gives you a view of the dictionary's keys. The result is a `dict_keys` object,
and like `items()`, it's a live view rather than a list:

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

### Looping Over `keys()`

Just as you can loop over `items()`, you can loop over `keys()`:

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

### Looping Directly over the Dictionary

If you loop over a dictionary directly, without calling `keys()`, Python loops over its keys.
So this loop gives the same results as the one above:

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

> **About the Pylint warning:** Pylint may flag the `keys()` version, with a suggestion to drop
> `.keys()`. That's a style suggestion, not an error. Both loops are correct. The explicit `keys()`
> version is clearer when you're learning, because it says what you're looping over. The `.py` file
> disables that warning on purpose, so the lesson's example runs cleanly in the editor.

---

