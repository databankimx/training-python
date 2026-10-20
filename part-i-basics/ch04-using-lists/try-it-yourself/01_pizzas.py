"""Assignment 4.1"""

from random import choice

# Pizzas: Think of at least three kinds of your favorite pizza.
#         Store these pizza names in a list, and then use a for
#         loop to print the name of each pizza.

print("Try-it-Yourself:")
print("Assignment 4.1")

pizzas = ["margherita", "spinach and garlic", "feta and black olive"]
adjectives = ["delicious", "tasty", "scrumptious"]
for pizza in pizzas:
    print(f"I think {pizza} pizza is {choice(adjectives)}!")
print("Pizza is magnificent!")
