## Filtering Iterables

These four functions filter an iterable without building a new list first. Two of them
stop at a boundary, and two select items by a test or by a set of flags.

The code for this lesson is in [06_filtering.py](./06_filtering.py).

---

### `takewhile()`: Keep the Start

`takewhile(test, items)` yields items while the test is true, and stops the first
time it is false. Items after that point are never checked:

```python
from itertools import takewhile

print(list(takewhile(lambda x: x < 4, [1, 2, 3, 4, 1])))
```

Output:

```
[1, 2, 3]
```

The final `1` is not included, even though it passes the test, because the
iteration has already stopped at `4`.

---

### `dropwhile()`: Skip the Start

`dropwhile(test, items)` is the opposite. It skips items while the test is true,
then yields everything from the first false item onward, including later items
that pass the test:

```python
from itertools import dropwhile

print(list(dropwhile(lambda x: x < 4, [1, 2, 3, 4, 1])))
```

Output:

```
[4, 1]
```

---

### `filterfalse()`: Keep What Fails the Test

`filterfalse(test, items)` keeps the items for which the test is false. It's the
same as a `filter()` with the test reversed:

```python
from itertools import filterfalse

print(list(filterfalse(lambda x: x % 2 == 0, range(6))))
```

Output:

```
[1, 3, 5]
```

Here the test asks "is this number even?", and `filterfalse()` keeps the odd numbers.

---

### `compress()`: Select with a Mask

`compress(items, selectors)` yields each item whose matching selector is true. The
selectors are usually `1` and `0`, or `True` and `False`:

```python
from itertools import compress

print(list(compress("ABCDE", [1, 0, 1, 0, 1])))
```

Output:

```
['A', 'C', 'E']
```

Use `compress()` when the selection rule is already a list of flags, such as a
column of a table.

---

### Try It

Use `takewhile()` to read numbers from a list until the first negative number,
and check that the negative number and everything after it are left out.

---
