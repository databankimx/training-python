"""Assignment 9.11"""

# Imported Admin: Start with your work from Exercise 9-8. Store the
#                 classes `User`, `Privileges`, and `Admin` in one
#                 module. Create a separate file, make an `Admin`
#                 instance, and call `show_privileges()` to show that
#                 everything is working correctly.

from full_user import Admin

print("Try-it-Yourself:")
print("Assignment 9.11")

my_admin = Admin("Sue", "Smith")
my_admin.describe()
my_admin.privileges.show_privileges()
