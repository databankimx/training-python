"""Lesson 8.6"""

print("Chapter 8:")
print("Exercise 6 - Returning Dictionaries from Functions")

def build_person_simple(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")

musician = build_person_simple("jimi", "hendrix")
print(musician)
pause()

musician = build_person("jimi", "hendrix", age = 27)
print(musician)
