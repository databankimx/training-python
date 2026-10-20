"""Lesson 3.9"""

print("Chapter 3:")
print("Exercise 9 - Sorting Lists")

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

print(f"There are {len(cars)} items in the cars list.")
