"""Assignment 4.2"""

from random import choice

# Animals: Think of at least three different animals that have
#          a common characteristic. Store the names of these
#          animals in a list, and then use a for loop to print
#          out the name of each animal.

print("Try-it-Yourself:")
print("Assignment 4.2")

animals = ["octopus", "squid", "cuttlefish"]
verbs = ["eat", "devour", "dine on"]
for animal in animals:
    print(f"I like to {choice(verbs)} {animal}.")
print("You have to be very careful cooking any of these animals.")
