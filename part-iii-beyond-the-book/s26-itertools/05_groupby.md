## Grouping with `groupby()`

`groupby()` splits a sequence into groups of consecutive items that share the same
key. It is simple to use, but it has one rule you must follow: it only groups
items that are next to each other.

The code for this lesson is in [05_groupby.py](./05_groupby.py):

```python
from itertools import groupby

DATA = [("fruit", "apple"), ("fruit", "pear"), ("veg", "kale"), ("fruit", "plum")]

for key, group in groupby(DATA, key=lambda row: row[0]):
    items = ", ".join(item for _, item in group)
    print(f"{key}: {items}")
```

---

### Unsorted Data Makes Extra Groups

The `fruit` rows are in the data in two places, separated by `veg`. `groupby()` starts
a new group each time the key changes, so `fruit` appears twice:

```
fruit: apple, pear
veg: kale
fruit: plum
```

The key is the same, but the rows are not all together, so they land in separate groups.

---

### Sort First

Sort the data by the same key before grouping. Now all the `fruit` rows are next to
each other, and each key forms one group:

```python
for key, group in groupby(sorted(DATA, key=lambda row: row[0]), key=lambda row: row[0]):
    items = ", ".join(item for _, item in group)
    print(f"{key}: {items}")
```

Output:

```
fruit: apple, pear, plum
veg: kale
```

Python's `sorted()` keeps items with equal keys in their original order, so the
`fruit` items appear as `apple, pear, plum`.

---

### Try It

Remove the `sorted()` call from the second example, and move the `veg` row so
that it sits between the two `fruit` rows. Predict whether `fruit` will appear as one
group or two, then run the code to check.

---
