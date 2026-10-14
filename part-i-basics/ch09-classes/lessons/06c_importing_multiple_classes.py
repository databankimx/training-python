"""Lesson 9.6c"""

from full_car import Car, ElectricCar

print("Chapter 9:")
print("Exercise 6-c - Importing Multiple Classes")

my_gas_car = Car("volkswagen", "beetle", 1967)
print(my_gas_car.get_descriptive_name())

my_e_car = ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
