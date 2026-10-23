## Dictionary Values

Python also has a `values()` method, which gives you a view of the values in a dictionary. It's
used less often than `keys()` and `items()`, and in many situations it's less useful. It's still
worth knowing.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print(favorite_languages.values())
```

Output:

```
dict_values(['python', 'c', 'ruby', 'python'])
```

The result is a `dict_values` object, a live view of the values. Like the other views, you can loop
over it.

---

### Looping over `values()`

Since you can loop over the view, you can go through each value in turn:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

Output:

```
Python
C
Ruby
Python
```

---

### Avoiding Repetition

Unlike keys, a dictionary's values can repeat. If you want each language listed once, use the
`set()` function to remove the duplicates:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

Output:

```
C
Python
Ruby
```

> Note: Your output order may differ, because sets don't have a guaranteed order.

---

### Getting Statistics from Dictionary Values

One useful thing to do with `values()` is count how many times each value appears. There are two
ways to approach it.

#### Store a dictionary of value and count pairs

If you'll reuse the counts, it's worth storing them in a new dictionary, pairing each value with
how many times it appears:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
counts = {}
for language in favorite_languages.values():
    if language in counts:
        counts[language] += 1
    else:
        counts[language] = 1
print("\nThe following languages have been mentioned:")
for lang in sorted(counts):
    print(f"{lang.title()}: {counts[lang]} time{('' if counts[lang] == 1 else 's')}")
```

Output:

```
The following languages have been mentioned:
C: 1 time
Python: 2 times
Ruby: 1 time
```

#### Count on the fly

If you won't reuse the counts, you can work them out when you print. Here, `count()` on a list does
the counting for each unique value:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
languages = list(favorite_languages.values())
print("\nThe following languages have been mentioned:")
for lang in set(languages):
    print(f"{lang.title()}: {languages.count(lang)} time{('' if languages.count(lang) == 1 else 's')}")
```

Output:

```
The following languages have been mentioned:
C: 1 time
Python: 2 times
Ruby: 1 time
```

Because this loops over a `set`, the order of the lines may differ on your computer.

> **A shortcut:** the `collections` module includes a `Counter` class that does this counting for you.
> You'll meet it when you need it. For now, it's useful to know that counting values is a common job,
> and that a dictionary is a natural way to do it.

---
