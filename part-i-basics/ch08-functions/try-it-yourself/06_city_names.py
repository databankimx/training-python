"""Assignment 8.6"""

# City Names: Write a function called `city_country()` that takes in
#             the name of a city and its country. The function should
#             return a string formatted like this: "Santiago, Chile".
#             Call your function with at least three city-country pairs,
#             and print the values that are returned.

print("Try-it-Yourself:")
print("Assignment 8.6")

def city_country(city, country):
    """Return a string formatted as 'City, Country'"""
    return f"{city.title()}, {country.title()}"

place = city_country("ensenada", "mexico")
print(place)

place = city_country("dublin", "ireland")
print(place)

place = city_country("vienna", "austria")
print(place)
