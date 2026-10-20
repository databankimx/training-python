"""Lesson 9.6b"""

from electric_car import ElectricCar

print("Chapter 9:")
print("Exercise 9 - Importing Inherited Classes")

my_e_car = ElectricCar("nissan", "leaf", 2024)

print(my_e_car.get_descriptive_name())

my_e_car.battery.describe_battery()
my_e_car.battery.get_range()
