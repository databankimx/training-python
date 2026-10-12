"""Assignment 7.9"""

# No Pastrami: Using the list `sandwich_orders` from Exercise 7-8,
#              make sure the sandwich 'pastrami' appears in the list
#              at least three times. Add code near the beginning of
#              your program to print a message saying the deli has
#              run out of pastrami, and then use a while loop to
#              remove all occurrences of 'pastrami' from `sandwich_orders`.
#              Make sure no pastrami sandwiches end up in
#              `finished_sandwiches`.

print("Try-it-Yourself:")
print("Assignment 7.9")

sandwich_orders = [
    "italian sub",
    "pastrami",
    "reuben",
    "pastrami",
    "pastrami",
    "croque monsieur",
    "pastrami",
    "pb&j"

]
print("We have run out of pastrami!")
finished_sandwiches = []
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich...")
print(f"The following sandwich orders were fulfilled:\n{finished_sandwiches}")
