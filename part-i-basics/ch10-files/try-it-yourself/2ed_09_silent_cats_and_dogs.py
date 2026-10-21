"""Assignment 10.9 (2nd Edition)"""

# Silent Cats and Dogs: Modify your except block in Exercise 10.8 to
#                       fail silently if either file is missing.

import os

ROOT_DIR = os.path.dirname(__file__)
log_path = os.path.join(ROOT_DIR, "Files", "missing_files.log")

print("Try-it-Yourself:")
print("Assignment 10.9\n")

def read_file(filename):
    """Read the selected file"""
    file_path = os.path.join(ROOT_DIR, "Files", filename)
    try:
        with open(file_path, encoding="UTF-8") as file:
            content = file.read()
    except FileNotFoundError:
        with open(log_path, "a", encoding="UTF-8") as log:
            log.write(f"Missing File:\n{file_path}\n\n")
    else:
        print(f"{filename}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
