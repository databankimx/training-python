"""Lesson 10.9"""

import os
from pathlib import Path
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 9 - ASCII and UTF-8\n")

# --- 2nd Edition Method ---

# import os

ROOT_DIR = os.path.dirname(__file__)
file_name = "moby_dick.txt"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

# This version raises a UnicodeDecodeError on Windows, so it's commented out:
# with open(file_path) as f:
#     contents = f.read()
#     print(len(contents))

with open(file_path, encoding="UTF-8") as f:
    contents = f.read()
    print(len(contents))

# --- 3rd Edition Method ---

# from relative_paths import get_path
# from pathlib import Path

file_name = "moby_dick.txt"
file_path = get_path(file_name, "Files")
file = Path(file_path)

# This version raises a UnicodeDecodeError on Windows, so it's commented out:
# contents = file.read_text()
# print(len(contents))

contents = file.read_text(encoding="UTF-8")
print(len(contents))
