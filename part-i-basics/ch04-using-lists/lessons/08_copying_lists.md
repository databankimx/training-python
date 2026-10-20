## Using Slices to Copy Lists

An unbounded slice of a list creates a copy of the original list.

This can be very useful when you don't want to modify the original.

---

### Lists Assign as the Same Item in Memory

If we create a list and then assign it to a new variable, both variables are
pointing to the same list in memory.

This happens because the variable only contains the pointer to the memory 
location where the list data is stored. It takes both more memory and more
CPU time to create a copy, so the default behavior is just to copy the 
address (or *reference*), which means that both variables point to the same 
data.

In Python:

* All variables are passed and assigned by reference, but
    * All *mutable* data types assign as the same item in memory
    * All *immutable* data types are assigned as copies

```python
my_foods = ["pizza", "falafel", "carrot cake"]
print(my_foods)
other_foods = my_foods # Assignment is by reference
other_foods.append("gyros")
print(other_foods)
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake', 'gyros']
```

Appending a value to `other_foods` modified `my_foods`, since both are 
references to the same list.

---

### Slices Make Copies

But if we assign to a slice, we're creating the copy as a new list in memory.

```python
my_foods = ["pizza", "falafel", "carrot cake"]
print(my_foods)
other_foods = my_foods[:] # Unbounded slice makes a copy/clone
other_foods.append("gyros")
print(other_foods)
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake']
```

Appending to the copied list did not modify the original.

---

### Note on Shallow vs Deep Copies

`[:]` creates a *shallow* copy - the new list is independent, but any mutable
objects *inside* it (nested lists, dicts) are still shared references. For
lists of simple values (strings, numbers) this distinction does not matter.
For nested structures, use `copy.deepcopy()`.

---
