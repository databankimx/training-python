## Tuples

A tuple is essentially an immutable list. It holds a sequence of values, and once it's
created, you can't change what's inside it.

To tell a tuple from a list, use parentheses `()` instead of square brackets `[]`:

```python
coords = (1, 3)
```

Tuples can also be written without parentheses, with just commas. That's called *tuple
packing*, and you'll see it in other people's code. The parentheses make the tuple easier
to spot, so they're a good habit to keep.

```python
coords = 1, 3
```

---

### Declaring and Accessing Elements

Elements in a tuple can be read by index, just like elements in a list:

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

Unlike lists, tuples are immutable. You can't add, remove, or change an item once the tuple
exists:

```python
coords = (1, 3)
coords[0] = 2 # TypeError occurs here
```

Output:

```
Traceback (most recent call last):
  File "...\tuple.py", line 2, in <module>
    coords[0] = 2
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

---

Although you can't change a tuple, you can replace it with a new one:

```python
coords = (1, 3)
coords = (2, 3)
print(f"x: {coords[0]}, y: {coords[1]}")
```

Output:

```
x: 2, y: 3
```

The original tuple isn't modified. The name `coords` now points to a different tuple.

---

### Pseudo-Constants

A tuple with a single value needs a comma after that value. Without the comma, Python
sees only parentheses around a number:

```python
x = (2,)
y = (3,)
print(f"x: {x[0]}, y: {y[0]}")
```

Output:

```
x: 2, y: 3
```

Some developers use single-value tuples as pseudo-constants. They aren't truly constant,
since the name can still be reassigned. But an initialized tuple can't be changed in
place, which helps stop data from being modified by accident.

---

### Looping

You can loop over a tuple just like a list:

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

Tuples work especially well with multiple assignment. As we saw in lesson 2.12, you can
unpack one into separate variables:

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

### Zipping Lists

You can join two lists into a list of tuples with `zip()`. It takes the items at each
position and pairs them up:

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
tuples = zip(letters, numbers)
print(list(tuples))
```

Output:

```
[('a', 1), ('b', 2), ('c', 3)]
```

Notice the `list()` call. `zip()` returns an iterator, the same as `reversed()` did in
lesson 3.9. Printing the `zip()` result directly shows an object, not the pairs. Wrap it
in `list()` to see them.

---

### A Warning About `zip()`

Only use `zip()` on lists of the same length. If one list is longer, the extra items are
dropped:

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]
tuples = zip(letters, numbers)
print(list(tuples))
```

Output:

```
[('a', 1), ('b', 2), ('c', 3)]
```

Nothing was added for position 3, where the second list holds `4`. There's no error or
warning. The `4` simply never shows up.

---

#### Making Mismatched Lists Raise a `ValueError`

If you'd rather get an error than lose items quietly, add the `strict=True` argument to
`zip()`. Python checks the lengths and raises an error when they don't match. This
argument arrived in Python 3.10:

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 4]
tuples = zip(letters, numbers, strict=True)
print(list(tuples))
```

Output:

```
Traceback (most recent call last):
  File "...\zip.py", line 4, in <module>
    print(list(tuples))
          ^^^^^^^^^^^^
ValueError: zip() argument 2 is longer than argument 1
```

---

