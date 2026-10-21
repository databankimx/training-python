"""Lesson 6.1"""

print("Chapter 6:")
print("Exercise 1 - Simple Dictionaries")

alien = {"color": "green", "points": 5}
print(alien["color"])
print(alien["points"])

print()

# Duplicate keys: the later value replaces the earlier one
alien = {"color": "green", "points": 5, "color": "red"} #pylint: disable=duplicate-key #NOSONAR
print(alien)

print()

print("color" in alien)
print("speed" in alien)

print()

squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

# Uncomment to see the TypeError for a list used as a key
# alien = {["color"]: "green"}

# Uncomment to see the KeyError for a missing key
# alien = {"color": "green", "points": 5}
# print(alien["speed"])
