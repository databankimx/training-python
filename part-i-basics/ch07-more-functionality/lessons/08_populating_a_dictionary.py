"""Lesson 7.8"""

print("Chapter 7:")
print("Exercise 8 - Using a Loop to Populate a Dictionary")

responses = {}

while True:
    name = input("\nWhat is your name?\n> ")
    mountain = input("Which mountain would you like to climb someday?\n> ")

    responses[name] = mountain

    repeat = input("Would you like to let another person respond? (yes/no)\n> ").lower()[0]
    if repeat == "n":
        break

print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")
