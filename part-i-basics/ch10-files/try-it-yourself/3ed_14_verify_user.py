"""Assignment 10.14 (3rd Edition)"""

# Verify User: The final listing for remember_me.py assumes either that
#              the user has already entered their username or that the
#              program is running for the first time. We should modify it
#              in case the current user is not the person who last used
#              the program. Before printing a welcome back message in
#              greet_user(), ask the user if this is the correct username.
#              If it's not, call get_new_username() to get the correct
#              username.

import json
from pathlib import Path
from relative_paths import get_path

def store_user(filepath):
    """Store the username to JSON file"""
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    file = Path(filepath)
    file.write_text(json.dumps(username), encoding="UTF-8")

    return username

def get_stored_user(filepath):
    """Attempt to retrieve the username from JSON file"""
    file = Path(filepath)

    if file.exists():
        username = json.loads(file.read_text(encoding="UTF-8"))
        return username

    return None

def greet_user(filepath):
    """Show desired greeting to user"""
    username = get_stored_user(filepath)
    matched = False

    if username:
        answer = input(f"Are you {username.upper()}? (Y|N)\n> ")
        matched = answer[0].lower() == "y"
        if not matched:
            username = store_user(filepath)
    else:
        username = store_user(filepath)

    if matched:
        print(f"\nWelcome back, {username.upper()}\n")
    else:
        print(f"\nWe'll remember you when you come back, {username.upper()}\n")

print("Try-it-Yourself:")
print("Assignment 10.14\n")

file_name = "username.json"
file_path = get_path(file_name, "Files")

greet_user(file_path)
