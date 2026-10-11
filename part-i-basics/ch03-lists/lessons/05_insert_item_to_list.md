## Insert an Item into a List

`insert()` adds an item at a specific index. The rest of the list shifts right
and its indices renumber accordingly.

```python
motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
print(motorcycles[3])
motorcycles.insert(3, "ducati")
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
