"""Lesson 7.3"""

print("Chapter 7:")
print("Exercise 3 - Using the Modulo Operator")

numbers = [4, 5, 6, 7]
for number in numbers:
    print(f"{number} % 3 = {number % 3}")

number = int(input("\nEnter a number, and I will tell you if it is even or odd:\n> "))
if number % 2 == 0:
    condition = "even"
else:
    condition = "odd"
print(f"The number {number} is {condition}.")
