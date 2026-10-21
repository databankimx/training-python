"""Assignment 10.8 (3rd Edition)"""

# Cats and Dogs: Make two files, `cats.txt` and `dogs.txt`. Store at least
#                three names of cats in the first file and three names of
#                dogs in the second file. Write a program that tries to
#                read these files and print the contents of the file to
#                the screen. Wrap your code in a try-except block to catch
#                the FileNotFound error, and print a friendly message if
#                a file is missing. Move one of the files to a different
#                location on your system, and make sure the code in the
#                except block executes properly.

from pathlib import Path
from relative_paths import get_path

print("Try-it-Yourself:")
print("Assignment 10.8\n")

def read_file(filename):
    """Read the selected file"""
    file_path = get_path(filename, "Files")
    try:
        file = Path(file_path)
        content = file.read_text(encoding="UTF-8")
    except FileNotFoundError:
        print(f"File [{filename}] not found!\n")
    else:
        print(f"{filename}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
