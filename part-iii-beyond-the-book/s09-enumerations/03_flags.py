"""Flags"""

from enum import Flag
from datetime import date

class Weekday(Flag):
    """Defines names for days of the week as bit-flags"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

    @classmethod
    def from_date(cls, day: date) -> Flag:
        """Get weekday name of the given date"""
        return cls(2 ** day.weekday())

def show_chores(chores: dict[str: Flag], day: Flag) -> None:
    """Show chores for a given day"""
    print(f"Chores for {day.name.title()}:")
    for chore, days in chores.items():
        if day in days:
            print("-", chore)

def main() -> None:
    """Main function"""
    today = Weekday.from_date(date.today())
    print(f"Today is {today.name.title()}.\n")

    first_weekday = Weekday.MONDAY
    print(first_weekday.name, first_weekday.value, "\n")

    weekend = Weekday.SATURDAY | Weekday.SUNDAY
    print(weekend, weekend.value, "\n")

    first_last_weekdays = 17
    print(Weekday(first_last_weekdays), "\n")

    in_weekend = today & weekend == today
    infix = "" if in_weekend else "not "
    print(f"{today.name.title()} is {infix}part of the weekend.\n")

    print("Weekend Days:")
    for day in weekend:
        print(f" - {day.name.title()}")
    print()

    my_chores = {
        "feed the dog": Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
        "do the dishes": Weekday.TUESDAY | Weekday.THURSDAY,
        "answer stack overflow questions": Weekday.MONDAY | Weekday.SATURDAY,
    }

    show_chores(my_chores, Weekday.MONDAY)

if __name__ == "__main__":
    main()
