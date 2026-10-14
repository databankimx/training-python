"""Assignment 10.6 (3rd Edition)"""

# Addition: One common problem when prompting for numerical input occurs
#           when people provide text instead of numbers. When you try to
#           convert the input to an int, you'll get a ValueError. Write
#           a program that prompts for two numbers. Add them together
#           and print the result. Catch the ValueError if either input
#           value is not a number, and print a friendly error message.
#           Test your program by entering two numbers and then by
#           entering some text instead of a number.

print("Try-it-Yourself:")
print("Assignment 10.6\n")

print("Enter two integers and I will add them.")

numbers = []

while len(numbers) < 2:
    response = input("Enter a number:\n> ")
    if response is None or len(response) < 1:
        print("You cannot leave the entry blank.")
        continue
    try:
        number = int(response)
        numbers.append(number)
    except ValueError:
        print("Please only enter numbers.")

my_sum = numbers[0] + numbers[1]
print(f"\n{numbers[0]} + {numbers[1]} = {my_sum}")
