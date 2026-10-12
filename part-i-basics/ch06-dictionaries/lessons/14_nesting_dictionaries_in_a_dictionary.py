"""Lesson 6.14"""

print("Chapter 6:")
print("Exercise 14 - Nesting Dictionaries in a Dictionary")

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    print(f"\tName: {full_name.title()}")
    print(f"\tLocation: {user_info['location'].title()}")
