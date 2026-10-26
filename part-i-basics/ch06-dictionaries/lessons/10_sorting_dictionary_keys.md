## Sorting Dictionaries

There are a few ways to sort a dictionary. The most common is to sort only the keys, and then use
them to look up values.

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print(sorted(favorite_languages.keys()))
# Note: Just as before, `.keys()` is optional, since it's the default result
print(sorted(favorite_languages))
```

Output:

```
['edward', 'jen', 'phil', 'sarah']
['edward', 'jen', 'phil', 'sarah']
```

---

### Looping over the Sorted Keys

`sorted()` returns a list of the keys, so you can loop over the result like any other list:

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")
```

Output:

```
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

---

### Sorting the Dictionary Itself

Sorting the keys has always worked. What's new is that dictionaries keep their insertion order
(guaranteed since Python 3.7), so the order you create a dictionary in matters when you print it
or loop over it.

You can't sort a dictionary in place, though. `sorted()` gives you a list of the items, and to get
a dictionary back, you build a new one with `dict()`. The original dictionary stays as it was.

---

### Sorting the Dictionary by Key

Here, we sort the `items()` by key. Each item is a `(key, value)` tuple, so `item[0]` is the key:

```python
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(dict(sorted(people.items())))
```

Output:

```
{1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}
```

---

### Sorting the Dictionary by Value

To sort by value instead, pass the `key` argument to `sorted()`. The argument is a small function
that tells `sorted()` which part of each item to compare. Here we use a `lambda`, which is a short,
unnamed function. Chapter 8 covers functions, and you'll see more of them there.

```python
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(dict(sorted(people.items(), key=lambda item: item[1])))
```

Output:

```
{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
```

---
