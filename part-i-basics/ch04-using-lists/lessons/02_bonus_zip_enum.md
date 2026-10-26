## Improving Loops with `enumerate()` and `zip()`

Sometimes you need the position of each item as well as the item itself. Other times
you need to walk two lists side by side. You could handle both with a range of
indexes, and you'd get the job done. But Python has two functions that make these
loops cleaner.

* `enumerate()` returns an *iterable* of pairs, where each pair holds an index and the
  item at that index: `(i, lst[i])`
* `zip()` returns an iterable of pairs that line up items from two lists:
  `(lst_1[n], lst_2[n])`

An *iterable* is anything you can loop over. Lists are iterables, and so are the
objects that `enumerate()` and `zip()` give back.

---

### Looping over the Indexes

Here's the long way to get both the index and the value. It works, but it's a lot of
typing for a simple job:

```python
nums = [1, 42, 73]
print("Looping list on index:")
for i in range(len(nums)):
    item = nums[i]
    print(f"Index: {i}, Item: {item}")
```

Output:

```
Looping list on index:
Index: 0, Item: 1
Index: 1, Item: 42
Index: 2, Item: 73
```

---

### Looping with `enumerate()`

`enumerate()` gives you the index and the value together, so you don't have to look
the value up yourself:

```python
nums = [1, 42, 73]
print("Looping list on enumerate:")
for i, item in enumerate(nums):
    print(f"Index: {i}, Item: {item}")
```

Output:

```
Looping list on enumerate:
Index: 0, Item: 1
Index: 1, Item: 42
Index: 2, Item: 73
```

With a list this small, the difference is minor. In bigger programs, `enumerate()` is a
tool you'll reach for all the time.

---

### Looping Two Lists over the Indexes

When you have two lists, you can use the same index-based approach to walk both at
once:

```python
nums = [1, 42, 73]
letters = ["S", "W", "M"]
print("Looping two lists on index:")
for i in range(len(nums)):
    item_1 = nums[i]
    item_2 = letters[i]
    print(f"Index: {i}, Item 1: {item_1}, Item 2: {item_2}")
```

Output:

```
Looping two lists on index:
Index: 0, Item 1: 1, Item 2: S
Index: 1, Item 1: 42, Item 2: W
Index: 2, Item 1: 73, Item 2: M
```

---

### Looping Two Lists with `zip()` and `enumerate()`

`zip()` pairs up the items from each list, and `enumerate()` adds the index on top:

```python
nums = [1, 42, 73]
letters = ["S", "W", "M"]
print("Looping two lists on enumerate/zip:")
for i, (item_1, item_2) in enumerate(zip(nums, letters)):
    print(f"Index: {i}, Item 1: {item_1}, Item 2: {item_2}")
```

Output:

```
Looping two lists on enumerate/zip:
Index: 0, Item 1: 1, Item 2: S
Index: 1, Item 1: 42, Item 2: W
Index: 2, Item 1: 73, Item 2: M
```

---

### What `zip()` Does with Lists of Different Lengths

`zip()` stops as soon as the shorter list runs out. It doesn't raise an error, so
the items left over in the longer list quietly disappear from the loop:

```python
nums = [1, 42, 73, 99]
letters = ["S", "W", "M"]
for n, letter in zip(nums, letters):
    print(f"{n} {letter}")
```

Output:

```
1 S
42 W
73 M
```

The `99` never gets a turn. If your lists should always be the same length, that's
worth checking before you trust the loop.

---

> **About the `.py` file:** the file wraps these examples in functions, which use `def`
> and type hints such as `list[int]`. Functions are covered in Chapter 8, so for now,
> read those parts as packaging. The loops themselves are the same ones shown above.
>
> The file also loops over a dictionary with `enumerate()` and `.items()`. Dictionaries
> get their own chapter, Chapter 6, so you'll see them again then.

---
