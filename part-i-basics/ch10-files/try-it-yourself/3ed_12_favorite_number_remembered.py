"""Assignment 10.12 (3rd Edition)"""

# Favorite Number Remembered: Combine the two programs from Exercise 10.11
#                             into one file. If the number is already stored,
#                             report the favorite number to the user. If not,
#                             prompt for the user's favorite number and store
#                             it in a file. Run the program twice to see that
#                             it works.

import json
from pathlib import Path
from relative_paths import get_path

print("Try-it-Yourself:")
print("Assignment 10.12\n")

def store_favorite_number(filepath):
    """Get the user's favorite number and store it in a file"""
    num = None
    while num is None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!\n")
    file = Path(filepath)
    file.write_text(json.dumps(num), encoding="utf-8")
    print(f"I saved {num} as your favorite number!\n")
    return num

def get_favorite_number(file):
    """Attempt to read user's favorite number from a file"""
    file = Path(file_path)
    if file.exists():
        num = json.loads(file.read_text(encoding="utf-8"))
        return num
    return store_favorite_number(file)

file_name = "favorite_number_remembered.json"
file_path = get_path(file_name, "Files")

number = get_favorite_number(file_path)
if number:
    print(f"I know your favorite number is {number}.\n")
else:
    print("Something went wrong!")
