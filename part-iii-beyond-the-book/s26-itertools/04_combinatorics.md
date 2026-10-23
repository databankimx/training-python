## Combinations, Permutations, and Products

These three functions generate every way of picking or arranging items from a
collection. They are useful for counting possibilities, testing all options, and
building search spaces.

The code for this lesson is in [04_combinatorics.py](./04_combinatorics.py).

---

### `combinations()`: Order Does Not Matter

`combinations(items, r)` yields every way to choose `r` items. `("A", "B")` and
`("B", "A")` are the same choice, so only one of them appears:

```python
from itertools import combinations

print(list(combinations("ABC", 2)))
```

Output:

```
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

---

### `permutations()`: Order Matters

`permutations(items, r)` yields every way to arrange `r` items. Now `("A", "B")`
and `("B", "A")` are different results:

```python
from itertools import permutations

print(list(permutations("ABC", 2)))
```

Output:

```
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

With three items and `r = 2`, there are six permutations, and three combinations.

---

### `product()`: Every Pair

`product(a, b)` pairs each item in `a` with each item in `b`. It is the same as
nested `for` loops:

```python
from itertools import product

print(list(product([1, 2], ["x", "y"])))
```

Output:

```
[(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]
```

`product()` also accepts a `repeat` argument, so `product("01", repeat=3)` gives
all eight three-digit binary strings.

---

### Try It

Use `combinations()` to list every two-person team that can be made from four
players named `Ana`, `Ben`, `Cy`, and `Dee`. Count the teams before you run the code.

---
