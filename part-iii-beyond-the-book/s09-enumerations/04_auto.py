"""Automatic Flag Values"""

from enum import Flag, auto

class Weekday(Flag):
    """Defines names for days of the week as bit-flags"""
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    WEEKEND = SATURDAY | SUNDAY

def main() -> None:
    """Main function"""
    for day in [Weekday.SATURDAY, Weekday.SUNDAY, Weekday.WEEKEND]:
        print(day, "=", day.value)
    print()
    for i in [2 ** n for n in range(7)]:
        print(f"{i:>2}", Weekday(i))

if __name__ == "__main__":
    main()
