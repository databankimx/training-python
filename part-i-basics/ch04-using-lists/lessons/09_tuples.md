## Tuples

A `tuple` in Python is essentially an immutable list.

To distinguish that a collection is a tuple in stead of a list, we use 
parentheses instead of square brackets when we initialize the variable.

---

### Declaring and Accessing Elements

Elements in a tuple can be read by index just like elements in a list.

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

Unlike lists, tuples are immutable. You cannot add, remove, or modify items
after the tuple is initialized.


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

Although tuples cannot be mutated, they can be replaced/reinitialized.

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

### Pseudo-Constants

A tuple can have just one value, but the value must be followed by a comma.

Some developers use these single-value tuples to create pseudo-constant
variables. They aren't truly constant, but the immutability of an initialized
tuple helps prevent inadvertent modification of data.

```python
x = (2,)
y = (3,)
print(f"x: {x[0]}, y: {y[0]}")
```

Output:

```
x: 2, y: 3
```

---

### Looping

You can loop across a tuple, just like a list

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

Tuples are especially well suited to being deconstructed using multiple 
assignment (we call this "unpacking").

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

You can join two lists into a single list of tuples using the `zip()` 
function.

This takes the elements at each index in the lists and creates a tuple to 
populate at that index in a new list.

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

---

### Warning on `zip()`

Be careful to only use `zip()` on lists of the same length. If one of the 
lists has more elements than the other, only the indices where both lists 
contain a value will be populated in the resulting tuple list.

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

No values were added for index 3, which contains the value `4` in the
second list.

---

#### Making Mismatched Lists Throw a `ValueError`

Normally, you don't receive an error or warning. You just don't receive
the extra values from the list with more elements.

However, you can add the optional argument `strict=True` to the `zip()` call
to force an error instead when we try to use the results.

This argument was added in Python 3.10.

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
