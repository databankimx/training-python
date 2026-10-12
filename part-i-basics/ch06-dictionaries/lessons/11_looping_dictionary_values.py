"""Lesson 6.11"""

print("Chapter 6:")
print("Exercise 11 - Looping Dictionary Values")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(favorite_languages.values(), "\n")

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

counts = {}
for language in favorite_languages.values():
    # pylint: disable=consider-iterating-dictionary
    if language in counts.keys():
        counts[language] += 1
    else:
        counts[language] = 1
print("\nThe following languages have been mentioned:")
for lang in sorted(counts.keys()):
    print(f"{lang.title()}: {counts[lang]} time{('' if counts[lang] == 1 else 's')}")

languages = list(favorite_languages.values())
print("\nThe following languages have been mentioned:")
for lang in set(languages):
    print(f"{lang.title()}: {languages.count(lang)} time{('' if counts[lang] == 1 else 's')}")
