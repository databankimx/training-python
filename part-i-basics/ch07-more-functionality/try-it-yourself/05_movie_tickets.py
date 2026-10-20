"""Assignment 7.5"""

# Movie Tickets: A movie theater charges different ticket prices
#                depending on a person's age. If a person is under
#                the age of 3, the ticket is free; if they are
#                between 3 and 12, the ticket is $ 10; and if they
#                are over age 12, the ticket is $ 15. Write a loop
#                in which you ask users their age, and then tell
#                them the cost of their movie ticket.

print("Try-it-Yourself:")
print("Assignment 7.5")

price = 0
age = 0
message = ""
prompt = "Please enter your age or 'quit':\n> "
while True:
    message = input(prompt)
    if message.lower() == 'quit':
        break
    age = int(message)
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15
    print(f"Your ticket costs ${price}.00")
