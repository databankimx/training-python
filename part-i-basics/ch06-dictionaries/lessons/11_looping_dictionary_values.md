## Dictionary Values

Although less frequently used (and frankly, less valuable in most scenarios), 
Python also exposes the `values()` method, which returns a dict_values object 
containing a list of the values in the dictionary.

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

---

### Looping over `values()`

Of course, since `values()` contains a list, we can iterate over the values.

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

As you saw above, unlike keys, a dictionary's values can include duplicates.
When you want to list the *unique* values, we can use the `set()` function.

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

> Note: Your output order may differ, as sets are not ordered.

---

### Getting Statistics from Dictionary Values

One scenario where analyzing `values()` can be useful is to obtain statistics
like a count of how many times each item has been listed.

There are a couple of approaches we can use:

#### Store a dictionary of `value, count` pairs:

If we'll reuse the information, it's useful to store a new dictionary pairing
each value with its count in the dictionary.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
counts = {}
for language in favorite_languages.values():
    if language in counts.keys():
        counts[language] += 1
    else:
        counts[language] = 1
print("\nThe following languages have been mentioned:")
for lang in sorted(counts.keys()):
    print(f"{lang.title()}: {counts[lang]} time{('' if counts[lang] == 1 else 's')}")
```

Output:

```
The following languages have been mentioned:
C: 1 time
Python: 2 times
Ruby: 1 time
```

---

#### Use the data without storing a new dictionary

If we're not going to reuse the data, it's just as easy to obtain the counts
on the fly rather than storing them for later use.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
languages = list(favorite_languages.values())
for lang in set(languages):
    print(f"{lang.title()}: {languages.count(lang)} time{('' if counts[lang] == 1 else 's')}")
```

Output:

```
The following languages have been mentioned:
Python: 2 times
Ruby: 1 time
C: 1 time
```

---
