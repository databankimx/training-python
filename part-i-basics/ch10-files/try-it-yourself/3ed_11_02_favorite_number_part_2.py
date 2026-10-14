"""Assignment 10.11 (3rd Edition)"""

# Favorite Number: Write a program that prompts for the user's favorite number. Use json.dump() to
#                  store this number in a file. Write a separate program that reads in this value
#                  and prints the message, "I know your favorite number! It's _____."

import json
from pathlib import Path
from relative_paths import get_path

file_name = "favorite_number.json"
file_path = get_path(file_name, "Files")

print("Try-it-Yourself:")
print("Assignment 10.11 - part 2\n")

file = Path(file_path)

if file.exists():
    num = json.loads(file.read_text(encoding="utf-8"))
    print(f"I know your favorite number is {num}.\n")
else:
    print("You haven't stored a favorite number yet!")
