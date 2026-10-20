"""Module for employee class and functions"""

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
