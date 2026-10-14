"""Aliases and Uniqueness"""

from enum import Enum, auto, unique

class TiffCompression(Enum):
    """Defines names for days of the week"""
    NONE = auto()
    LZW = auto()
    ZIP = auto()
    PACKBITS = auto()
    CCITT_T4 = auto()
    CCITT_T6 = auto()
    GROUP_III = CCITT_T4
    GROUP_IV = CCITT_T6

@unique
class NoRepeats(Enum):
    """Defines names for numbers"""
    ONE = 1
    TWO = 2
    THREE = 3
    # TRES = 3

def main() -> None:
    """Main function"""
    print(TiffCompression.CCITT_T6.name, TiffCompression.CCITT_T6.value)
    print(TiffCompression.GROUP_IV.name, TiffCompression.GROUP_IV.value)

    print()

    print(TiffCompression.__members__)

if __name__ == "__main__":
    main()
