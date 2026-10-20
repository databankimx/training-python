## Improving Loops with the `enumerate()` and `zip()` Functions

There will be times when you need to access the indices as well as the 
values when looping over a list or loops over two lists at the same time.

Of course, you can just loop over a range of indices, but we have a couple
of functions that can improve how we're doing this:

* `enumerate()`: returns an `iterable` (like the generic form of a list) 
  of tuples, where each tuple contains (`i`, `lst[i]`)
* `zip()`: returns an `iterable` of tuples, where each tuple contains
  (`lst_1[n]`, `lst_2[n]`)

---

### Looping a List over the Indices

This is the somewhat noob-ish way to loop over a list getting the indices 
and values:

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

### Looping a List Using `enumerate()`

We can improve this by using the `enumerate()` function to get the indices
and values together:

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

ALthough this small example makes the difference trivial, in more complex
scenarios, `enumerate()` will be a great tool to have in your arsenal.

---

### Looping Two Lists over the Indices

When working with two lists at once, we again could iterate over the 
indices:

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

### Looping Two Lists Using `zip()` and `enumerate()`

Alternately, we can `zip()` the lists and then use `enumerate()`

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
