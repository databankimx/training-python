## Tuples

A `tuple` is an immutable sequence. Where a list uses square brackets, a
tuple uses parentheses.

---

### Declaring and Accessing Elements

```python
coords = (1, 3)
print(f"x: {coords[0]}, y: {coords[1]}")
```

Output:

```
x: 1, y: 3
```

---

### Immutability

You cannot add, remove, or modify items after initialization:

```python
coords = (1, 3)
coords[0] = 2   # TypeError
```

Output:

```
TypeError: 'tuple' object does not support item assignment
```

A tuple can be rebound to a new value entirely though:

```python
coords = (1, 3)
coords = (2, 3)
print(f"x: {coords[0]}, y: {coords[1]}")
```

Output:

```
x: 2, y: 3
```

---

### Single-Value Tuples

A single-value tuple requires a trailing comma, otherwise Python treats the
parentheses as grouping:

```python
x = (2,)    # tuple
y = (2)     # just the integer 2
print(type(x), type(y))
```

Output:

```
<class 'tuple'> <class 'int'>
```

---

### Looping

```python
dimensions = (3, 4, 5)
for d in dimensions:
    print(d)
```

Output:

```
3
4
5
```

---

### Unpacking

Tuples unpack cleanly into multiple variables:

```python
coords = (1, 3)
x, y = coords
print(f"x: {x}, y: {y}")
```

Output:

```
x: 1, y: 3
```

---

### Zipping Lists into Tuples

`zip()` pairs elements from two lists into a list of tuples:

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))
```

Output:

```
[('a', 1), ('b', 2), ('c', 3)]
```

---

### Warning: `zip()` on Unequal Lists

By default, `zip()` stops at the shortest list with no error:

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]
print(list(zip(letters, numbers)))
```

Output:

```
[('a', 1), ('b', 2), ('c', 3)]
```

The value `4` is silently dropped. To force an error instead, use
`strict=True` (Python 3.10+):

```python
print(list(zip(letters, numbers, strict=True)))
```

Output:

```
ValueError: zip() argument 2 is longer than argument 1
```

---
