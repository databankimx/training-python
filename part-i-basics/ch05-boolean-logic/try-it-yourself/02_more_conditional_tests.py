"""Assignment 5.2"""

# More Conditional Tests: At least one True and one False for each:
#   • Equality and inequality with strings
#   • Tests using lower()
#   • Numerical tests (==, !=, >, >=, <, <=)
#   • Tests using and and or
#   • Test whether an item is in a list
#   • Test whether an item is not in a list

print("Try-it-Yourself:")
print("Assignment 5.2")

make = "Dodge"
model = "Challenger"
year = 2014

print("Is make == 'fiat'? I predict False.")
print(make == "fiat")
print("Is make != 'fiat'? I predict True.")
print(make != "fiat")

print("Is case-insensitive make == 'fiat'? I predict False.")
print(make.lower() == "fiat")
print("Is case-insensitive make == 'dodge'? I predict True.")
print(make.lower() == "dodge")

print("\nIs year == 2014? I predict True.")
print(year == 2014)
print("Is year == 2020? I predict False.")
print(year == 2020)
print("Is year != 2020? I predict True.")
print(year != 2020)
print("Is year > 2020? I predict False.")
print(year > 2020)
print("Is year >= 2020? I predict False.")
print(year >= 2020)
print("Is year < 2020? I predict True.")
print(year < 2020)
print("Is year <= 2020? I predict True.")
print(year <= 2020)

print("\nIs case-insensitive make == 'dodge' and model == 'charger'? I predict False.")
print(make.lower() == "dodge" and model.lower() == "charger")
print("Is case-insensitive make == 'dodge' and model == 'challenger'? I predict True.")
print(make.lower() == "dodge" and model.lower() == "challenger")
print("Is case-insensitive make == 'dodge' or model == 'charger'? I predict True.")
print(make.lower() == "dodge" or model.lower() == "charger")
print("Is case-insensitive make == 'fiat' or model == 'spider'? I predict False.")
print(make.lower() == "fiat" or model.lower() == "spider")

stats = [2014, "dodge", "challenger"]
print("\nDoes stats contain 'fiat'? I predict False.")
print("fiat" in stats)
print("\nDoes stats contain 'dodge'? I predict True.")
print("dodge" in stats)
print("\nDoes stats not contain 'charger'? I predict True.")
print("charger" not in stats)
print("\nDoes stats not contain 'challenger'? I predict False.")
print("challenger" not in stats)
