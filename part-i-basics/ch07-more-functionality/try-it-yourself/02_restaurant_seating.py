"""Assignment 7.2"""

# Restaurant Seating: Write a program that asks the user how many people
#                     are in their dinner group. If the answer is more than
#                     eight, print a message saying they'll have to wait
#                     for a table. Otherwise, report that their table is ready.

print("Try-it-Yourself:")
print("Assignment 7.2")

guests = input("How many guests in your party?\n> ")
guests = int(guests)
if guests > 8:
    print("There will be a little wait for a table.")
else:
    print("Your table is ready.")
