"""Lesson 9.5"""

print("Chapter 9:")
print("Exercise 5 - Classes as Attributes")

class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_level = 0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")

    def set_odometer(self, mileage):
        """Set the odometer mileage"""
        # Let's prevent anyone from "rolling back" the odometer
        if mileage >= self.odometer_reading:
            print(f"Setting odometer to {mileage}")
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increment the odometer mileage"""
        if miles > 0:
            self.odometer_reading += miles
            print(f"Updated odometer to {self.odometer_reading}")
        else:
            print("You can't add negative miles!")

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        self.fuel_level = 1

    def check_fuel_level(self):
        """Check the fuel level"""
        fuel_state = "empty"
        if self.fuel_level == 1.0:
            fuel_state = "full"
        elif self.fuel_level >= 0.75:
            fuel_state = "three quarters full"
        elif self.fuel_level >= 0.5:
            fuel_state = "half full"
        elif self.fuel_level >= 0.25:
            fuel_state = "one quarter full"
        elif self.fuel_level > 0.0:
            fuel_state = "running on fumes"
        print(f"Fuel Status: {fuel_state}\n")


class ElectricCar(Car):
    """Defines an Electric Car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Check the fuel level"""
        print("This car doesn't contain any fuel!\n")


class Battery:
    """Defines a battery"""
    def __init__(self, battery_size=75):
        """Initialize a new instance of the Battery class"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Get the range of the battery"""
        battery_range = "unknown"
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
        else:
            print(f"Range unknown for battery size: {self.battery_size}-kWh.")
            return
        print(f"This car can go about {battery_range} miles on a full charge.")


my_e_car = ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())

my_e_car.battery.describe_battery()
my_e_car.battery.get_range()
