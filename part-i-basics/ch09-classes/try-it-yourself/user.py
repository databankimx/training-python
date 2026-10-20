"""A class module to allow modeling users"""

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
