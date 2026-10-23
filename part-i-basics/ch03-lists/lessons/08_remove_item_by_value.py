"""Lesson 3.8"""

print("Chapter 3:")
print("Exercise 8 - Removing an Item from a List by Value")

motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)

# Removing a value held in a variable
motorcycles = ["honda", "ducati", "suzuki", "triumph"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)

# CAUTION - If a value exists more than once in a list,
#           list.remove(value) only removes the first occurrence
motorcycles = ["honda", "ducati", "suzuki", "ducati", "triumph"]
motorcycles.remove(too_expensive)
print(motorcycles)

# Uncomment the next two lines to see the ValueError for a missing value
# motorcycles = ["honda", "yamaha", "suzuki", "triumph"]
# motorcycles.remove("ducati")
