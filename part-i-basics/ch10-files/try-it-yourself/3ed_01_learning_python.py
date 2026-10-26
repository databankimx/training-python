"""Assignment 10.1 (3rd Edition)"""

# Learning Python: Open a blank file in your text editor and write a few lines
#                  summarizing what you've learned about Python so far. Start
#                  each line with the phrase In Python you can. . . . Save the
#                  file as learning_python.txt in the same directory as your
#                  exercises from this chapter. Write a program that reads the
#                  file and prints what you wrote two times: print the contents
#                  once by reading in the entire file, and once by storing the
#                  lines in a list and then looping over each line.

from pathlib import Path
from relative_paths import get_path

file_path = get_path("learning_python.txt", "Files")

print("Try-it-Yourself:")
print("Assignment 10.1\n")

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")
print(text.rstrip())

print()

lines = text.splitlines()
for line in lines:
    print(line.rstrip())
