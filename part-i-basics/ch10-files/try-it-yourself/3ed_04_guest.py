"""Assignment 10.4 (3rd Edition)"""

# Guest: Write a program that prompts the user for their name. When
#        they respond, write their name to a file called `guest.txt`.

from pathlib import Path
from relative_paths import get_path

file_path = get_path("guest.txt", "Files")

print("Try-it-Yourself:")
print("Assignment 10.4\n")

file = Path(file_path)

name = input("Please enter your name:\n> ")
file.write_text(name + "\n", encoding="utf-8")

print(file.read_text(encoding="utf-8"))
