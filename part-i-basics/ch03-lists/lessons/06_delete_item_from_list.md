## Deleting an Item from a List

The `del` keyword removes the item at a given index from a list:

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

Once `suzuki` is gone, the items after it shift one place to the left. `triumph`
moves into position 2. The items before the gap stay where they were.

---

### Why `del` Isn't a Function

You might expect `del` to be a function, since it does something to a list. It
isn't, and the reason comes down to how functions receive their arguments.

When you pass something to a function, the function gets the *value*, not the
place where that value lives. If `del` were a function, `del(motorcycles[2])` would
hand the function the string `"suzuki"`. The function would have no idea which list
it came from, so it couldn't remove the item.

Passing the whole list, `del(motorcycles)`, has a different problem. The function
gets the list, but not a position, so it doesn't know what to delete.

`del` is part of Python's grammar instead. It works on the place a name or an item
refers to, which is why you write it as a statement, with no parentheses.

---

### `del` Can Also Remove a Variable

`del` doesn't only remove items. It can also delete a variable name:

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
del motorcycles
print(motorcycles)
```

Output:

```
Traceback (most recent call last):
  File "...\del_variable.py", line 3, in <module>
    print(motorcycles)
          ^^^^^^^^^^^
NameError: name 'motorcycles' is not defined
```

Once the name is gone, Python has nothing to find. You won't use this often, but
it's good to know what `del` can do.

---

### Deleting All Items from a List

If you want to keep the list but empty it, use the `clear()` method. The list still
exists, and it just has nothing in it:

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
