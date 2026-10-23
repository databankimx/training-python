"""Lesson 5.5"""

#pylint: disable=useless-else-on-loop

print("Chapter 5:")
print("Exercise 5 - Using 'if' Statements")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")

age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")

age = 70
price = 20
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
print(f"Your admission cost is ${price}\n")

requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms...")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni...")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese...")
print("Finished making your pizza!")

print()
i = 0
while i < 5:
    i += 1
    print(i)
else: #NOSONAR
    print("If this ran, i must be 5 or more.\n")

for i in range(1, 6):
    print(i)
else: #NOSONAR
    print("This ran when I exhausted the range.")

print()
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("This won't print, because the loop stopped at 3.")
