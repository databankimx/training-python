## Improving Loops with `enumerate()` and `zip()`

There are times when you need the index as well as the value while looping,
or when you need to loop over two lists simultaneously. Python provides two
built-in functions that handle both cases cleanly.

- `enumerate(iterable)` - returns an iterable of `(index, value)` tuples
- `zip(iterable_1, iterable_2)` - returns an iterable of `(value_1, value_2)` tuples

---

### Looping a List with Indices - the basic way

```python
nums = [1, 42, 73]
for i in range(len(nums)):
    item = nums[i]
    print(f"Index: {i}, Item: {item}")
```

Output:

```
Index: 0, Item: 1
Index: 1, Item: 42
Index: 2, Item: 73
```

---

### Looping a List Using `enumerate()`

`enumerate()` gives you both the index and value without manual indexing:

```python
nums = [1, 42, 73]
for i, item in enumerate(nums):
    print(f"Index: {i}, Item: {item}")
```

Output:

```
Index: 0, Item: 1
Index: 1, Item: 42
Index: 2, Item: 73
```

In more complex scenarios the difference becomes more significant - `enumerate()`
is cleaner and avoids off-by-one errors.

---

### Looping Two Lists with Indices - the basic way

```python
nums = [1, 42, 73]
letters = ["S", "W", "M"]
for i in range(len(nums)):
    item_1 = nums[i]
    item_2 = letters[i]
    print(f"Index: {i}, Item 1: {item_1}, Item 2: {item_2}")
```

Output:

```
Index: 0, Item 1: 1, Item 2: S
Index: 1, Item 1: 42, Item 2: W
Index: 2, Item 1: 73, Item 2: M
```

---

### Looping Two Lists Using `zip()` and `enumerate()`

```python
nums = [1, 42, 73]
letters = ["S", "W", "M"]
for i, (item_1, item_2) in enumerate(zip(nums, letters)):
    print(f"Index: {i}, Item 1: {item_1}, Item 2: {item_2}")
```

Output:

```
Index: 0, Item 1: 1, Item 2: S
Index: 1, Item 1: 42, Item 2: W
Index: 2, Item 1: 73, Item 2: M
```

---
