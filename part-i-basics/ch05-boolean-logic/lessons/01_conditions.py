"""Lesson 5.1"""

print("Chapter 5:")
print("Exercise 1 - Handling Conditions")

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
