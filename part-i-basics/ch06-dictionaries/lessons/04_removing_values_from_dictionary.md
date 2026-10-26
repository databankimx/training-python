## Removing Values from a Dictionary

Like lists, you can remove items from a dictionary with the `del` keyword:

Syntax:
`del my_dictionary[my_key]`

```python
alien = {"color" : "green", "points" : 5}
print(alien)
del alien["points"]
print(alien)
```

Output:

```
{'color': 'green', 'points': 5}
{'color': 'green'}
```

`del` removes the key and its value, and that's all it does. It doesn't hand the value back.

---

### Removing a Key and Getting Its Value Back

If you want the value as well, use the `pop()` method. It removes the key, and returns the value
stored under it:

```python
alien = {"color": "green", "points": 5}
points = alien.pop("points")
print(points)
print(alien)
```

Output:

```
5
{'color': 'green'}
```

This is the same idea as `pop()` for lists in lesson 3.7, where the removed item comes back to you.

---

### Removing a Key That Doesn't Exist

Deleting a key that isn't in the dictionary raises a `KeyError`. The same thing happens if you try
to delete the same key twice:

```python
alien = {"color": "green", "points": 5}
del alien["points"]
del alien["points"]
```

Output:

```
Traceback (most recent call last):
  File "...\del_twice.py", line 3, in <module>
    del alien["points"]
        ~~~~~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'points'
```

Check that the key is there with `in` before you delete it, if there's any chance it isn't.

---
