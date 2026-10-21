"""Lesson 6.5"""

print("Chapter 6:")
print("Exercise 5 - Using Dictionaries to Group Similar Objects")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
name = "phil"
language = favorite_languages[name].title()
print(f"{name.title()}'s favorite language is {language}.")
