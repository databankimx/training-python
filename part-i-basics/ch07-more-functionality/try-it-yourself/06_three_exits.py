"""Assignment 7.6"""

# Three Exits: Write different versions of either Exercise 7.4 or
#              Exercise 7.5 that does each of the following at least once:
#       • Use a conditional test in the while statement to stop the loop.
#       • Use an active variable to control how long the loop runs.
#       • Use a break statement to exit the loop when the user enters a
#         'quit' value.

print("Try-it-Yourself:")
print("Assignment 7.6")

# Version 1: a conditional test in the while statement
message = input("Enter a topping or 'quit':\n> ")
while message.lower() != "quit":
    print(f" - Added {message}")
    message = input("Enter a topping or 'quit':\n> ")

# Version 2: an active variable controls the loop
active = True
prompt = "Enter a topping or 'quit':\n> "
while active:
    message = input(prompt)
    if message.lower() == "quit":
        active = False
    else:
        print(f" - Added {message}")

# Version 3: a break statement exits the loop
prompt = "Enter a topping or 'quit':\n> "
while True:
    message = input(prompt)
    if message.lower() == "quit":
        break
    print(f" - Added {message}")
