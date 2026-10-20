"""Assignment 4.10"""

# Slices: Using one of the programs you wrote in this chapter,
#         add several lines that print slices of the list.

print("Try-it-Yourself:")
print("Assignment 4.10")

odd_numbers = list(range(1, 21, 2))
print(f"The first three odd numbers are: {odd_numbers[:3]}")
print(f"The next three odd numbers are: {odd_numbers[3:6]}")
print(f"The last three odd numbers are: {odd_numbers[-3:]}")
