"""Lesson 5.7"""

user_entry = input("Enter whatever you want:\n> ")

if not user_entry.strip():
    data = "nothing"
else:
    data = user_entry.strip()
print(f"You entered: [{data}]")

data = "nothing" if user_entry.strip() == "" else user_entry.strip()
print(f"You entered: [{data}]")

print(f"You entered: [{'nothing' if user_entry.strip() == '' else user_entry.strip()}]")
