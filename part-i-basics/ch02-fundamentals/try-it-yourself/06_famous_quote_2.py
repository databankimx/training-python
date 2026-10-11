"""Assignment 2.6"""

# Famous Quote 2: Repeat Exercise 2-5, but this time represent the famous
#                 person's name using a variable called `famous_person`. Then
#                 compose your message and represent it with a new variable
#                 called `message`. Print your message.

print("Try-it-Yourself:")
print("Assignment 2.6")

name = "count maurice maeterlinck"
famous_person = name.title()
quote = """At every crossway on the road that leads to the future each \
progressive spirit is opposed by a thousand men appointed to guard the past."""
message = f"{famous_person} wrote:\n\"{quote}\"\n"
print(message)
