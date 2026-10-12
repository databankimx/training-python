## Remove Items from List by Value

Sometimes, you won't know the index of an item you want to remove and won't be 
able to use `del`.

---

### Removing an item:

Python lists expose the `remove()` method to allow you to remove items by value
instead.

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

Of course, you can use a variable to determine what is removed.

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

### A Warning about Duplicate Values

As we already know, lists permit duplicate values.

If a list contains more than one instance of the value you're removing, 
**only the first matching element will be removed**.

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

Note: Only the first instance of "ducati" was removed.

When we review loops and conditionals, we'll see a way to work around this 
limitation.

---
