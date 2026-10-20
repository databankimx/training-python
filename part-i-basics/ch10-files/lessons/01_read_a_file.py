"""Lesson 10.1"""

import os
from pathlib import Path
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 1 - Read a File\n")

# --- 2nd Edition Method ---
# import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

file_object = open(file_path, encoding="UTF-8")
text = file_object.read()
print(text.rstrip(), "\n")
file_object.close()

with open(file_path, encoding="UTF-8") as file_object:
    text = file_object.read()
print(text.rstrip())

print()

# --- 3rd Edition Method ---
# from relative_paths import get_path
# from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")
path_object = Path(file_path)

text = path_object.read_text(encoding="UTF-8")
print(text.rstrip())
