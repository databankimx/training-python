"""Assignment 8.13"""

# User Profile: Start with a copy of user_profile.py. Build a profile
#               of yourself by calling `build_profile()`, using your
#               first and last names and three other key-value pairs
#               that describe you.

print("Try-it-Yourself:")
print("Assignment 8.13")

def build_profile(first, last, **user_info):
    """Populate a user-profile dictionary"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

me = build_profile("scott", "mclean",
                   profession="programmer",
                   avocation="musician",
                   hobby="cobbler")
print(me)
