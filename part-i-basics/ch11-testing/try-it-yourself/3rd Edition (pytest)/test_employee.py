"""Assignment 11.3 (3rd Edition)"""

# Employee: Write a class called Employee. The `__init__()` method should
#           take in a first name, a last name, and an annual salary, and
#           store each of these as attributes. Write a method called
#           give_raise() that adds $5,000 to the annual salary by default
#           but also accepts a different raise amount.
#
#           Write a test file for Employee with two test functions,
#           `test_give_default_raise()` and `test_give_custom_raise()`.
#           Write your tests once without using a fixture, and make sure
#           they both pass. Then write a fixture so you don't have to
#           create a new employee instance in each test function.
#           Run the tests again, and make sure both tests still pass.

import pytest
from employee import Employee

# def test_give_default_raise():
#     """Test that a default raise works correctly."""
#     employee = Employee("scott", "mclean", 65_000)
#     employee.give_raise()
#     assert employee.annual_salary == 70_000

# def test_give_custom_raise():
#     """Test that a custom raise works correctly."""
#     employee = Employee("scott", "mclean", 65_000)
#     employee.give_raise(10000)
#     assert employee.annual_salary == 75_000

@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    fixed_employee = Employee("scott", "mclean", 65_000)
    return fixed_employee

# pylint: disable=redefined-outer-name

def test_give_default_raise(employee: Employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.annual_salary == 70_000

def test_give_custom_raise(employee: Employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.annual_salary == 75_000
