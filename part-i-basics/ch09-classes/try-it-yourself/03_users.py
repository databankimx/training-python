"""Exercise 9.3"""

# Users: Make a class called User. Create two attributes called
#        `first_name` and `last_name`, and then create several
#        other attributes that are typically stored in a user
#        profile. Make a method called `describe_user()` that
#        prints a summary of the user's information. Make another
#        method called `greet_user()` that prints a personalized
#        greeting to the user. Create several instances representing
#        different users, and call both methods for each user.

print("Try-it-Yourself:")
print("Assignment 9.3")

class User:
    """Defines a user"""

    def __init__(self, first_name, last_name, location, profession):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.profession = profession

    def greet(self):
        """Greet the user"""
        print(
            f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(
            f"Name:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Location:   {self.location.title()}")
        print(f"Profession: {self.profession.title()}\n")

user_1 = User("scott", "mclean", location="dallas", profession="programmer")
user_1.greet()
user_1.describe()

user_2 = User("hillary", "taylor", location="twinsburg", profession="lawyer")
user_2.greet()
user_2.describe()

user_3 = User("jeremy", "mclean", location="columbus",
              profession="restaurant manager")
user_3.greet()
user_3.describe()
