## Popping an Item from a List

Sometimes you want to remove items from the list as you use them. In such a
case, it is useful to have a method that deletes the item from the list while
simultaneously returning the value that was stored in the removed item.

For this purpose, Python lists implement the `pop()` method.

---

### Pop the Last Item

By default, `pop()` will remove the last item from the list and capture its 
value to use immediately.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
popped = motorcycles.pop()
print(popped)
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
triumph
['honda', 'yamaha', 'suzuki']
```

In a later chapter, when we discuss modeling a `stack`, we will use `pop()`.

---

### Pop a Different Item

Although originally created solely to remove and capture the last item from a
list, subsequent improvements on the `pop()` method allow passing an index to
specify a different item to remove and capture.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
popped = motorcycles.pop(1)
print(popped)
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
yamaha
['honda', 'suzuki', 'triumph']
```

In a later chapter, when we discuss modeling a `queue`, we will use `pop(0)`.

---
