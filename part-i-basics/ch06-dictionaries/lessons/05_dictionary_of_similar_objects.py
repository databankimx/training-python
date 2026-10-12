"""Lesson 6.5"""

print("Chapter 6:")
print("Exercise 5 - Using Dictionaries to Group Similar Objects")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

language = favorite_languages["phil"].title()
print(f"Phil's favorite language is {language}.")
