"""Lesson 6.3"""

print("Chapter 6:")
print("Exercise 3 - Modifying Values in a Dictionary")

alien = {"color": "green", "points": 5}
print(f"The alien is {alien['color']}")

alien["color"] = "yellow"
print(f"The alien is now {alien['color']}")

alien = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"\nOriginal x-position: {alien['x_position']}")
if alien["speed"] == "slow":
    x_increment = 1
elif alien["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien["x_position"] = alien["x_position"] + x_increment
print(f"New x-position:      {alien['x_position']}")
