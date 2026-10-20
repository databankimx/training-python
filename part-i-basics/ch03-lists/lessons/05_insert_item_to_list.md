## Insert an Item into a List

Sometimes you will want to add an item to the list but not place it at the end.

Python provides the `insert()` function to provide this capability.

You can insert an item at a specific location by specifying the index of the 
item you're adding

The rest of the list will renumber its indices accordingly.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
print(motorcycles[3])
motorcycles.insert(3, "ducati") # Insert at index 3
print(motorcycles[3])
print(motorcycles[4])
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
triumph
ducati
triumph
['honda', 'yamaha', 'suzuki', 'ducati', 'triumph']
```

---
