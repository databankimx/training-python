"""Lesson 9.6a"""

from car import Car

print("Chapter 9:")
print("Exercise 6-a - Importing Classes")

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.set_odometer(23)
my_new_car.read_odometer()
