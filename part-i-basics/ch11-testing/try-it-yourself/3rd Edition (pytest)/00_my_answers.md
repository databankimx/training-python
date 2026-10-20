## Chapter 11 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 11 try-it-yourself exercises.

> Because the 2nd and 3rd editions of the textbook present different 
> approaches to file system interaction, I will present separate solutions for
> these editions for each problem. This file covers the 3rd edition answers,
> which use the `pytest` library.

---

### Assignment 11.1 - City, Country

> Note: Assignments 11.1 and 11.2 are in [test_cities.py](./test_cities.py)

Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form `City, Country`, such as `Santiago, Chile`.

Store the function in a module called `city_functions.py`, and save this file in a new folder so pytest won't try to run the tests we've already written.

Create a file called `test_cities.py` that tests the function you just wrote. Write a function called `test_city_country()` to verify that calling your function with values such as `santiago` and `chile` results in the correct string. Run the test, and make sure `test_city_country()` passes.

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
from city_functions import city_country

def test_city_country():
    """Does the function return the expected data"""
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
=================== test session starts ===================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 1 item

test_cities.py .                                     [100%]

==================== 1 passed in 0.03s ====================
```

</details>
<br>

---

### Assignment 11.2 - Population

Modify your function so it requires a third parameter, `population`. It 
should now return a single string of the form 
`City, Country – population xxx`, such as
`Santiago, Chile – population 5000000`. Run the test again, and make sure 
`test_city_country()` fails this time.

Modify the function so the population parameter is optional. Run the test, 
and make sure `test_city_country()` passes again. Write a second test called 
`test_city_country_population()` that verifies you can call your function 
with the values `santiago`, `chile`, and `population=5000000`. Run the tests 
one more time, and make sure this new test passes.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>City Functions</summary>

In [city_functions.py](./city_functions.py)

```python
def city_country_population(city, country, population=None):
    """Return formatted city, country and population"""
    pop_str = "" if population is None else f" - pop: {population}"
    return f"{city}, {country}{pop_str}".title()

def city_country_population_broken(city, country, population):
    """Return formatted city, country and population"""
    return f"{city}, {country} - pop: {population}".title()
```

</details>
<br>

<details>
<summary>Test Case (Failure)</summary>

```python
from city_functions import city_country_population_broken

def test_city_country_no_pop_broken():
    """Does the function return the expected data"""
    result = city_country_population_broken("santiago", "chile")
    assert result == "Santiago, Chile"

def test_city_country_pop_broken():
    """Does the function return the expected data"""
    result = city_country_population_broken("santiago", "chile", population=5_000_000)
    assert result == "Santiago, Chile - Pop: 5000000"
```

</details>
<br>

<details>
<summary>Test Case (Success)</summary>

```python
from city_functions import city_country_population

def test_city_country_no_pop():
    """Does the function return the expected data"""
    result = city_country_population("santiago", "chile")
    assert result == "Santiago, Chile"

def test_city_country_pop():
    """Does the function return the expected data"""
    result = city_country_population("santiago", "chile", population=5_000_000)
    assert result == "Santiago, Chile - Pop: 5000000"
```

</details>

</details>
<br>

<details>
<summary>Output</summary>
<br>

<details>
<summary>Output (Failure)</summary>

```
========================== test session starts ==========================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_cities.py F.                                                  [100%]
=============================== FAILURES ================================
____________________ test_city_country_no_pop_broken ____________________

    def test_city_country_no_pop_broken():
        """Does the function return the expected data"""
>       result = city_country_population_broken("santiago", "chile")
E       TypeError: city_country_population_broken() missing 1 required positional argument: 'population'

test_cities.py:43: TypeError
======================== short test summary info ========================
FAILED test_cities.py::test_city_country_no_pop_broken - TypeError: city_country_population_broken() missing 1 required positional argument: 'population'
====================== 1 failed, 1 passed in 0.08s ======================
```

</details>
<br>

<details>
<summary>Output (Success)</summary>

```
========================== test session starts ==========================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_cities.py ..                                                  [100%]

=========================== 2 passed in 0.01s ===========================
```

</details>

</details>
<br>

---

### Assignment 11.3 - Employee

Write a class called `Employee`. The `__init__()` method should take in a 
first name, a last name, and an annual salary, and store each of these as 
attributes. Write a method called `give_raise()` that adds $5,000 to the 
annual salary by default but also accepts a different raise amount.

Write a test file for Employee with two test functions, 
`test_give_default_raise()` and `test_give_custom_raise()`. Write your tests 
once without using a fixture, and make sure they both pass. Then write a 
fixture so you don't have to create a new employee instance in each test 
function. Run the tests again, and make sure both tests still pass.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>Employee Class</summary>

In [employee.py](./employee.py)

```python
class Employee():
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def __str__(self):
        """Return a representation of the employee as a string."""
        return f"{self.first_name} {self.last_name} - " + \
               f"Salary : ${self.annual_salary}".title()

    def give_raise(self, amount=5000):
        """Increase the employee's salary"""
        self.annual_salary += amount
```

</details>
<br>

<details>
<summary>Test without Fixture</summary>

```python
from employee import Employee

def test_give_default_raise():
    """Test that a default raise works correctly."""
    employee = Employee("scott", "mclean", 65_000)
    employee.give_raise()
    assert employee.annual_salary == 70_000

def test_give_custom_raise():
    """Test that a custom raise works correctly."""
    employee = Employee("scott", "mclean", 65_000)
    employee.give_raise(10000)
    assert employee.annual_salary == 75_000
```

</details>
<br>

<details>
<summary>Test with Fixture</summary>

```python
import pytest
from employee import Employee

@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    employee = Employee("scott", "mclean", 65_000)
    return employee

def test_give_default_raise(employee: Employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.annual_salary == 70_000

def test_give_custom_raise(employee: Employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.annual_salary == 75_000
```

</details>

</details>
<br>

<details>
<summary>Output</summary>
<br>

<details>
<summary>Output without Fixture</summary>

```
=================== test session starts ===================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_employee.py ..                                  [100%]

==================== 2 passed in 0.02s ====================
```

</details>
<br>

<details>
<summary>Output with Fixture</summary>

```
=================== test session starts ===================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_employee.py ..                                  [100%]

==================== 2 passed in 0.02s ====================
```

</details>

</details>

---

