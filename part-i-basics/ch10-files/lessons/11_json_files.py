"""Lesson 10.11"""

import os
import json
from pathlib import Path
from sm_utils import pause, clear_terminal
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 11 - Working with JSON Files\n")

# --- 2nd Edition Method ---

# from sm_utils import pause, clear_terminal
# import json
# import os

clear_terminal()

ROOT_DIR = os.path.dirname(__file__)

numbers = [2, 3, 5, 7, 11, 13]
numbers_object = {"numbers" : numbers}

file_name = "numbers.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)
with open(file_path, "w", encoding="UTF-8") as f:
    json.dump(numbers_object, f)

print(f"Stored JSON file [{file_name}]")

with open(file_path, encoding="UTF-8") as f:
    print(f.read().rstrip())

pause()
clear_terminal()

with open(file_path, encoding="UTF-8") as f:
    numbers_object = json.load(f)

print(numbers_object)

pause()
clear_terminal()

# --- 3rd Edition Method ---

# import json
# from relative_paths import get_path
# from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]
numbers_object = {"numbers" : numbers}

file_name = "numbers.json"
file_path = get_path("numbers.json", "Files")

contents = json.dumps(numbers_object)
file = Path(file_path)
file.write_text(contents, encoding="UTF-8")

print(f"Stored JSON file [{file_name}]")

print(file.read_text(encoding="UTF-8"))

pause()
clear_terminal()

file_name = "numbers.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
numbers_object = json.loads(file.read_text(encoding="UTF-8"))

print(numbers_object)
