"""Assignment 10.13 (3rd Edition)"""

# 10-13. User Dictionary: The remember_me.py example only stores one piece
#                         of information, the username. Expand this example
#                         by asking for two more pieces of information about
#                         the user, then store all the information you
#                         collect in a dictionary. Write this dictionary to
#                         a file using json.dumps(), and read it back in
#                         using json.loads(). Print a summary showing
#                         exactly what your program remembers about the user.

import json
from pathlib import Path
from relative_paths import get_path

print("Try-it-Yourself:")
print("Assignment 10.13\n")

file_name = "user_info.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)

if file.exists():
    user = json.loads(file.read_text(encoding="utf-8"))
    print(f"Welcome back, {user['username']}!")
    print("Here's what I know about you:")
    for key, value in user.items():
        if key == "username":
            continue
        print(f"{key.replace('_', ' ').title()}: {value}")
else:
    user = {}
    user_keys = ["first_name", "last_name", "job_title", "location"]
    for key in user_keys:
        user[key] = input(f"Enter your {key.replace('_', ' ')}:\n> ")

    user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()

    file.write_text(json.dumps(user), encoding="utf-8")

    print(f"We'll remember you when you come back, {user['username']}")
