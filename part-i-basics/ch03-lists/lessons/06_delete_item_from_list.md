## Deleting an Item from a List

The `del` statement removes the item at a given index. The remaining items
renumber automatically.

`del` is a statement rather than a function because a function call only
receives the item value - it has no way to remove that item from the list or
renumber the rest. A statement operates on the list structure directly.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
print(motorcycles[2])

del motorcycles[2]
print(motorcycles[2])
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
suzuki
triumph
['honda', 'yamaha', 'triumph']
```

---

### Deleting All Items

The `clear()` method removes all items from a list without deleting the list
itself.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
motorcycles.clear()
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
[]
```

---
