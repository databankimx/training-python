"""Module exposing the make_pizza() function"""

# This file is designed to be a module, called from another file
# We're only exposing the make_pizza() method

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
