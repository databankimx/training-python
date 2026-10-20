"""Assignment 10.1 (2nd Edition)"""

# Learning Python: Open a blank file in your text editor and write a few
#                  lines summarizing what you've learned about Python so
#                  far. Start each line with the phrase 'In Python you can...'
#                  Save the file as `learning_python.txt` in the same
#                  directory as your exercises from this chapter. Write a
#                  program that reads the file and prints what you wrote
#                  three times. Print the contents once by reading in the
#                  entire file, once by looping over the file object, and
#                  once by storing the lines in a list and then working
#                  with them outside the with block.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "learning_python.txt")

print("Try-it-Yourself:")
print("Assignment 10.1\n")

with open(file_path, encoding="utf-8") as file:
    result = file.read()
    print(result.rstrip())

print()

with open(file_path, encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())

print()

with open(file_path, encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())
