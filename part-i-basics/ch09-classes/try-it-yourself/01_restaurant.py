"""Exercise 9.1"""

# Restaurant: Make a class called Restaurant. The `__init__()` method for
#             Restaurant should store two attributes: a `restaurant_name`
#             and a `cuisine_type`. Make a method called `describe_restaurant()`
#             that prints these two pieces of information, and a method called
#             `open_restaurant()` that prints a message indicating that the
#             restaurant is open. Make an instance called `restaurant` from
#             your class. Print the two attributes individually, and then
#             call both methods.

print("Try-it-Yourself:")
print("Assignment 9.1")

class Restaurant:
    """Defines a restaurant object"""
    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Print a description of the restaurant"""
        print(f"{self.name.title()} proudly serves {self.cuisine.title()}")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

restaurant = Restaurant("the mad greek", "greek & indian food")
print(restaurant.name.title())
print(restaurant.cuisine.title())
restaurant.describe()
restaurant.open()
