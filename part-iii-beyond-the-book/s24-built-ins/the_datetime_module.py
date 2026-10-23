"""The datetime module: dates, times, and arithmetic"""

from datetime import date, datetime, timedelta


def date_example() -> None:
    """Create a date and format it with strftime()"""
    launch = date(2024, 3, 15)
    print(launch)
    print(launch.strftime("%d %B %Y"))
    print()


def timedelta_example() -> None:
    """Move a date forward with a timedelta"""
    launch = date(2024, 3, 15)
    print(launch + timedelta(days=30))
    print()


def datetime_example() -> None:
    """Create a date and time, then format them"""
    meeting = datetime(2024, 3, 15, 14, 30)
    print(meeting.isoformat())
    print(meeting.strftime("%A, %H:%M"))
    print()


def subtract_dates_example() -> None:
    """Subtract one date from another to get a timedelta"""
    launch = date(2024, 3, 15)
    days_between = date(2024, 12, 25) - launch
    print(days_between.days)
    print()


def main() -> None:
    """Run each datetime example"""
    date_example()
    timedelta_example()
    datetime_example()
    subtract_dates_example()


if __name__ == "__main__":
    main()
