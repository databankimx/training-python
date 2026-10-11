## Popping an Item from a List

`pop()` removes an item from the list and returns its value so you can use
it immediately.

---

### Pop the Last Item

By default, `pop()` removes and returns the last item.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
popped = motorcycles.pop()
print(popped)
print(motorcycles)
```

Output:

```
triumph
['honda', 'yamaha', 'suzuki']
```

We will use `pop()` without an argument when we model a **stack** in a later
chapter.

---

### Pop a Specific Item

Pass an index to remove and return a different item.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
popped = motorcycles.pop(1)
print(popped)
print(motorcycles)
```

Output:

```
yamaha
['honda', 'suzuki', 'triumph']
```

We will use `pop(0)` when we model a **queue** in a later chapter.

---
