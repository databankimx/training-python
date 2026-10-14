"""A class module allowing modeling of admins"""

from user import User

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
