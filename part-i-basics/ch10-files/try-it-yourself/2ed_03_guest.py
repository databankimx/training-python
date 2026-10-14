"""Assignment 10.3 (2nd Edition)"""

# Guest: Write a program that prompts the user for their name.
#        When they respond, write their name to a file called
#        `guest.txt`.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "guest.txt")

print("Try-it-Yourself:")
print("Assignment 10.3\n")

name = input("Please enter your name:\n> ")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(name)
    
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())
