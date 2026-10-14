"""Defines the suits in a deck of cards"""

from enum import Enum
from colors import Colors

class Suits(Enum):
    """Defines the suits in a deck of card"""
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3

    @classmethod
    def glyph(cls, suit: Enum, color: Colors=Colors.WHITE) -> str:
        """Gets the unicode character for the suit"""
        black = [0x0, 0x5, 0x6, 0x3]
        white = [0x4, 0x1, 0x2, 0x7]
        base_hex = 0x2660
        codes = white if color == Colors.WHITE else black
        return chr(base_hex + codes[suit.value])

    # pylint: disable=function-redefined
    # pylint: disable=arguments-renamed
    @classmethod
    def name(cls, suit: Enum) -> str:
        """Gets the name of the suit"""
        return suit._name_.title()

    @classmethod
    def initial(cls, suit: Enum) -> str:
        """Gets the first letter of the suit for abbreviating a card name"""
        return suit._name_[0]
