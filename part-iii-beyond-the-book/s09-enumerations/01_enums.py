"""Enumerations"""

from enum import Enum

class Weekday(Enum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def main() -> None:
    """Main function"""
    print(Weekday(3), "\n")

    print(repr(Weekday(2)))
    print(str(Weekday(2)), "\n")

    print(Weekday.THURSDAY, "\n")

    print(Weekday.FRIDAY.name)
    print(Weekday.FRIDAY.value, "\n")

    print(type(Weekday.MONDAY))
    print(isinstance(Weekday.MONDAY, Weekday))

if __name__ == "__main__":
    main()
