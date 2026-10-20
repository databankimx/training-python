"""Assignment 11.2 (2nd Edition)"""

# Population: Modify your function so it requires a third parameter,
#             `population`. It should now return a single string of the form
#             "City, Country – population xxx", such as "Santiago, Chile –
#             population 5000000". Run `test_cities.py` again. Make sure
#             `test_city_country()` fails this time.
#
#             Modify the function so the population parameter is optional.
#             Run test_cities.py again, and make sure `test_city_country()`
#             passes again.
#
#             Write a second test called `test_city_country_population()`
#             that verifies you can call your function with the values
#             'santiago', 'chile', and 'population=5000000'. Run
#             `test_cities.py` again, and make sure this new test passes.

import unittest
from city_functions import city_country_pop
# from city_functions import city_country_pop_broken

def main():
    """Perform unit tests"""
    print("Try-it-Yourself:\nAssignment 11.2\n")
    unittest.main()

class CityCountryPopTestCase(unittest.TestCase):
    """Test the city_country_pop function"""
    def test_city_country(self):
        """Test the function with city and country"""
        location = city_country_pop("dublin", "ireland")
        # location = city_country_pop_broken("dublin", "ireland")
        self.assertEqual(location, "Dublin, Ireland")

    def test_city_country_pop(self):
        """Test the function with city, country, and population"""
        location = city_country_pop("dublin", "ireland", 544_107)
        self.assertEqual(location, "Dublin, Ireland - Population 544107")

if __name__ == "__main__":
    main()
