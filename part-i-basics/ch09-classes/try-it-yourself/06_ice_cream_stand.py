"""Assignment 9.6"""

# Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
#                  Write a class called `IceCreamStand` that inherits from
#                  the `Restaurant` class you wrote in Exercise 9.1 or
#                  Exercise 9.4. Either version of the class will work;
#                  just pick the one you like better. Add an attribute
#                  called `flavors` that stores a list of ice cream flavors.
#                  Write a method that displays these flavors. Create an
#                  instance of `IceCreamStand`, and call this method.

print("Try-it-Yourself:")
print("Assignment 9.6")

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

class IceCreamStand(Restaurant):
    """Defines an Ice Cream Stand as a subclass of Restaurant"""

    def __init__(self, name, cuisine, flavors=None):
        """Initialize a new instance of the IceCreamStand class"""
        super().__init__(name, cuisine)
        self.flavors = flavors if flavors else ["chocolate", "vanilla", "strawberry"]

    def list_flavors(self):
        """Print out a list of the available flavors"""
        print(f"\n{self.name.title()} has the following flavors available:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

    def add_flavor(self, flavor):
        """Add an item to the list of the available flavors"""
        if flavor not in self.flavors:
            self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        """Remove an item from the list of the available flavors"""
        if flavor in self.flavors:
            self.flavors.remove(flavor)

my_stand = IceCreamStand("Frosty Freeze", "ice cream",
                         ["chocolate", "vanilla", "strawberry", "pistachio"])
my_stand.list_flavors()

my_stand.add_flavor("rocky road")
my_stand.list_flavors()

my_stand.remove_flavor("pistachio")
my_stand.list_flavors()
