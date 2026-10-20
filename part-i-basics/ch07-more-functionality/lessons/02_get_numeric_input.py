"""Lesson 7.2"""

print("Chapter 7:")
print("Exercise 2 - Getting Numeric Input")

# This would result in a TypeError
# num = input("Enter a number: ")
# print(num > 10)

age = input("How old are you?\n> ")
age = int(age)
print(age >= 18)

height = int(input("\nHow tall are you in inches?\n> "))
if height >= 48:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older...")

price = 1.75
paid = float(input("\nEnter the amount paid:\n> "))
if paid > price:
    print(f"Your change is ${(paid - price):.2f}")
elif paid < price:
    print(f"You still owe ${(price - paid):.2f}")
else:
    print("Thank you.")
