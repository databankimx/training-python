"""Lesson 8.2"""

print("Chapter 8:")
print("Exercise 2 - Function Arguments and Parameters")

def greet_named_user(name):
    """Print a greeting to the user passed to the function"""
    print(f"\nHello, {name.title()}")

def greet_full_name(first_name, last_name):
    """Print a greeting to the user passed to the function"""
    print(f"\nHello, {first_name.title()} {last_name.title()}")

def greet_users(names):
    """Print a greeting to each of the users passed to the function"""
    for name in names:
        msg = f"\nHello, {name.title()}!"
        print(msg)

person = "abe"
greet_named_user(person)

first = "charles"
last = "babbage"
greet_full_name(first, last)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
