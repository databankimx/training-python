"""Lesson 9.2"""

print("Chapter 9:")
print("Exercise 2 - Working with Attributes")

class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()
print(my_new_car.odometer_reading)

# The expanded class replaces the one above for the rest of this file.
class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, mileage):
        """Set the odometer mileage"""
        if mileage >= self.odometer_reading:
            print(f"Setting odometer to {mileage}")
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles=1):
        """Increment the odometer mileage"""
        if miles > 0:
            self.odometer_reading += miles
            print(f"Updated odometer to {self.odometer_reading}")
        else:
            print("You can't add negative miles!")

my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()

# Modifying attributes directly
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()
print()

my_new_car.odometer_reading = 15_000
my_new_car.read_odometer()
print()

my_new_car.odometer_reading = -1_000
my_new_car.read_odometer()
print()

my_new_car.odometer_reading += 2_000
my_new_car.read_odometer()
print()

my_new_car.odometer_reading -= 1_001
my_new_car.read_odometer()
print()

# The set_odometer() method
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()
print()

my_new_car.set_odometer(14_000)
my_new_car.read_odometer()
print()

my_new_car.set_odometer(-1_000)
my_new_car.read_odometer()
print()

# The increment_odometer() method
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()
print()

my_new_car.increment_odometer()
my_new_car.read_odometer()
print()

my_new_car.increment_odometer(1_000)
my_new_car.read_odometer()
print()

my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
print()
