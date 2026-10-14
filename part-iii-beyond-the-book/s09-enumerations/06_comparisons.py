"""Enum Comparisons"""

import sys
from enum import Enum, IntEnum

class Weekday(Enum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    HUMP_DAY = 3

class IntWeekday(IntEnum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    HUMP_DAY = 3

def check_types():
    """Review the data types"""
    print("type(Weekday.MONDAY):",
          type(Weekday.MONDAY))
    print("isinstance(Weekday.MONDAY, int):",
          isinstance(Weekday.MONDAY, int))
    print("type(Weekday.MONDAY.value):", 
        type(Weekday.MONDAY.value))
    print("isinstance(Weekday.MONDAY.value, int):",
        isinstance(Weekday.MONDAY.value, int))
    print("type(IntWeekday.MONDAY):",
          type(IntWeekday.MONDAY))
    print("isinstance(IntWeekday.MONDAY, int):",
          isinstance(IntWeekday.MONDAY, int))
    print("type(IntWeekday.MONDAY.value):", 
        type(IntWeekday.MONDAY.value))
    print("isinstance(IntWeekday.MONDAY.value, int):",
        isinstance(IntWeekday.MONDAY.value, int))

def check_equivalency():
    """Perform equivalency `==` comparisons"""
    print("Weekday.MONDAY == IntWeekday.MONDAY:",
          Weekday.MONDAY == IntWeekday.MONDAY)
    print("Weekday.MONDAY.value == IntWeekday.MONDAY.value:",
          Weekday.MONDAY.value == IntWeekday.MONDAY.value)
    print("Weekday.MONDAY == 1:",
          Weekday.MONDAY == 1)
    print("IntWeekday.MONDAY == 1:",
          IntWeekday.MONDAY == 1)
    print("Weekday.MONDAY.value == 1:",
          Weekday.MONDAY.value == 1)
    print("IntWeekday.MONDAY.value == 1:",
          IntWeekday.MONDAY.value == 1)

# pylint: disable=literal-comparison
def check_identity():
    """Perform identity `is` comparisons"""
    print("Weekday.MONDAY is IntWeekday.MONDAY:",
          Weekday.MONDAY is IntWeekday.MONDAY)
    print("Weekday.MONDAY.value is IntWeekday.MONDAY.value:",
          Weekday.MONDAY.value is IntWeekday.MONDAY.value)
    print("Weekday.MONDAY is 1:",
          Weekday.MONDAY is 1)
    print("IntWeekday.MONDAY is 1:",
          IntWeekday.MONDAY is 1)
    print("Weekday.MONDAY.value is 1:",
          Weekday.MONDAY.value is 1)
    print("IntWeekday.MONDAY.value is 1:",
          IntWeekday.MONDAY.value is 1)

def check_inequalities() -> None:
    """Perform inequality `>`, `<`, `>=`, `<=`, comparisons"""
    # This results in a TypeError
    # print("Weekday.MONDAY < Weekday.TUESDAY:",
    #       Weekday.MONDAY < Weekday.TUESDAY)
    print("IntWeekday.MONDAY < IntWeekday.TUESDAY:",
        IntWeekday.MONDAY < IntWeekday.TUESDAY)
    print("Weekday.MONDAY.value < Weekday.TUESDAY.value:",
          Weekday.MONDAY.value < Weekday.TUESDAY.value)
    print("IntWeekday.MONDAY.value < IntWeekday.TUESDAY.value:",
        IntWeekday.MONDAY.value < IntWeekday.TUESDAY.value)

def pause(end: bool=False) -> None:
    """Wait for user input"""
    act = "end program" if end else "continue"
    input(f"\nPress <ENTER> to {act}...")
    if end:
        sys.exit()

def clear_terminal(end: str="") -> None:
    """Clear the terminal"""
    print("\033c", end=end)

def main() -> None:
    """Main program"""
    clear_terminal()
    print(check_types.__doc__, "\n")
    check_types()
    pause()

    clear_terminal()
    print(check_equivalency.__doc__, "\n")
    check_equivalency()
    pause()

    clear_terminal()
    print(check_identity.__doc__, "\n")
    check_identity()
    pause()

    clear_terminal()
    print(check_inequalities.__doc__, "\n")
    check_inequalities()
    pause(True)

if __name__ == "__main__":
    main()
