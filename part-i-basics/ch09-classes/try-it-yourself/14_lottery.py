"""Assignment 9.14"""

# Lottery: Make a list or tuple containing a series of ten numbers
#          and five letters. Randomly select four numbers or letters
#          from the list and print a message saying that any ticket
#          matching these four numbers or letters wins a prize.

from random import choice

print("Try-it-Yourself:")
print("Assignment 9.14")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]
selected = []

while len(selected) < 4:
    val = choice(numbers)
    if val not in selected:
        selected.append(val)

# Alternate Solution
# for _ in range(4):
#     i = choice(range(len(numbers)))
#     val = numbers.pop(i)
#     selected.append(val)

print(f"The winning numbers are: {selected}\n")
