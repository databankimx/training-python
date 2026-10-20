"""Assignment 4.11"""

# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
#                         Make a copy of the list and call it friend_pizzas.
#                         Add a new pizza to each list and prove they are separate.

print("Try-it-Yourself:")
print("Assignment 4.11")

my_pizzas = ["margherita", "spinach and garlic", "feta and black olive"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("pepperoni")
friend_pizzas.append("sausage and green pepper")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f" - {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f" - {pizza}")
