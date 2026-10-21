## Nesting Dictionaries in a List

Programs often need collections of collections: lists of lists, lists of tuples, or lists of
dictionaries. A list of dictionaries is one of the most useful.

When one dictionary describes an object, there may be many objects with the same properties.
It makes more sense to store those dictionaries in a list than to keep a large group of
separate variables.

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

Usually, you'll build a list like this in a loop, rather than writing separate variables.

Here's an example where you need thirty aliens:

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

The loop variable here is `_`. Python programmers use `_` as a throwaway name when the loop needs to
run a set number of times, but the value itself isn't used.

> **A warning about copies:** each pass of the loop creates a new dictionary, so each alien is
> independent. Compare that with multiplying a list:
>
> ```python
> aliens = [{"color": "green", "points": 5}] * 3
> aliens[0]["color"] = "red"
> print(aliens)
> ```
>
> Output:
>
> ```
> [{'color': 'red', 'points': 5}, {'color': 'red', 'points': 5}, {'color': 'red', 'points': 5}]
> ```
>
> `* 3` puts the same dictionary in all three slots, so changing one changes them all. We saw the same
> idea with copying lists in lesson 4.8. Build the list in a loop, as above, when each item needs to be
> its own dictionary.

---

### Modify Dictionaries in a List

You can change a group of dictionaries by looping over a slice of the list:

```python
num_aliens = 30
aliens = []
for _ in range(num_aliens):
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

