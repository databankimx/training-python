"""Lesson 8.10"""

print("Chapter 8:")
print("Exercise 10 - Passing an Arbitrary Amount of Keyword Arguments")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


def sum_up(x, y, z):
    """Calculate the sum of three numbers."""
    print(f"{x} + {y} + {z} = {x + y + z}")


user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)

values = {"y": 3, "z": 4}

# Uncomment to see the TypeError from passing the dictionary as one argument
# sum_up(2, values)

sum_up(2, **values)
