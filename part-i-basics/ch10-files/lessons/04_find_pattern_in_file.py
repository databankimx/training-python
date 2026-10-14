"""Lesson 10.4"""

import os
from pathlib import Path
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 4 - Read a File and Search for a Pattern\n")

# --- 2nd Edition Method ---

# import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

pi_string = ""

with open(file_path, encoding="UTF-8") as file_object:
    for line in file_object:
        pi_string += line.strip()

birthday = input("Enter your birthday in the form MMDDYY:\n> ")

if birthday in pi_string:
    print("Yay! Your birthday appears in the first million digits of pi!")
else:
    print("Aww... Your birthday does not appear in the first million digits of pi.")

print()

# --- 3rd Edition Method ---

# from relative_paths import get_path
# from pathlib import Path

file_path = get_path("pi_million_digits.txt", "Files")

pi_string = ""

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form MMDDYY:\n> ")

if birthday in pi_string:
    print("Yay! Your birthday appears in the first million digits of pi!")
else:
    print("Aww... Your birthday does not appear in the first million digits of pi.")
