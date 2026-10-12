"""Lesson 8.9"""

print("Chapter 8:")
print("Exercise 9 - Passing an Arbitrary Amount of Arguments")

def make_pizza_simple(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")

make_pizza_simple("pepperoni")
make_pizza_simple("mushrooms", "green peppers", "extra cheese")

make_pizza_simple(*["mushrooms", "sausage", "black olives"])

pause()
    
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

pause()

def sum_up(x, y, z):
    """Sum the provided numbers."""
    print(f"{x} + {y} + {z} = {x + y + z}")

values = [2, 3, 4]

# This would result in a TypeError
# sum_up(values)

sum_up(*values)
