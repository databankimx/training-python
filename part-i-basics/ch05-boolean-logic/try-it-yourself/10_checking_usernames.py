"""Assignment 5.10"""

# Checking Usernames: Simulate unique username enforcement.
#   • current_users: list of existing users
#   • new_users: list with some duplicates
#   • Check case-insensitively, print availability for each new username.

print("Try-it-Yourself:")
print("Assignment 5.10")

current_users = ["Anna", "Bob", "Charlie", "Diana", "Admin"]
lower_case_users = []
for user in current_users:
    lower_case_users.append(user.lower())
new_users = ["abigail", "bob", "curtis", "diana", "edward"]
for user in new_users:
    if user.lower() in lower_case_users:
        print(f"Sorry. Username {user} is already in use. Choose another username")
    else:
        print(f"Username {user} is available.")
        current_users.append(user.title())
        lower_case_users.append(user.lower())
print("Final list of users:")
print(current_users)
