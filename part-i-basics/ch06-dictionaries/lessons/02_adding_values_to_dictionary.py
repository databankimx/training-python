"""Lesson 6.2"""

print("Chapter 6:")
print("Exercise 2 - Adding Values to a Dictionary")

alien = {"color": "green", "points": 5}
print(alien)

alien["x_position"] = 0
alien["y_position"] = 25
print(alien)

print()

# Assigning to an existing key replaces its value
alien = {"color": "green", "points": 5}
alien["points"] = 10
print(alien)

print()

alien = {}
alien["color"] = "blue"
alien["points"] = 10
print(alien)
