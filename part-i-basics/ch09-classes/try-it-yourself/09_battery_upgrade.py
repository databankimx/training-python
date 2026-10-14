"""Assignment 9.9"""

# Battery Upgrade: Use the final version of `electric_car.py` from this
#                  section. Add a method to the `Battery` class called
#                  `upgrade_battery()`. This method should check the
#                  battery size and set the capacity to 100 if it isn't
#                  already. Make an electric car with a default battery
#                  size, call `get_range()` once, and then call
#                  `get_range()`a second time after upgrading the battery.
#                  You should see an increase in the car's range.

print("Try-it-Yourself:")
print("Assignment 9.9")

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

    def fill_gas_tank(self):
        """Set the fuel level to full"""
        self.fuel_level = 1

    def check_fuel_level(self):
        """Get the fuel level"""
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
    """Define an electric car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Set the fuel level to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Get the fuel level"""
        print("This car doesn't contain any fuel!\n")


class Battery:
    """Define a battery"""

    def __init__(self, battery_size=75):
        """Initialize a new instance of the Battery class"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Get the battery range"""
        battery_range = "unknown"
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
        print(f"This car can go about {battery_range} miles on a full charge.\n")

    def upgrade_battery(self):
        """Upgrade the battery"""
        if self.battery_size < 100:
            self.battery_size = 100
            print("Upgraded battery.")


my_nissan = ElectricCar("nissan", "leaf", 2024)
print(my_nissan.get_descriptive_name())

my_nissan.battery.describe_battery()
my_nissan.battery.get_range()

my_nissan.battery.upgrade_battery()
my_nissan.battery.describe_battery()
my_nissan.battery.get_range()
