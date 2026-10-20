"""Assignment 6.8"""

# Pets: Several dictionaries each representing a pet (animal kind + owner name).
#       Store in a list called pets. Loop through and print everything about each pet.

print("Try-it-Yourself:")
print("Assignment 6.8")

charlie = {
    "animal": "dog",
    "owner": "talia",
}

orville = {
    "animal": "guinea pig",
    "owner": "scott",
}

bronte = {
    "animal": "cat",
    "owner": "melissa",
}

pets = [charlie, orville, bronte]
for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}")
