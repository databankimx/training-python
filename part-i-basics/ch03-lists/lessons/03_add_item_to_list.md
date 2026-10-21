## Adding Items to a List

You can add a new item to the end of a list with the `append()` method. A
method is a function that belongs to a particular object, which here is the list.
You call it with a dot, the same way we called `title()` and `upper()` on strings.

```python
motorcycles = ["ducati", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("triumph") # Add a value to the end of the list
print(motorcycles)
```

Output:

```
['ducati', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki', 'triumph']
```

`append()` adds exactly one item, and it goes at the end. The list changes in place,
so you don't need to assign the result anywhere.

---

### Don't Assign the Result of `append()`

Here's the mistake most people make with this method at least once:

```python
motorcycles = ["ducati", "yamaha", "suzuki"]
motorcycles = motorcycles.append("triumph")
print(motorcycles)
```

Output:

```
None
```

`append()` returns `None`, which is Python's way of saying "nothing." It doesn't
hand you the new list. It changes the list you already have. So call it, and leave
the variable alone.

---

The `.py` file for this lesson also prints the number of items before and after
the change, using `len()` as we saw in the last lesson:

```python
motorcycles = ["ducati", "yamaha", "suzuki"]

print(f"{len(motorcycles)} elements")
print(motorcycles)

motorcycles.append("triumph")
print(f"{len(motorcycles)} elements")
print(motorcycles)
```

Output:

```
3 elements
['ducati', 'yamaha', 'suzuki']
4 elements
['ducati', 'yamaha', 'suzuki', 'triumph']
```

---

