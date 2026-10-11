"""Assignment 5.8"""

# Hello Admin: Loop through usernames, print a special greeting for admin
#              and a generic greeting for everyone else.

print("Try-it-Yourself:")
print("Assignment 5.8")

usernames = ["anna", "bob", "charlie", "diana", "admin"]
for user in usernames:
    if user.lower() == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
