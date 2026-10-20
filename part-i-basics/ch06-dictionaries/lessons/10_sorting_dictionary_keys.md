## Sorting Dictionaries

There are a number of ways to sort a dictionary. The most common is to sort
only the keys, and then use those to access any element in the dictionary.

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

Like any list, the result of sorting the dictionary keys

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

### Sorting the Actual Dictionary

Prior to Python v3.6, dictionaries were not ordered, meaning they were
non-sortable. However, in current versions of Python, dictionary order is
maintained, so it is possible to sort them.

Unfortunately, dictionaries cannot be sorted in place. No matter what method 
is used, a copy must be created using the `dict()` function for sorting.

---

### Sorting the Dictionary by Key

Here is an example where we've sorted `items()` by key (or `item[0]` to be
precise)

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

To sort by the values instead, we must specify the `key` argument in the
`sorted()` function. For this, I am using a `lambda`, which is an anonymous 
function that can be passed as an argument or stored in a variable.

> Don't worry about `lambda` functions for now. They are covered in the
> Part III supplemental lessons.

```python
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(dict(sorted(people.items(), key=lambda item: item[1])))
```

Output:

```
{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}
```

---
