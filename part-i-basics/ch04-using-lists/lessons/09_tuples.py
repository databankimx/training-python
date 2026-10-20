"""Lesson 4.9"""

print("Chapter 4:")
print("Exercise 9 - Tuples")

dimensions = (200, 50)
print(f"\nDimensions: {dimensions[0]} x {dimensions[1]}")

three = (3,)

for dim in dimensions:
    print(dim)

print("\nOriginal dimensions:")
for dim in dimensions:
    print(dim)

dimensions = (250, 50)
print("\nModified dimensions:")
for dim in dimensions:
    print(dim)

coordinates = (2, 6)
x, y = coordinates
print(f"\nCoordinates: {coordinates}\nx = {x}\ny = {y}")

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
tuples = zip(letters, numbers)
print()
print(list(tuples))
