"""Lesson 8.10"""

print("Chapter 8:")
print("Exercise 10 - Passing an Arbitrary Amount of Keyword Arguments")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)

def sum_up(x, y, z):
    """Calculate the sum of three numbers."""
    print(f"{x} + {y} + {z} = {x + y + z}")

values = {"z": 4, "y": 3}

# This would result in a TypeError
# sum_up(2, values)

sum_up(2, **values)
