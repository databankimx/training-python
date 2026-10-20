## Dictionary Comprehensions

Like lists, dictionaries can be expressed as comprehensions. This enables you
to write more concise code with fewer nested loops.

---

### Using a Loop to Merge Two Lists

Consider the case where we have two lists and want to combine them into one
dictionary such that for each index `n`, the key is `list1[n]` and the value
is `list2[n]`.

We can use a loop the way we've done thus far:

```python
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]
print(dictionary)
```

Output:

```
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

---

### Converting a Loop to a Comprehension

Just as we learned when we were reviewing list comprehensions, the loop can be
encapsulated as the range for a dictionary comprehension.

Of course, in a comprehension for a dictionary, we must specify both parts of
the `key: value` pair.

```python
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)
```

Output:

```
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

---

### Using `zip()` in the Comprehension

Since the `zip()` function produces a list of tuples from two lists, we can
use it to avoid needing to use an index like `i` above.

```python
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
dictionary = {key: value for (key, value) in zip(keys, values)}
print(dictionary)
```

Output:

```
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

---

### Adding Conditions

Lastly, we can filter the results being populated in the new dictionary by
adding a condition to the comprehension.

```python
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
odd_dict = {key: value for (key, value) in zip(keys, values) if value % 2}
print(odd_dict)
```

Output:

```
{'a': 1, 'c': 3, 'e': 5}
```

---
