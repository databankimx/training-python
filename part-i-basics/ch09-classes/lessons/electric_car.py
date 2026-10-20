"""A class module to define an electric car"""

from car import Car

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
