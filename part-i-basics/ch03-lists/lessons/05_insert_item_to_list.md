## Insert an Item into a List

Sometimes you want to add an item somewhere other than the end of a list. The
`insert()` method handles that. Give it a position and a value, and it puts the
value at that spot.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
motorcycles.insert(3, "ducati") # Insert at position 3
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
['honda', 'yamaha', 'suzuki', 'ducati', 'triumph']
```

Everything from position 3 onward shifts one place to the right to make room. The
new item takes position 3, and `triumph` moves to position 4. The positions of the
items before it don't change.

Here's the same list, shown item by item:

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
motorcycles.insert(3, "ducati")
print(motorcycles[3])
print(motorcycles[4])
```

Output:

```
ducati
triumph
```

---

### Inserting Past the End

`append()` adds to the end of a list. `insert()` can do that too, if you give it a
position past the end:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(10, "ducati")
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'ducati']
```

This is different from lesson 2, where assigning to a missing position raised an
`IndexError`. `insert()` doesn't fail. It quietly places the item at the end. If you
want the error, use assignment. If you want the item added, `insert()` is happy to
do it.

---

### Negative Positions

Negative positions work with `insert()`, the same way they work with indexing. A
position of `-1` puts the new item in front of the last one:

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
motorcycles.insert(-1, "ducati")
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'ducati', 'triumph']
```

---

The `.py` file for this lesson also prints the number of items before and after the
insert, using `len()`:

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"{len(motorcycles)} elements")
print(motorcycles)

motorcycles.insert(3, "ducati")
print(f"{len(motorcycles)} elements")
print(motorcycles[4])
print(motorcycles)
```

Output:

```
4 elements
['honda', 'yamaha', 'suzuki', 'triumph']
5 elements
triumph
['honda', 'yamaha', 'suzuki', 'ducati', 'triumph']
```

---
