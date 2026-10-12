"""Assignment 7.3"""

# Multiples of Ten: Ask the user for a number, and then report whether
#                   the number is a multiple of 10 or not.

print("Try-it-Yourself:")
print("Assignment 7.3")

number = int(input("\nEnter a number, and I will tell you if it is a multiple of 10:\n> "))
condition = "" if number % 10 == 0 else "not "
print(f"{number} is {condition}a multiple of 10.")
