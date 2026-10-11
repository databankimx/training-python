## Using Slices to Copy Lists

An unbounded slice (`[:]`) of a list creates a shallow copy. This is useful
when you want to work with a copy without modifying the original.

---

### Assignment Copies the Reference, Not the Data

When you assign a list to a new variable, both variables point to the same
list in memory. Python variables hold references, not data directly.

```python
my_foods = ["pizza", "falafel", "carrot cake"]
other_foods = my_foods          # both point to the same list
other_foods.append("gyros")
print(other_foods)
print(my_foods)                 # also changed!
```

Output:

```
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake', 'gyros']
```

---

### A Slice Creates a New List

```python
my_foods = ["pizza", "falafel", "carrot cake"]
other_foods = my_foods[:]       # unbounded slice creates a copy
other_foods.append("gyros")
print(other_foods)
print(my_foods)                 # unchanged
```

Output:

```
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake']
```

---

### Note on Shallow vs Deep Copies

`[:]` creates a *shallow* copy - the new list is independent, but any mutable
objects *inside* it (nested lists, dicts) are still shared references. For
lists of simple values (strings, numbers) this distinction does not matter.
For nested structures, use `copy.deepcopy()`.

---
