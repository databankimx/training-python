## Populate an Empty List

One common way of populating lists is to initialize an empty list `[]` and 
then add items to it during the program execution.

```python
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
motorcycles.append("triumph")
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
```

---

In newer Python versions, SonarQube may flag the use of `append` for adding single items to a list as a potential issue, suggesting the use of `extend` instead. This is because `extend` can add multiple items at once and is generally more efficient for larger lists.

```python
motorcycles = []
motorcycles.extend(["honda"])
motorcycles.extend(["yamaha"])
motorcycles.extend(["suzuki", "triumph"])
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
```

---
