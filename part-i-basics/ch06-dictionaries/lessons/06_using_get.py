"""Lesson 6.6"""

print("Chapter 6:")
print("Exercise 6 - Using 'get()'")

alien = {"color": "green", "speed": "slow"}

# This line would throw a KeyError because "points" does not exist:
# print(alien["points"])

point_value = alien.get("points", "No point value assigned")
print(point_value)

print(alien.get("color", "No color assigned"))

point_value = alien.get("points")
print(point_value)

print(alien)
