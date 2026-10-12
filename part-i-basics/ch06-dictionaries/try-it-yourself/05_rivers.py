"""Assignment 6.5"""

# Rivers: Dictionary of three major rivers and the country each runs through.
#         Loop to print a sentence about each river, each river name, each country.

print("Try-it-Yourself:")
print("Assignment 6.5")

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
print()

for river in rivers:
    print(river.title())
print()

for country in rivers.values():
    print(country.title())
