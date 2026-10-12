"""Lesson 8.11"""

import pizza

print("Chapter 8:")
print("Exercise 11 - Importing a Module")

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green pepper")

# pylint: disable=wrong-import-position
from pizza import make_pizza

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper")

# pylint: disable=reimported
import pizza as p
from pizza import make_pizza as mp

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green pepper")

mp(16, "pepperoni")
mp(12, "mushrooms", "green pepper")
