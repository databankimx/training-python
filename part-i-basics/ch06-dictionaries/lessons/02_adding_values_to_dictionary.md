## Adding Values to Dictionaries

You can add a new value to a dictionary by assigning it to a new key:

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

The new keys go at the end, because dictionaries keep their insertion order (see lesson 6.1).

---

### Assigning to an Existing Key

Assigning to a key that's already in the dictionary doesn't add anything. It replaces the value
stored under that key:

```python
alien = {"color": "green", "points": 5}
alien["points"] = 10
print(alien)
```

Output:

```
{'color': 'green', 'points': 10}
```

Assignment is how you both add and change values. Python decides which one you mean by checking
whether the key is already there.

---

### Starting Empty

You can also start with an empty dictionary, and add values as you need them:

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

Be careful with the braces. `{}` is an empty dictionary. An empty set is written `set()`, because
`{}` on its own already means a dictionary.

---

