"""Module for city functions"""

def city_country(city, country):
    """Return formatted city and country string"""
    return f"{city}, {country}".title()

def city_country_population(city, country, population=None):
    """Return formatted city, country and population"""
    pop_str = "" if population is None else f" - pop: {population}"
    return f"{city}, {country}{pop_str}".title()

def city_country_population_broken(city, country, population):
    """Return formatted city, country and population"""
    return f"{city}, {country} - pop: {population}".title()
