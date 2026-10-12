"""Assignment 6.10"""

# Favorite Numbers: Modify Exercise 6.2 so each person can have more than one
#                   favorite number. Print each person's name and their numbers.

print("Try-it-Yourself:")
print("Assignment 6.10")

favorite_numbers = {
    "Scott": [42, 73],
    "Sean": [13, 42],
    "Andy": [37],
    "Rene": [1, 2, 343],
    "Matt": [12, 6, 4, 3],
    "John": ["i", "√-1"],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers include:")
    for number in numbers:
        print(f"\t{number}")
