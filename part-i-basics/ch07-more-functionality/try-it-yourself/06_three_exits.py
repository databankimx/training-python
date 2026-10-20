"""Assignment 7.6"""

# Three Exits: Write different versions of either Exercise 7.4 or
#              Exercise 7-5 that does each of the following at least once:
#       • Use a conditional test in the while statement to stop the loop.
#       • Use an active variable to control how long the loop runs.
#       • Use a break statement to exit the loop when the user enters a
#         'quit' value.

print("Try-it-Yourself:")
print("Assignment 7.6")

message = ""
active = True
prompt = "Enter a topping or 'quit':\n> "
while active:
    message = input(prompt)
    if message.lower() == "quit":
        # Only one of these is needed (bullets 2 and 3)
        active = False
        break
    print(f" - Added {message}")
