"""Lesson 2.4"""

print("Chapter 2:")
print("Exercise 4 - Manipulating String Case")

name = "ada lovelace"
print(f"Title Case: {name.title()}")
print(f"UPPER CASE: {name.upper()}")
print(f"lower case: {name.lower()}")
print(f"Sentence case: {name.capitalize()}")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
