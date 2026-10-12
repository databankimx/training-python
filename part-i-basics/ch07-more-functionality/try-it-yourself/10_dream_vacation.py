"""Assignment 7.10"""

# Dream Vacation: Write a program that polls users about their dream vacation.
#                 Write a prompt similar to "If you could visit one place
#                 in the world, where would you go?""
#                 Include a block of code that prints the results of the poll.

print("Try-it-Yourself:")
print("Assignment 7.10")

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n> ")
    response = input("Where would you take your dream vacation?\n> ")
    responses[name] = response
    repeat = input("Let another person respond? (yes/no)\n> ").lower()[0]
    if repeat == "n":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s dream vacation is to {response}.")
