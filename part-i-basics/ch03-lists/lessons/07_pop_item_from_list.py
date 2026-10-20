"""Lesson 3.7"""

print("Chapter 3:")
print("Exercise 7 - Popping an Item from a List")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"\n{len(motorcycles)} elements")
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(f"\nI popped '{popped_motorcycle}'...")
print(f"{len(motorcycles)} elements")
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
print(f"\nI popped '{popped_motorcycle}'...")
print(f"{len(motorcycles)} elements")
print(motorcycles)
