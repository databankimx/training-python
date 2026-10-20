"""Assignment 9.4"""

# Number Served: Start with your program from Exercise 9-1. Add an
#                attribute called `number_served` with a default value
#                of 0. Create an instance called `restaurant` from this
#                class. Print the number of customers the restaurant
#                has served, and then change this value and print it again.
#
#                Add a method called `set_number_served()` that lets you
#                set the number of customers that have been served. Call
#                this method with a new number and print the value again.
#
#                Add a method called `increment_number_served()` that lets
#                you increment the number of customers who've been served.
#                Call this method with any number you like that could
#                represent how many customers were served in, say, a day
#                of business.

print("Try-it-Yourself:")
print("Assignment 9.4")

class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()} food!")

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


restaurant = Restaurant("burger heaven", "american")
restaurant.describe()
restaurant.get_number_served()
restaurant.number_served = 10
restaurant.get_number_served()

restaurant.set_number_served(20)
restaurant.get_number_served()

restaurant.increment_number_served(5)
restaurant.get_number_served()
