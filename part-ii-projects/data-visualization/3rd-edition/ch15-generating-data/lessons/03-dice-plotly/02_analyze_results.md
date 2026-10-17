# Analyzing Results

## Introduction

A list of 100 rolls is hard to read. Counting how often each face came up turns the list into
something useful. This lesson rolls the die 1,000 times and counts the results, one face at a time.

---

## The Code

```python
"""Lesson 3.2 - Analyzing Results"""

from die import Die

die = Die()

results = []
for _ in range(1000):
    results.append(die.roll())

# Process the results and stash the number of times each value occurs in a new list
frequencies = []
poss_results = range(1, die.num_sides + 1)
for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

print(frequencies)
```

---

### Walking Through the Code

**Rolling many times.** The first loop rolls the die 1,000 times, as before.

**The possible results.** `range(1, die.num_sides + 1)` gives the faces 1 to 6. Using `num_sides`
rather than a fixed 6 means the code still works for a die with a different number of sides.

**Counting.** For each face, `results.count(n)` counts how many times that face appears in the
results. The counts go into `frequencies`, in the same order as the faces. The first number is
the count of 1s, the second the count of 2s, and so on.

---

### Output

The terminal prints six numbers. They should be roughly equal, close to 167 each, because 1,000
rolls divided by six faces is about 167. Each run gives slightly different numbers. A sample run
looks like this:

```
[155, 177, 156, 167, 175, 170]
```

---
