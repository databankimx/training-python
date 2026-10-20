"""Lesson 3.6"""

print("Chapter 3:")
print("Exercise 6 - Deleting an Item from a List")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"\n{len(motorcycles)} elements")
print(motorcycles)

del motorcycles[2]
print(f"\n{len(motorcycles)} elements")
print(motorcycles[2])
print(motorcycles)

motorcycles.clear()
print(f"\n{len(motorcycles)} elements")
print(motorcycles)
