"""Assignment 8.12"""

# Sandwiches: Write a function that accepts a list of items a person
#             wants on a sandwich. The function should have one
#             parameter that collects as many items as the function
#             call provides, and it should print a summary of the
#             sandwich that's being ordered. Call the function three
#             times, using a different number of arguments each time.

print("Try-it-Yourself:")
print("Assignment 8.12")

def make_sandwich(*toppings):
    """List out the provided sandwich toppings"""
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_sandwich("corned beef", "sauerkraut")
make_sandwich("pastrami", "onions", "mustard")
make_sandwich("salami", "swiss cheese", "lettuce", "tomato", "mayonnaise")
