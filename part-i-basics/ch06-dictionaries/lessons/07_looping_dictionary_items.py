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
    print(f"Key:   {key}")
    print(f"Value: {value}\n")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print()

for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite language is {value.title()}.")
