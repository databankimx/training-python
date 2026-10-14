"""Class to model a Restaurant"""

class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

    def get_number_served(self):
        """Get the number of people served by the restaurant"""
        print(f"We have served {self.number_served} people today.\n")

    def set_number_served(self, num):
        """Set the number of people served by the restaurant"""
        if num >= self.number_served:
            self.number_served = num
            print(f"Set number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

    def increment_number_served(self, num=1):
        """Increment the number of people served by the restaurant"""
        if num >= 0:
            self.number_served += num
            print(f"Incremented number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")
