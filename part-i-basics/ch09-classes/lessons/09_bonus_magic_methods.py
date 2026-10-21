"""Lesson 9.9"""

from sm_utils import clear_terminal, pause

print("Chapter 9:")
print("Bonus - Magic (Dunder) Methods and Properties\n")
clear_terminal()
print(dir(int))
pause()

clear_terminal()
print(dir(str))
pause()

# pylint: disable=too-few-public-methods
class PlainPerson:
    """Class to define a person without a __str__ method"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the person class"""
        self.first_name = first_name
        self.last_name = last_name

clear_terminal()
plain_someone = PlainPerson("john", "doe")
print(plain_someone)
pause()

class Person:
    """Class to define a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the person class"""
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """Return a string representation of the person"""
        return f"{self.first_name.title()} {self.last_name.title()}"

clear_terminal()
someone = Person("john", "doe")
print(someone)
pause()

clear_terminal()
print(Person.__doc__)
pause()

clear_terminal()
print(someone.__dict__)
