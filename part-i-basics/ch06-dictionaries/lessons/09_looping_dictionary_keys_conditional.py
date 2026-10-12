"""Lesson 6.9"""

print("Chapter 6:")
print("Exercise 9 - Looping Dictionary Keys for Conditional Handling")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

friends = ["phil", "sarah"]
# pylint: disable=consider-using-dict-items
for name in favorite_languages:
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

print()

people = ["phil", "sarah", "erin", "jen", "edward"]
for person in people:
    if person not in favorite_languages:
        print(f"{person.title()}, please take the languages poll.")
