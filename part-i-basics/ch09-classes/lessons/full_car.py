# Note: While we're including multiple classes in this file, it is because they are related.
#       It's smart in the real world to separate unrelated classes in separate modules
#       In lesson 9.11, we will separate these

# Include a module-level doc string
"""A set of classes used to represent gas and electric cars"""

class Car:
    """Define a car"""

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initialize a new instance of the Car class

        Parameters:  
        * **make**: Manufacturer of the car
        * **model**: Model name of the car
        * **year**: Model year of the car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_level = 0

    def get_descriptive_name(self) -> str:
        """
        Describe the car
        
        **Returns**:  
        Description of the car
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self) -> None:
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")

    def set_odometer(self, mileage: int) -> None:
        """
        Set the odometer mileage
        
        Parameters:
        * **mileage**: Number of miles on the odometer
        """
        if mileage >= self.odometer_reading:
            print(f"Setting odometer to {mileage}")
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int=1) -> None:
        """
        Increment the odometer mileage
        
        Parameters:
        * **miles**: Number of miles to add to the odometer
        """
        if miles > 0:
            self.odometer_reading += miles
            print(f"Updated odometer to {self.odometer_reading}")
        else:
            print("You can't add negative miles!")

    def fill_gas_tank(self) -> None:
        """Set the fuel level to full"""
        self.fuel_level = 1

    def check_fuel_level(self) -> None:
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
    """ Define an electric car as a subclass of Car"""

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initialize a new instance of the ElectricCar class

        Parameters:  
        * **make**: Manufacturer of the car
        * **model**: Model name of the car
        * **year**: Model year of the car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self) -> None:
        """Set the fuel level to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self) -> None:
        """Get the fuel level"""
        print("This car doesn't contain any fuel!\n")


class Battery:
    """Define a battery"""

    def __init__(self, battery_size: int=75) -> None:
        """
        Initialize a new instance of the Battery class

        Parameters:  
        * **battery_size**: Battery size (in kWh)
        """
        self.battery_size = battery_size

    def describe_battery(self) -> None:
        """Describe the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self) -> None:
        """Get the battery range in miles"""
        battery_range = "unknown"
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
        print(f"This car can go about {battery_range} miles on a full charge.\n")

    def upgrade_battery(self) -> None:
        """Upgrade the battery"""
        if self.battery_size < 100:
            self.battery_size = 100
            print("Upgraded battery.")
