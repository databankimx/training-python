## Dictionary Comprehensions

Like lists, dictionaries can be written as comprehensions. A comprehension lets you write
the same logic in less code, with fewer nested loops.

---

### Using a Loop to Merge Two Lists

Suppose you have two lists, and you want to combine them into one dictionary. For each index `n`,
the key should be `list1[n]`, and the value should be `list2[n]`.

We can use a loop, the way we've done so far:

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

Just as we saw with list comprehensions, the loop's body becomes the expression at the front of
the comprehension. For a dictionary, that expression has to supply both parts of the `key: value`
pair.

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

`zip()` pairs up the items from two lists, and it returns an iterator of tuples. Pairing the two
lists this way removes the need for an index like `i`:

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

Finally, you can filter the entries that go into the new dictionary by adding a condition to the
comprehension. This example keeps only the odd values:

```python
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
odd_dict = {key: value for (key, value) in zip(keys, values) if value % 2 == 1}
print(odd_dict)
```

Output:

```
{'a': 1, 'c': 3, 'e': 5}
```

---
