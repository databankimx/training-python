"""Lesson 9.6d"""

import electric_car

print("Chapter 9:")
print("Exercise 6-d - Importing Module that Imports Another Module")

my_e_car = electric_car.ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())

# This would result in a NameError
# my_car = Car("volkswagen", "beetle", 2019)
# print(my_car.get_descriptive_name())
