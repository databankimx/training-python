"""Lesson 5.4"""

print("Chapter 5:")
print("Exercise 4 - Check if List Contains Value")

requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

banned_users = ["andrew", "carolina", "david"]
active_users = ["marie", "andrew"]
for user in active_users:
    if user not in banned_users:
        print(f"{user.title()}, you can post a response.")
    else:
        print(f"{user.title()}, you cannot post responses!")
