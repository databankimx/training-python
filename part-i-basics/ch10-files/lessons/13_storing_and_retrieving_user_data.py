"""Lesson 10.13"""

import os
import json
from pathlib import Path
from sm_utils import pause, clear_terminal
from relative_paths import get_path

print("Chapter 10:")
print("Exercise 13 - Storing and Retrieving User Data Using a JSON File\n")

clear_terminal()

# --- 2nd Edition Method ---

# import os
# import json

def user_check(filepath: str) -> None:
    """
    If a user file exists, get the user from it
    Otherwise, create a new file with user input
    """
    try:
        with open(filepath, encoding="utf-8") as f:
            user = json.load(f)
            print(f"Welcome back, {user['username']}")
    except FileNotFoundError:
        user = {
            "first_name": input("Enter your first name:\n> "),
            "last_name": input("Enter your last name:\n> ")
        }
        user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(user, f)
        print(f"We'll remember you when you come back, {user['username']}")

ROOT_DIR = os.path.dirname(__file__)
file_name = "user.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)
user_check(file_path)

pause()
clear_terminal()

# --- 3rd Edition Method ---

# from relative_paths import get_path
# from pathlib import Path
# import json

def user_check_from_path(filepath: str) -> None:
    """
    If a user file exists, get the user from it
    Otherwise, create a new file with user input
    """
    file_object = Path(filepath)
    try:
        user = json.loads(file_object.read_text(encoding="utf-8"))
        print(f"Welcome back, {user['username']}")
    except FileNotFoundError:
        user = {
            "first_name": input("Enter your first name:\n> "),
            "last_name": input("Enter your last name:\n> ")
        }
        user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
        file_object.write_text(json.dumps(user), encoding="utf-8")
        print(f"We'll remember you when you come back, {user['username']}")

file_name = "user.json"
file_path = get_path(file_name, "Files")
user_check_from_path(file_path)
