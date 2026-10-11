"""Lesson 3.8"""

print("Chapter 3:")
print("Exercise 8 - Removing an Item from a List by Value")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]

print(f"{len(motorcycles)} elements")
print(motorcycles)

motorcycles.remove("honda")
print(f"{len(motorcycles)} elements")
print(motorcycles)

too_expensive = "ducati"
motorcycles.append(too_expensive)
print(f"{len(motorcycles)} elements")
print(motorcycles)

# CAUTION - If a value exists more than once in a list,
#           list.remove(value) only removes the first occurrence
motorcycles.remove(too_expensive)
print(f"I removed '{too_expensive}', because it's too expensive...")
print(f"{len(motorcycles)} elements")
print(motorcycles)
