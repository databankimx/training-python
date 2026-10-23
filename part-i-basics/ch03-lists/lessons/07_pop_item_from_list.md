## Popping an Item from a List

Sometimes you want to take an item off a list and use it right away. The `del`
statement removes an item, but it doesn't hand the item back to you. For that, Python
lists have the `pop()` method. It removes an item and returns its value, so you can
store it or print it.

The name comes from picturing the list as a stack of plates. You pop one off the top,
and the top of the stack is the end of the list.

---

### Pop the Last Item

By default, `pop()` removes the last item and returns it:

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

The `popped` variable holds `triumph`, and the list no longer has it.

---

### Pop a Different Item

`pop()` also takes an optional position, so you can remove an item from anywhere in
the list. The item at that position is removed and returned:

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

Everything after position 1 shifts one place to the left to close the gap.

---

### Pop Is Not Free

Removing the last item is quick. Removing an item from the front, with `pop(0)`, is
slower on a long list. Every other item has to shift left to fill the gap. For a
list of four motorcycles, you won't notice. For a list of a million items, you will.

If you find yourself removing from the front a lot, keep that cost in mind. It's a
good reason to choose a different structure, and Python has several.

---
