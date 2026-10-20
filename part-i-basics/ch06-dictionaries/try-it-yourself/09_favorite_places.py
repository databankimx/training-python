"""Assignment 6.9"""

# Favorite Places: Dictionary called favorite_places. Three names as keys,
#                  one to three favorite places per person as a list value.
#                  Loop through and print each person's name and their places.

print("Try-it-Yourself:")
print("Assignment 6.9")

favorite_places = {
    "scott": ["ireland", "spain", "mexico"],
    "matt": ["puerto rico"],
    "pat": ["minnesota", "scotland"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places include:")
    for place in places:
        print(f"\t{place.title()}")
