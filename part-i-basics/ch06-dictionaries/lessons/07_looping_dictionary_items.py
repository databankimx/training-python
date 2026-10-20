"""Lesson 6.7"""

print("Chapter 6:")
print("Exercise 7 - Looping Dictionary Items")

user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

print(user.items())

for key, value in user.items():
    print(f"\nKey:   {key}")
    print(f"Value: {value}")

print()

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite language is {value.title()}.")

print()

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
