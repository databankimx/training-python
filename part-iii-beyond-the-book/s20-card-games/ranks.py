"""Defines the ranks in a deck of cards"""

from enum import Enum
from suits import Suits

class Ranks(Enum):
    """Defines the ranks in a deck of cards"""
    BACK = 0
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    @classmethod
    def glyph(cls, rank: Enum, suit: Suits) -> str:
        """Gets the unicode character for the card"""
        val = rank.value
        base_hex = 0x1f000
        suits = [0xa0, 0xb0, 0xc0, 0xd0]
        code = val if val < 12 else val + 1
        return chr(base_hex + suits[suit.value] + code)

    # pylint: disable=function-redefined
    # pylint: disable=arguments-renamed
    @classmethod
    def name(cls, rank: Enum) -> str:
        """Returns the rank name"""
        return rank._name_.title()

    @classmethod
    def initial(cls, rank: Enum) -> str:
        """Gets the first letter of the rank for abbreviating a card name"""
        if 1 < rank.value < 11:
            return str(rank.value)
        return rank._name_[0]
