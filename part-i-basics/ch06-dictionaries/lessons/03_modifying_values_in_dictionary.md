## Modifying Values in a Dictionary

Changing a value is just like adding a new one, except you specify a key that 
already exists.

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

### Real_world Scenario : A Game

Here's the book example for a real-world (game) scenario

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
