## Running Totals with `accumulate()`

`accumulate()` yields each intermediate result of combining the values so far. By
default it adds them, which gives a running total.

The code for this lesson is in [03_accumulate.py](./03_accumulate.py).

---

### A Running Sum

```python
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4])))
```

Output:

```
[1, 3, 6, 10]
```

Each value is the sum of all the items up to and including that position: 1,
then 1 + 2, then 1 + 2 + 3, and so on.

---

### A Running Maximum

Pass a function as the second argument to combine the values in a different way.
Here, `max` keeps track of the largest value seen so far:

```python
print(list(accumulate([3, 1, 4, 1, 5], max)))
```

Output:

```
[3, 3, 4, 4, 5]
```

The result never goes down, because each step keeps the larger of the current
value and the largest value seen before.

---

### Try It

Use `accumulate()` with `min` on a list of temperatures, to track the lowest
temperature seen so far. Predict the result before you run the code.

---
