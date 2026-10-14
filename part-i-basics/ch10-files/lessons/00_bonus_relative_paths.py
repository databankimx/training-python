"""Lesson 10.0"""

import os
from pathlib import Path
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 0 - Relative Paths\n")

# -------------------- RELATIVE PATHS - METHOD 1 --------------------
# import os

ROOT_DIR = os.path.dirname(__file__)
print(f"Root directory is:          \"{ROOT_DIR}\"")

file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")
print(f"File path (manual) is:      \"{file_path}\"")

# -------------------- RELATIVE PATHS - METHOD 2 --------------------
# from relative_paths import get_path

file_path = get_path("pi_digits.txt", "Files")
print(f"File path (from module) is: \"{file_path}\"\n")

# ------------------ READ FILE - 2nd EDITION METHOD ------------------
with open(file_path, encoding="UTF-8") as file:
    text = file.read()
    print(text.rstrip())

print("-----")

# ------------------ READ FILE - 3rd EDITION METHOD ------------------
# from pathlib import Path

file = Path(file_path)
contents = file.read_text(encoding="UTF-8")
print(contents.rstrip())
