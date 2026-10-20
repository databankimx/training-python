"""Exercise 9.2"""

# Three Restaurants: Start with your class from Exercise 9.1. Create
#                    three different instances from the class, and call
#                    `describe_restaurant()` for each instance.

print("Try-it-Yourself:")
print("Assignment 9.2")

class Restaurant:
    """Defines a restaurant object"""
    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Print a description of the restaurant"""
        print(f"{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

restaurant_1 = Restaurant("The Mad Greek", "Greek & Indian food")
restaurant_2 = Restaurant("Charley's Crab", "seafood")
restaurant_3 = Restaurant("The Brown Derby", "steak")

restaurant_1.describe()
restaurant_2.describe()
restaurant_3.describe()
