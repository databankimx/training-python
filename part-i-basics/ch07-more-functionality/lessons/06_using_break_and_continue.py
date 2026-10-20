"""Lesson 7.6"""

print("Chapter 7:")
print("Exercise 6 - Using 'break' and 'continue'")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\n> "

while True:
    city = input(prompt)
    if city.lower() == "quit":
        break
    print(f"I'd love to go to {city.title()}!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
