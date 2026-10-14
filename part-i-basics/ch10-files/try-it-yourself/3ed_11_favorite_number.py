"""Assignment 10.11 (3rd Edition)"""

# Favorite Number: Write a program that prompts for the user's favorite
#                  number. Use json.dump() to store this number in a file.
#                  Write a separate program that reads in this value and
#                  prints the message:
#                  "I know your favorite number! It's _____."

import json
from pathlib import Path
from relative_paths import get_path

print("Try-it-Yourself:")
print("Assignment 10.11 - part 1\n")

def get_favorite_number():
    """Get the user's favorite number"""    
    num = None

    while num is None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!")

    file = Path(file_path)
    file.write_text(json.dumps(num), encoding="utf-8")

    print(f"I saved {num} as your favorite number!\n")
    return num

def read_favorite_number():
    """Read the user's favorite number from a file"""    
    file = Path(file_path)
    if file.exists():
        num = json.loads(file.read_text(encoding="utf-8"))
        return num
    return get_favorite_number()

file_name = "favorite_number.json"
file_path = get_path(file_name, "Files")

number = read_favorite_number()

if number:
    print(f"I know your favorite number is {number}.\n")
else:
    print("Something went wrong!")
