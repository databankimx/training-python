"""Class representing a single die"""

from random import randint

# pylint: disable=too-few-public-methods
class Die:
    """Class representing a single die"""

    def __init__(self, num_sides = 6):
        """Initialize - Assume 6-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return random number between 1 and number of sides"""
        return randint(1, self.num_sides)
