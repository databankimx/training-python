## Modifying Values in a Dictionary

Changing a value works just like adding one, except the key already exists. You name the key,
and assign the new value to it:

```python
alien = {"color" : "green", "points" : 5}
print(f"The alien is {alien['color']}")
alien["color"] = "yellow"
print(f"The alien is now {alien['color']}")
```

Output:

```
The alien is green
The alien is now yellow
```

---

### A Real-World Example: A Game

Dictionaries are a natural fit for game objects. Here's an alien that moves across the screen,
with its position and speed stored together:

```python
alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nStart x-position: {alien['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else: # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien["x_position"] = alien["x_position"] + x_increment
print(f"End   x-position: {alien['x_position']}")
```

Output:

```
Start x-position: 0
End   x-position: 2
```

---

### Shorthand with `+=`

Updating a value from its own old value is common enough that Python has a shorthand for it.
The last line of the example can be written this way:

```python
alien["x_position"] += x_increment
```

It means the same thing as `alien["x_position"] = alien["x_position"] + x_increment`. You'll see
both forms in code, so it helps to recognize them.

---

