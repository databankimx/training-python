"""Lesson 5.4"""

print("Chapter 5:")
print("Exercise 4 - Check if List Contains Value")

toppings = ["mushrooms", "onions", "pineapple"]
seek = "anchovies"
found = False
for item in toppings:
    if item == seek:
        found = True
print(found)

print(seek in toppings)
print(seek not in toppings)

print("Mushrooms" in toppings)
print("mushrooms" in toppings)
print("mushrooms".title() in toppings)
print("Mushrooms".lower() in toppings)

print("an" in "banana")
print("an" in ["banana"])

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

active_users = ["marie", "andrew"]
for user in active_users:
    if user not in banned_users:
        print(f"{user.title()}, you can post a response.")
    else:
        print(f"{user.title()}, you cannot post responses!")
