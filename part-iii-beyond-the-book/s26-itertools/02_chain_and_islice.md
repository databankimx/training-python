## Joining and Slicing

`chain()` joins several iterables end to end. `islice()` takes a slice of any
iterable, including ones that don't support `[start:stop]` indexing, such as a
generator.

The code for this lesson is in [02_chain_and_islice.py](./02_chain_and_islice.py).

---

### `chain()`: Joining Iterables

`chain()` takes any number of iterables and yields the values from each one in turn:

```python
from itertools import chain

print(list(chain([1, 2], [3], [4, 5])))
```

Output:

```
[1, 2, 3, 4, 5]
```

The iterables don't have to be lists. Any iterable works, and the values are not
copied into a new list until you ask for one.

---

### `chain.from_iterable()`: Joining a Collection of Iterables

If the iterables are already in one list, pass that list to `chain.from_iterable()`
instead of unpacking it with `*`:

```python
print(list(chain.from_iterable([[1, 2], [3, 4]])))
```

Output:

```
[1, 2, 3, 4]
```

This is the same result as `chain(*[[1, 2], [3, 4]])`, but it is clearer and
avoids unpacking a large number of arguments.

---

### `islice()`: Slicing Any Iterable

`islice(iterable, start, stop, step)` works like `[start:stop:step]`, but for any
iterable. The `stop` value is not included, as with normal slices:

```python
from itertools import islice

print(list(islice(range(10), 2, 8, 2)))
```

Output:

```
[2, 4, 6]
```

Use `islice()` with a generator, where `[start:stop]` would fail because the
generator cannot be indexed.

---

### Try It

Join three lists of different lengths with `chain()`. Then use `islice()` to take
only the first four values from the joined result.

---
