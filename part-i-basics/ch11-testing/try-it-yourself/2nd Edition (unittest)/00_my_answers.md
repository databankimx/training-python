## Chapter 11 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 11 try-it-yourself exercises.

> Because the 2nd and 3rd editions of the textbook present different 
> approaches to file system interaction, I will present separate solutions for
> these editions for each problem. This file covers the 2nd edition answers,
> which use the `unittest` library.

---

### Assignment 11.1 - City, Country

Write a function that accepts two parameters: a city name and a country name. 
The function should return a single string of the form City, Country, such as 
`Santiago, Chile`. Store the function in a module called `city_functions.py`.

Create a file called `test_cities.py` that tests the function you just wrote 
(remember that you need to import `unittest` and the function you want to 
test). Write a method called `test_city_country()` to verify that calling 
your function with values such as `santiago` and `chile` results in the 
correct string. Run `test_cities.py`, and make sure `test_city_country()` 
passes.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>City Functions</summary>

In [city_functions.py](./city_functions.py)

```python
def city_country(city, country):
    """Return formatted city and country string"""
    return f"{city}, {country}".title()
```

</details>
<br>

<details>
<summary>Test Case</summary>

```python
import unittest
from city_functions import city_country

def main():
    unittest.main()

class LocationTestCase(unittest.TestCase):
    def test_city_country(self):
        location = city_country("dublin", "ireland")
        self.assertEqual(location, "Dublin, Ireland")

if __name__ == "__main__":
    main()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

</details>
<br>

---

### Assignment 11.2 - Population

Modify your function so it requires a third parameter, `population`. It 
should now return a single string of the form 
`City, Country – population xxx`, such as 
`Santiago, Chile – population 5000000`. Run `test_cities.py` again. Make sure 
`test_city_country()` fails this time. Modify the function so the population 
parameter is optional. Run `test_cities.py` again, and make sure 
`test_city_country()` passes again.

Write a second test called `test_city_country_population()` that verifies you 
can call your function with the values `santiago`, `chile`, and 
`population = 5000000`. Run `test_cities.py` again, and make sure this new 
test passes.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>City Functions</summary>

```python
def city_country_pop_broken(city, country, population):
    """Return formatted city, country, population string"""
    return f"{city}, {country} - population {population}".title()

def city_country_pop(city, country, population=None):
    """Return formatted city, country, population string"""
    if population:
        return f"{city}, {country} - population {population}".title()
    return f"{city}, {country}".title()
```

</details>
<br>

<details>
<summary>Test Case</summary>

```python
import unittest
from city_functions import city_country_pop
# from city_functions import city_country_pop_broken

def main():
    unittest.main()

class CityCountryPopTestCase(unittest.TestCase):
    def test_city_country(self):
        location = city_country_pop("dublin", "ireland")
        # location = city_country_pop_broken("dublin", "ireland")
        self.assertEqual(location, "Dublin, Ireland")

    def test_city_country_pop(self):
        location = city_country_pop("dublin", "ireland", 544_107)
        self.assertEqual(location, "Dublin, Ireland - Population 544107")

if __name__ == "__main__":
    main()
```

</details>

</details>
<br>

> Note: to see the failure below, uncomment the `city_country_pop_broken` import
> (line 20 of the code file) and the call in `test_city_country()` (line 32).
> Comment them out again to see the passing run.

<details>
<summary>Output (Failure)</summary>

```
E.
======================================================================
ERROR: test_city_country (__main__.CityCountryPopTestCase.test_city_country)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...\02_population.py", line 32, in test_city_country
    location = city_country_pop_broken("dublin", "ireland")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: city_country_pop_broken() missing 1 required positional argument: 'population'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=1)
```

</details>
<br>

<details>
<summary>Output (Success)</summary>

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

</details>

---

### Assignment 11.3 - Employee

Write a class called `Employee`. The `__init__()` method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called `give_raise()` that adds $ 5,000 to the annual salary by default but also accepts a different raise amount.

Write a test case for `Employee`. Write two test methods,  `test_give_default_raise()` and `test_give_custom_raise()`. Use the `setUp()` method so you don't have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>Employee Class</summary>

```python
class Employee():
    """Class to model an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def show_details(self):
        """Show details of the employee"""
        print(f"{self.first_name} {self.last_name} - Salary : " + \
              f"${self.annual_salary}".title())

    def give_raise(self, amount = 5000):
        """Give the employee a raise"""
        self.annual_salary += amount
```

</details>
<br><details>
<summary>Test Case</summary>

```python
import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("joe", "coder", 50_000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55_000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10_000)
        # Note: This test uses the value from setUp and does not
        #       include the increment from the previous unit test
        self.assertEqual(self.employee.annual_salary, 60_000)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

</details>
<br>

---
