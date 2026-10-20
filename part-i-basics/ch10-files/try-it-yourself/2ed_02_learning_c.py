"""Assignment 10.2 (2nd Edition)"""

# Learning C: You can use the `replace()` method to replace any word
#             in a string with a different word. Here's a quick example
#             showing how to replace 'dog' with 'cat' in a sentence:
#             -----------------------------------
#             >>> message = "I really like dogs."
#             >>> message.replace('dog', 'cat')
#             'I really like cats.'
#             -----------------------------------
#             Read in each line from the file you just created,
#             `learning_python.txt`, and replace the word Python with
#             the name of another language, such as C. Print each
#             modified line to the screen.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "learning_python.txt")

print("Try-it-Yourself:")
print("Assignment 10.2\n")

with open(file_path, encoding="utf-8") as file:
    for line in file:
        line = line.replace("Python", "C++")
        print(line.rstrip())
