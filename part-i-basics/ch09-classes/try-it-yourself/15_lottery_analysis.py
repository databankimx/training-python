"""Assignment 9.15"""

# Lottery Analysis: You can use a loop to see how hard it might be to win
#                   the kind of lottery you just modeled. Make a list or
#                   tuple called `my_ticket`. Write a loop that keeps
#                   pulling numbers until your ticket wins. Print a message
#                   reporting how many times the loop had to run to give
#                   you a winning ticket.

from random import choice

print("Try-it-Yourself:")
print("Assignment 9.15")

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"]
my_ticket = ["1", "2", "3", "4"]
i_won = False
attempts = 0

while not i_won:
    attempts += 1
    selected = []
    while len(selected) < 4:
        val = choice(numbers)
        if val not in selected:
            selected.append(val)
    print(selected)
    if sorted(selected) == sorted(my_ticket):
        i_won = True

print(f"\nMy ticket {my_ticket} won after {attempts} attempts!\n")
