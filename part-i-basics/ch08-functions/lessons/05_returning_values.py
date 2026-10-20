"""Lesson 8.5"""

print("Chapter 8:")
print("Exercise 5 - Returning Values from Functions")

# By writing your function so that it returns some data,
#   you add a lot of flexibility to your code
# Note: ALL functions provide return values. If you do not include
#   a return statement, the function returns `None`

# Note: You do not have to declare a return in the method signature
def get_formatted_name_simple(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    # Return statement determines what the function returns to the calling code
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
