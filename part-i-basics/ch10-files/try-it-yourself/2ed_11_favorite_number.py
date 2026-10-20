"""Assignment 10.11 (2nd Edition)"""

# Favorite Number: Write a program that prompts for the user's favorite
#                  number. Use json.dump() to store this number in a file.
#                  Write a separate program that reads in this value
#                  and prints the message:
#                  "I know your favorite number! It's _____."

import os
import json

print("Try-it-Yourself:")
print("Assignment 10.11 - part 1\n")

ROOT_DIR = os.path.dirname(__file__)

file_name = "favorite_number.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

def get_favorite_number():
    """Get the user's favorite number"""
    num = None

    while num is None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(num, f)

    print(f"I saved {num} as your favorite number!\n")
    return num

def read_favorite_number():
    """Read the user's favorite number from a file"""
    try:
        with open(file_path, encoding="utf-8") as f:
            num = json.load(f)
            return int(num)
    except FileNotFoundError:
        num = get_favorite_number()
    return num

print(f"I know your favorite number! It's {read_favorite_number()}")
