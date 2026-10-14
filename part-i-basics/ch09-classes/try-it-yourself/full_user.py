"""A class module to allow modeling users and admins"""

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
        print(f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempt counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempt counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Read the login attempt counter"""
        print(f"Login Attempts: {self.login_attempts}\n")

class Admin(User):
    """Define an admin ad a subclass of User"""

    def __init__(self, first_name, last_name, privileges = None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

# pylint: disable=too-few-public-methods
class Privileges:
    """Define a collection of user privileges"""

    def __init__(self, privileges = None):
        """Initialize a new instance of the Privileges class"""
        if privileges is None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the list of user privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
