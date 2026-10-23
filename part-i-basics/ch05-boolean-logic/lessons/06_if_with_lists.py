"""Lesson 5.6"""

print("Chapter 5:")
print("Exercise 6 - Using 'if' with Lists")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

out_of_stock = ["green peppers", "anchovies"]
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in out_of_stock:
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("Finished your plain pizza.")

available_toppings = ["mushrooms", "olives", "green peppers",
                      "pepperoni", "pineapple", "extra cheese"]
out_of_stock = ["green peppers", "mushrooms"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        if requested_topping in out_of_stock:
            print(f"Sorry, we're out of {requested_topping}.")
        else:
            print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't offer {requested_topping}.")
print("Finished making your pizza!")
