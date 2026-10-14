"""Assignment 9.12"""

# Multiple Modules: Store the `User` class in one module, and store the
#                   `Privileges` and `Admin` classes in a separate module.
#                   In a separate file, create an `Admin` instance and
#                   call `show_privileges()` to show that everything is
#                   still working correctly.

from admin import Admin

print("Try-it-Yourself:")
print("Assignment 9.12")

my_admin = Admin("Sue", "Smith")
my_admin.describe()
my_admin.privileges.show_privileges()
