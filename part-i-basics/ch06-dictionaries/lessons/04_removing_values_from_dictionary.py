"""Lesson 6.4"""

print("Chapter 6:")
print("Exercise 4 - Removing Values from a Dictionary")

alien = {"color": "green", "points": 5}
print(alien)
del alien["points"]
print(alien)

print()

alien = {"color": "green", "points": 5}
points = alien.pop("points")
print(points)
print(alien)

# Uncomment to see the KeyError from deleting the same key twice
# alien = {"color": "green", "points": 5}
# del alien["points"]
# del alien["points"]
