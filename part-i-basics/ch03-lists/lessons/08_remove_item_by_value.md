## Remove Items from a List by Value

When you do not know the index of the item you want to remove, use `remove()`.

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

---

### Removing Based on a Variable

```python
motorcycles = ["honda", "ducati", "suzuki", "triumph"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
```

Output:

```
['honda', 'suzuki', 'triumph']
```

---

### Warning: Duplicate Values

If the value appears more than once, `remove()` only removes the **first**
matching element.

```python
motorcycles = ["honda", "ducati", "suzuki", "ducati", "triumph"]
motorcycles.remove("ducati")
print(motorcycles)
```

Output:

```
['honda', 'suzuki', 'ducati', 'triumph']
```

When we cover loops and conditionals, we will see how to remove all instances
of a value.

---
