"""Module for city functions"""

def city_country(city, country):
    """Return formatted city and country string"""
    return f"{city}, {country}".title()

def city_country_pop_broken(city, country, population):
    """Return formatted city, country, population string"""
    return f"{city}, {country} - population {population}".title()

def city_country_pop(city, country, population=None):
    """Return formatted city, country, population string"""
    if population:
        return f"{city}, {country} - population {population}".title()
    return f"{city}, {country}".title()
