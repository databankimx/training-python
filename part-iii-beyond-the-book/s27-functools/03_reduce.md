## Reducing a Sequence with `reduce()`

`reduce(function, items)` combines the items two at a time. It takes the first two
items, combines them, then combines that result with the next item, and so on until
one value is left.

The code for this lesson is in [03_reduce.py](./03_reduce.py):

```python
from functools import reduce

print(reduce(lambda total, value: total * value, [1, 2, 3, 4]))
print(reduce(lambda total, value: total + value, [1, 2, 3], 10))
print(reduce(max, [3, 9, 4]))
```

---

### Multiplying a Sequence

For `[1, 2, 3, 4]`, `reduce()` computes `((1 * 2) * 3) * 4`:

Output:

```
24
```

The `math.prod()` function does this for you, so `reduce()` with multiplication
shows the idea rather than being the usual tool.

---

### Starting with an Initial Value

The optional third argument sets the starting value. Here the reduction starts at 10,
so the result is `10 + 1 + 2 + 3`:

Output:

```
16
```

Without the initial value, `reduce()` starts with the first item. With it, the
reduction starts from the value you give, which also makes an empty list safe to pass.

---

### Using a Built-In Function

Any function that takes two arguments can be used, including `max`:

Output:

```
9
```

---

### When to Use `reduce()`

`reduce()` is worth using when the combining step is short and clear. When a loop
would be easier to read, use the loop. Many people find `sum()`, `max()`, and
`math.prod()` clearer for the common cases.

---

### Try It

Use `reduce()` to find the longest word in a list of words. Use `max` with the
`key=len` argument by writing a small function that returns the longer of two words.

---
