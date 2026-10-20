"""Class to model an employee"""

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
