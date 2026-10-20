## `copy()` and `deepcopy()`

Assigning one list to another variable doesn't copy it. Both names refer to the
same list, so a change through either name shows up in both. The `copy` module
gives two ways to make a real copy.

The code for this lesson is in [the_copy_module.py](./the_copy_module.py):

```python
"""The copy module: shallow copies and deep copies"""

from copy import copy, deepcopy

original = [1, 2, [3, 4]]

# copy() makes a new outer list, but the nested list is still shared
shallow = copy(original)

# deepcopy() also copies the nested list
deep = deepcopy(original)

print(f"Equal values: {shallow == original}")
print(f"Same list object: {shallow is original}")

# Change the nested list in the original
original[2].append(5)
print(f"Original: {original}")
print(f"Shallow:  {shallow}   (the nested list changed too)")
print(f"Deep:     {deep}      (unaffected)")
```

---

### Shallow Copy

`copy()` creates a new outer list. The values in it are the same as the
original, but any value that is itself a list is still the same object in both
lists. Changing that nested list changes both copies.

### Deep Copy

`deepcopy()` copies every level, including nested lists, so the two lists are
fully independent.

---

### Output

```
Equal values: True
Same list object: False
Original: [1, 2, [3, 4, 5]]
Shallow:  [1, 2, [3, 4, 5]]   (the nested list changed too)
Deep:     [1, 2, [3, 4]]      (unaffected)
```

The first two lines show that the copy has equal values but is a different
object. The last three show the effect of changing the nested list.

---

### When to Use `deepcopy()`

Use `deepcopy()` whenever the object contains other lists, dictionaries, or
objects that you don't want to share with the copy. A shallow copy is enough
for a flat list, such as `[1, 2, 3]`.

---
