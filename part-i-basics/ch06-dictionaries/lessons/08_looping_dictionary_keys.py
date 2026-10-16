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

for name in favorite_languages.keys(): # pylint: disable=consider-iterating-dictionary
    print(name.title())

print()

for name in favorite_languages:
    print(name.title())
