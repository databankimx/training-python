"""Lesson 6.10"""

print("Chapter 6:")
print("Exercise 10 - Sorting Dictionary Keys")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(sorted(favorite_languages.keys()))
print(sorted(favorite_languages))

for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(dict(sorted(people.items())))
print(dict(sorted(people.items(), key=lambda item: item[1])))
