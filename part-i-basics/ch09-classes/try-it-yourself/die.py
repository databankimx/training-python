"""A class module for modeling a fair die"""

from random import randint

# pylint: disable=too-few-public-methods
class Die:
    """Defines an n-sided die"""

    def __init__(self, sides=6):
        """Initialize a new instance of the Die class"""
        self.sides = sides

    def roll(self):
        """Roll the die"""
        return randint(1, self.sides)
