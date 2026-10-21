"""Lesson 8.5"""

print("Chapter 8:")
print("Exercise 5 - Returning Values from Functions")

# By writing your function so that it returns some data,
#   you add a lot of flexibility to your code.
# Note: Every function call produces a value. If a function has no
#   return statement, the value is `None`.


# You do not have to declare a return type in the function signature.
def get_formatted_name_simple(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    # The return statement determines what the function gives back to the calling code
    return full_name.title()


def get_formatted_name_middle(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")


musician = get_formatted_name_simple("jimi", "hendrix")
print(musician)
pause()

musician = get_formatted_name_middle("john", "lee", "hooker")
print(musician)
pause()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)

# HINT: Mouse over a function name to see what data type it returns
