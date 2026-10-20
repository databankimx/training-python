"""Assignment 8.14"""

# Cars: Write a function that stores information about a car in a
#       dictionary. The function should always receive a manufacturer
#       and a model name. It should then accept an arbitrary number
#       of keyword arguments. Call the function with the required
#       information and two other name-value pairs, such as a color
#       or an optional feature. Your function should work for a call
#       like this one:
#       -------------------------------------------------------------------
#       car = make_car("subaru", "outback", color="blue", tow_package=True)
#       -------------------------------------------------------------------
#       Print the dictionary that's returned to make sure all the
#       information was stored correctly.

print("Try-it-Yourself:")
print("Assignment 8.14")

def make_car(make, model, **details):
    """Create a dictionary describing a car"""
    details["Make"] = make.title()
    details["Model"] = model.title()
    return details

car = make_car("dodge", "challenger", color="header orange",
               feature="shaker", year=2014)
print(car)
