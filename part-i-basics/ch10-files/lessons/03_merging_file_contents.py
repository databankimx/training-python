"""Lesson 10.3"""

import os
from pathlib import Path
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 3 - Merging File Contents\n")

# --- 2nd Edition Method ---

# import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

pi_string = ""
with open(file_path, encoding="UTF-8") as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")

with open(file_path, encoding="UTF-8") as file_object:
    pi_string = "".join(l.strip() for l in file_object)

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")

pi_string = ""

file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

with open(file_path, encoding="UTF-8") as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string[:53])
print(f"pi_string is {len(pi_string):,} characters long.\n")

# --- 3rd Edition Method ---

# from relative_paths import get_path
# from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

pi_string = ""
lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")

pi_string = "".join(l.strip() for l in text.splitlines())

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")

file_path = get_path("pi_million_digits.txt", "Files")

pi_string = ""

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

print(pi_string[:53])
print(f"pi_string is {len(pi_string):,} characters long.\n")
