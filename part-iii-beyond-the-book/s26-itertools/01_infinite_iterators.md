## Infinite Iterators

Some `itertools` functions produce values forever. They are useful, but they must
be stopped. A `list()` on one of them would never finish, so we always limit them
with `islice()` or a similar stop.

The code for this lesson is in [01_infinite_iterators.py](./01_infinite_iterators.py).

---

### `count()`: Counting Forever

`count(start, step)` produces `start`, `start + step`, `start + 2 * step`, and so on:

```python
from itertools import count, islice

print(list(islice(count(10, 5), 4)))
```

Output:

```
[10, 15, 20, 25]
```

`islice(iterator, n)` takes the first `n` values. Without it, `count()` would
never stop.

---

### `cycle()`: Repeating a Sequence

`cycle()` goes through a sequence and then starts again from the beginning:

```python
from itertools import cycle, islice

print(list(islice(cycle("ABC"), 7)))
```

Output:

```
['A', 'B', 'C', 'A', 'B', 'C', 'A']
```

This is handy for round-robin tasks, such as giving each player a turn in order.

---

### `repeat()`: One Value, Several Times

`repeat(value, times)` produces the same value a fixed number of times. Unlike the
other two functions, it stops by itself when you give it a count:

```python
from itertools import repeat

print(list(repeat("ha", 3)))
```

Output:

```
['ha', 'ha', 'ha']
```

Without the `times` argument, `repeat()` produces the value forever.

---

### Try It

Use `cycle()` with a list of three colors to label the first ten items in a list,
each with the next color in turn. Predict the first three colors before you run it.

---
