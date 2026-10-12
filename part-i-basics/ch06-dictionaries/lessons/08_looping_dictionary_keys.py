"""Lesson 6.8"""

print("Chapter 6:")
print("Exercise 8 - Looping Dictionary Keys")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(favorite_languages.keys(), "\n")

# pylint: disable=consider-iterating-dictionary
for name in favorite_languages.keys():
    print(name.title())

print()

for name in favorite_languages:
    print(name.title())
