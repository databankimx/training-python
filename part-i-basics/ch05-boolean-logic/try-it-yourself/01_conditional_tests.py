"""Assignment 5.1"""

# Conditional Tests: Write a series of conditional tests.
#                    Print a statement describing each test and your
#                    prediction for the results of each test.
#                    Create at least ten tests - five True, five False.

print("Try-it-Yourself:")
print("Assignment 5.1")

make = "Dodge"
model = "Challenger"
print("Is make == 'fiat'? I predict False.")
print(make == "fiat")
print("Is make == 'dodge'? I predict False.")
print(make == "dodge")
print("Is make == 'Dodge'? I predict True.")
print(make == "Dodge")
print("Is case-insensitive make == 'dodge'? I predict True.")
print(make.lower() == "dodge")

print("Is model == 'charger'? I predict False.")
print(model == "charger")
print("Is model != 'charger'? I predict True.")
print(model != "charger")
print("Is model == 'challenger'? I predict False.")
print(model == "challenger")
print("Is model == 'Challenger'? I predict True.")
print(model == "Challenger")
print("Is case-insensitive model == 'charger'? I predict False.")
print(model.lower() == "charger")
print("Is case-insensitive model == 'challenger'? I predict True.")
print(model.lower() == "challenger")
