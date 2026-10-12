"""Lesson 3.4"""

print("Chapter 3:")
print("Exercise 4 - Populating an empty List")

motorcycles = []
motorcycles.append("honda") #NOSONAR
motorcycles.append("yamaha")
motorcycles.append("suzuki")
motorcycles.append("triumph")
print(motorcycles)

motorcycles = []
motorcycles.extend(["honda"])
motorcycles.extend(["yamaha"])
motorcycles.extend(["suzuki", "triumph"])
print(motorcycles)
