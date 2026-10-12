"""Assignment 6.11"""

# Cities: Dictionary called cities. Three city names as keys. Each value is a
#         dictionary with country, population, and one fact about the city.

print("Try-it-Yourself:")
print("Assignment 6.11")

cities = {
    "cleveland": {
        "country": "united states",
        "population": 383_331,
        "fact": "Home of the Rock & Roll Hall of Fame"
    },
    "london": {
        "country": "england",
        "population": 8_982_000,
        "fact": "Hosted the 2012 Summer Olympics"
    },
    "ensenada": {
        "country": "mexico",
        "population": 443_807,
        "fact": "Known as the 'Capital del vino Mexicano' (Capital of Mexican wine)"
    },
}

for city, facts in cities.items():
    print(f"\n{city.title()}")
    for heading, fact in facts.items():
        if heading == "country":
            fact = fact.title()
        print(f"\t{heading.upper()}:\n\t\t{fact}")
