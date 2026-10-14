"""Lesson 9.6e"""

from electric_car import ElectricCar as EC

print("Chapter 9:")
print("Exercise 6-e - Using an Alias for an Imported Class")

my_e_car = EC("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
