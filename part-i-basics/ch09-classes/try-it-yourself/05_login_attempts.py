"""Assignment 9.5"""

# Login Attempts: Add an attribute called `login_attempts` to your User
#                 class from Exercise 9-3. Write a method called
#                 `increment_login_attempts()` that increments the value
#                 of `login_attempts` by 1. Write another method called
#                 `reset_login_attempts()` that resets the value of
#                 `login_attempts` to 0.
#
#                 Make an instance of the User class and call
#                 `increment_login_attempts()` several times. Print the
#                 value of `login_attempts` to make sure it was
#                 incremented properly, and then call `reset_login_attempts()`.
#                 Print `login_attempts` again to make sure it was reset to 0.

print("Try-it-Yourself:")
print("Assignment 9.5")

class User:
    """Defines a user"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"Name:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the number of login attempts"""
        print(f"Login Attempts: {self.login_attempts}")

user = User("john", "doe")
user.describe()
user.get_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()
