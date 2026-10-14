"""Lesson 10.6"""

from random import randrange

print("Chapter 10:")
print("Exercise 6 - Handling Errors\n")

# This code would crash on a ZeroDivisionError
# for i in range(100):
#     x = randrange(10)
#     y = randrange(10)
#     print(f"{x} / {y} = {x / y}")

for i in range(100):
    try:
        x = randrange(10)
        y = randrange(10)
        print(f"{x} / {y} = {x / y}")
    except ZeroDivisionError:
        print("Caught attempt to divide by zero...")
        print("Halting loop!\n")
        break

while True:
    print("Input numbers to divide or 'q' to quit.")
    first_number = input("\nFirst number:\n> ")
    if first_number == 'q':
        break
    second_number = input("Second number:\n> ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!\n")
    else:
        print(f"\n{first_number} / {second_number} = {answer}\n")
