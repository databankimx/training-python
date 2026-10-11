"""Lesson 2.2"""

print("Chapter 2:")
print("Exercise 2 - Populate a variable from user input")

name = input("Please enter your name: ")

# f-strings (formatted strings) are the equivalent to string interpolation
# (available in Python 3.6+)
message = f"Hello {name}"
print(message)

# In older versions, you would use this syntax:
# pylint: disable=consider-using-f-string
message = "Hello {0}".format(name)
print(message)
