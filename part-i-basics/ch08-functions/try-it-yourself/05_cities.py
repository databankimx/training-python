"""Assignment 8.5"""

# Cities: Write a function called `describe_city()` that accepts the
#         name of a city and its country. The function should print a
#         simple sentence, such as "Reykjavik is in Iceland." Give the
#         parameter for the country a default value. Call your function
#         for three different cities, at least one of which is not in
#         the default country.

print("Try-it-Yourself:")
print("Assignment 8.5")

def describe_city(city, country="united states"):
    """Print a description of a city"""
    prefix = ""
    if country.lower() == "united states":
        prefix = "the "
    print(f"{city.title()} is in {prefix}{country.title()}")

describe_city("dallas")
describe_city("cleveland")
describe_city("ensenada", "mexico")
