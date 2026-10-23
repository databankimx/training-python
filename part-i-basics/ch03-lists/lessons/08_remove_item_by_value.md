## Removing Items from a List by Value

Sometimes you know what you want to remove, but not where it sits in the list. Maybe
the value came from user input, or you're checking for a specific item. You can't use
`del` in that case, because `del` needs a position.

Python lists have a `remove()` method for this. Give it a value, and it finds the
first matching item and removes it.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
['yamaha', 'suzuki', 'triumph']
```

Like `append()` and `insert()`, `remove()` changes the list in place and returns `None`.
Don't assign its result to anything.

---

### Removing Based on a Variable

The value can come from a variable, too:

```python
motorcycles = ["honda", "ducati", "suzuki", "triumph"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
```

Output:

```
['honda', 'ducati', 'suzuki', 'triumph']
['honda', 'suzuki', 'triumph']
```

---

### A Warning About Duplicate Values

Lists allow duplicate values. If the value you're removing shows up more than once,
`remove()` only removes the first match:

```python
motorcycles = ["honda", "ducati", "suzuki", "ducati", "triumph"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
```

Output:

```
['honda', 'ducati', 'suzuki', 'ducati', 'triumph']
['honda', 'suzuki', 'ducati', 'triumph']
```

Only the first `ducati` went. The second one is still there. When we get to loops and
conditionals, we'll see how to remove every match.

---

### When the Value Isn't in the List

If you ask `remove()` to remove a value that isn't in the list, Python raises a
`ValueError`:

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
motorcycles.remove("ducati")
```

Output:

```
Traceback (most recent call last):
  File "...\remove_missing.py", line 2, in <module>
    motorcycles.remove("ducati")
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
ValueError: list.remove(x): x not in list
```

A typo in the value is the usual cause. Check the spelling, and check that the value
really is in the list before you call `remove()`.

---
