"""Lesson 4.9"""

print("Chapter 4:")
print("Exercise 9 - Tuples")

coords = (1, 3)
print(f"x: {coords[0]}, y: {coords[1]}")

# Tuples are immutable. Uncomment the next two lines to see the TypeError.
# coords[0] = 2
# print(coords)

coords = (2, 3)
print(f"x: {coords[0]}, y: {coords[1]}")

x = (2,)
y = (3,)
print(f"x: {x[0]}, y: {y[0]}")

dimensions = (3, 4, 5)
for d in dimensions:
    print(d)

coords = (1, 3)
x, y = coords
print(f"x: {x}, y: {y}")

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
tuples = zip(letters, numbers)
print(list(tuples))

numbers = [1, 2, 3, 4]
tuples = zip(letters, numbers)
print(list(tuples))

# Uncomment these lines to see the ValueError from strict=True (Python 3.10 and later)
# tuples = zip(letters, numbers, strict=True)
# print(list(tuples))
