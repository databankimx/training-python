"""Assignment 11.3 (2nd Edition)"""

# Employee: Write a class called `Employee`. The `__init__()` method should
#           take in a first name, a last name, and an annual salary, and
#           store each of these as attributes. Write a method called
#           `give_raise()` that adds $5,000 to the annual salary by default
#           but also accepts a different raise amount.
#
#           Write a test case for Employee. Write two test methods,
#           `test_give_default_raise()` and `test_give_custom_raise()`.
#           Use the `setUp()` method so you don’t have to create a new
#           employee instance in each test method. Run your test case,
#           and make sure both tests pass.

import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Class to test Employee"""
    def setUp(self):
        """Set up test"""
        self.employee = Employee("joe", "coder", 50_000)

    def test_give_default_raise(self):
        """Test the give_raise function"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55_000)

    def test_give_custom_raise(self):
        """Test the give_raise function with defaults"""
        self.employee.give_raise(10_000)
        # Note: This test uses the value from setUp and does not
        #       include the increment from the previous unit test
        self.assertEqual(self.employee.annual_salary, 60_000)

def main():
    """Main function"""
    print("Try-it-Yourself:\nAssignment 11.3\n")
    unittest.main()

if __name__ == "__main__":
    main()
