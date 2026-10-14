"""Enum Methods"""

from enum import Enum
from datetime import date

class Weekday(Enum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, day: date) -> Enum:
        """Get weekday name of the given date"""
        return cls(day.isoweekday())

def main() -> None:
    """Main function"""
    day = Weekday.from_date(date.today())
    print(f"Today is {day.name.title()}.")

if __name__ == "__main__":
    main()
