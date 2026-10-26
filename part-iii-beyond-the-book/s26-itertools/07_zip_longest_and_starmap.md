## Pairing and Mapping

`zip()` stops at the shortest iterable. `zip_longest()` keeps going until the longest
one is finished. `starmap()` is `map()` for functions that take several arguments.

The code for this lesson is in [07_zip_longest_and_starmap.py](./07_zip_longest_and_starmap.py).

---

### `zip_longest()`: Pairing Unequal Lengths

With `zip()`, the shortest iterable decides the length of the result. `zip_longest()`
fills the missing values with `fillvalue`:

```python
from itertools import zip_longest

print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")))
```

Output:

```
[(1, 'a'), (2, 'b'), (3, '-')]
```

If you don't pass `fillvalue`, the missing values are `None`.

---

### `starmap()`: Unpacking Arguments

`map(function, items)` calls the function once for each item. If each item is a
tuple of arguments, use `starmap()`, which unpacks each tuple into the function's
parameters:

```python
from itertools import starmap

print(list(starmap(pow, [(2, 3), (3, 2)])))
```

Output:

```
[8, 9]
```

The first call is `pow(2, 3)`, which is 8, and the second is `pow(3, 2)`, which is 9.

---

### Try It

Use `zip_longest()` to combine a list of first names and a shorter list of last
names, with `"?"` as the fill value. Then use `starmap()` with `max` on a list of
pairs of numbers.

---
