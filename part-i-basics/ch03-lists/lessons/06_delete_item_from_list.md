## Deleting an Item from a List

The `del` keyword provides the ability to delete the item at a given index from
a list.

Because of the complexity of operations performed by `del`, it exists as a 
statement, not as a function, so the syntax does not include the use of 
parentheses for the argument.

After deleting the item at the specified index, the remaining list is 
renumbered automatically.

> ### Why can't `del` be a function?
> 
> * If we had a function where we pass the item, like `del(my_list[1])`, the
>   interpreter would only have awareness of the item, not of the list itself, 
>   so it couldn't:
>     * Remove the item from the list
>     * Renumber the remaining items
> 
> * If we pass the list itself, `del(my_list)`, the function would not know
>   what index to remove.
> 
> * We could in theory pass two separate arguments (the list and the index) 
>   like `del(my_list, 1)`, but this unnecessarily complicates the call and
>   moves away from the standard list-index syntax.
>
> Based on these factors, the decision was made to have `del` exist as a 
> statement, which is executed differently from a function.

---

### Code Sample

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

### Deleting All Items from a List

Additionally, the list type has a `clear()` method that deletes all items from 
the list but does not delete the list itself.

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
