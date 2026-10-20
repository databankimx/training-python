"""Assignment 9.13"""

# Dice: Make a class `Die` with one attribute called sides, which has
#       a default value of 6. Write a method called `roll_die()` that
#       prints a random number between 1 and the number of sides the
#       die has. Make a 6-sided die and roll it 10 times. Make a
#       10-sided die and a 20-sided die. Roll each die 10 times.

from die import Die

print("Try-it-Yourself:")
print("Assignment 9.13")

die = Die()
for i in range(1, 11):
    print(f"[{die.sides}-sided die] Roll {i}: {die.roll()}")
print("-----")

dice = [Die(10), Die(20)]
for die in dice:
    for i in range(1, 11):
        print(f"[{die.sides}-sided die] Roll {i}: {die.roll()}")
    print("-----")
