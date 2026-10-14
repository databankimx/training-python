"""Assignment 11.1 (3rd Edition)"""

# City, Country: Write a function that accepts two parameters: a city name
#                and a country name. The function should return a single
#                string of the form City, Country, such as "Santiago, Chile".
#                Store the function in a module called `city_functions.py`,
#                and save this file in a new folder so pytest won’t try to
#                run the tests we've already written.
#
#                Create a file called `test_cities.py` that tests the
#                function you just wrote. Write a function called
#                `test_city_country()` to verify that calling your function
#                with values such as 'santiago' and 'chile' results in the
#                correct string. Run the test, and make sure
#                `test_city_country()` passes.

from city_functions import city_country
# pylint: disable = no-name-in-module
from city_functions import city_country_population

def test_city_country():
    """Does the function return the expected data"""
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"

# Assignment 11.2 (3rd Edition)

# Population: Modify your function so it requires a third parameter,
#             population. It should now return a single string of the form
#             City, Country – population xxx, such as "Santiago, Chile –
#             population 5000000". Run the test again, and make sure
#             `test_city_country()` fails this time.
#
#             Modify the function so the population parameter is optional.
#             Run the test, and make sure `test_city_country()` passes again.
#             Write a second test called test_city_country_population() that
#             verifies you can call your function with the values 'santiago',
#             'chile', and 'population=5000000'. Run the tests one more time,
#             and make sure this new test passes.

# from city_functions import city_country_population_broken

def test_city_country_no_pop():
    """Does the function return the expected data"""
    result = city_country_population("santiago", "chile")
    assert result == "Santiago, Chile"

def test_city_country_pop():
    """Does the function return the expected data"""
    result = city_country_population("santiago", "chile", population=5_000_000)
    assert result == "Santiago, Chile - Pop: 5000000"

# def test_city_country_no_pop_broken():
#     """Does the function return the expected data"""
#     result = city_country_population_broken("santiago", "chile")
#     assert result == "Santiago, Chile"

# def test_city_country_pop_broken():
#     """Does the function return the expected data"""
#     result = city_country_population_broken("santiago", "chile", population=5_000_000)
#     assert result == "Santiago, Chile - Pop: 5000000"
