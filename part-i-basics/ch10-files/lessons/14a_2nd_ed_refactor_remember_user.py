"""Lesson 10.14a (2nd Edition)"""

import os
import json
from sm_utils import clear_terminal

print("Chapter 10:")
print("Exercise 14 - Refactoring Code\n")

clear_terminal()

# --- 2nd Edition Method ---

USER_FILE = "user.json"
USER_DIR = "Files"

def get_user_path() -> str:
    """Returns the path to the user JSON file"""
    root_dir = os.path.dirname(__file__)
    return os.path.join(root_dir, USER_DIR, USER_FILE)

def read_user_file(file_path: str) -> dict[str, str] | None:
    """Reads the user JSON file and returns the `user` dictionary"""
    try:
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def write_user_file(user: dict[str, str], file_path: str) -> None:
    """Writes the `user` dictionary to the user JSON file"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user, f)

def get_user_input() -> dict[str, str]:
    """Collects user input and returns the `user` dictionary"""
    user = {
        "first_name": input("Enter your first name:\n> "),
        "last_name": input("Enter your last name:\n> ")
    }
    user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
    return user

def check_returning_user() -> None:
    """Checks if a user is returning or not"""
    path = get_user_path()
    user = read_user_file(path)
    if user is None:
        user = get_user_input()
        write_user_file(user, path)
        print(f"We'll remember you next time, {user['username']}")
    else:
        print(f"Welcome back, {user['username']}!")

check_returning_user()
