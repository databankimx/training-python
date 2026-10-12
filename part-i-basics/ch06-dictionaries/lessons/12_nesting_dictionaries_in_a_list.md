## Nesting Dictionaries in a List

Frequently a program will require collections of collections (lists of lists, 
lists of tuples, etc.).

---

### A List of Dictionaries

When a dictionary defines various properties of an object, it's reasonable to
assume that there may be more than one object with those same collections of 
properties.

For a scenario like that, it makes more sense to store the dictionaries
together in a list than to maintain a large group of standalone variables.

```python
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
```

Output:

```
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

---

### Populating a List of Dictionaries

Commonly, we will populate a list like this iteratively instead of using
separate variables like we did above.

Take an example where you require a certain number of objects:

```python
num_aliens = 30
aliens = []
for _ in range(num_aliens):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
print(len(aliens), aliens[0])
```

Output:

```
30 {'color': 'green', 'points': 5, 'speed': 'slow'}
```

---

### Modify Dictionaries in a List

We can modify a group of elements using a slice of the list.

```python
num_aliens = 30
aliens = []
for alien_number in range(num_aliens):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
for alien in aliens[:5]:
    print(alien)
```

Output:

```
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
```

---
