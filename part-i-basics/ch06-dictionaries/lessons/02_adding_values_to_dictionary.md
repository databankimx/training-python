## Adding Values to Dictionaries

You can add a new value to a dictionary by simply populating a new key

```python
alien = {"color" : "green", "points" : 5}
print(alien)
alien["x_position"] = 0
alien["y_position"] = 25
print(alien)
```

Output:

```
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

---

### Starting Empty

You can also start with an empty dictionary and add values as you need them

```python
alien = {}
alien["color"] = "blue"
alien["points"] = 10
print(alien)
```

Output:

```
{'color': 'blue', 'points': 10}
```

---
