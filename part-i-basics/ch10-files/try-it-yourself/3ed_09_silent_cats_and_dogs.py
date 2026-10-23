"""Assignment 10.9 (3rd Edition)"""

# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
#                       silently if either file is missing.

from pathlib import Path
from relative_paths import get_path

log_path = get_path("missing_files.log", "Files")
log_file = Path(log_path)

print("Try-it-Yourself:")
print("Assignment 10.9\n")

def read_file(filename):
    """Read the selected file"""
    file_path = get_path(filename, "Files")
    try:
        file = Path(file_path)
        content = file.read_text(encoding="UTF-8")
    except FileNotFoundError:
        with log_file.open("a", encoding="UTF-8") as log:
            log.write(f"Missing File:\n{file_path}\n\n")
    else:
        print(f"{filename}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
