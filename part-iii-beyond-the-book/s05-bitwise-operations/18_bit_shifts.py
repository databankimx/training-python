"""Bit Shifts"""

from enum import IntFlag
from random import randint

class Settings(IntFlag):
    """Define settings as a bit-flag"""
    DebugMode = 1
    InteractiveMode = 2
    RememberSettings = 4
    Optimize = 8

def print_settings(settings: int) -> None:
    """Print the name of each setting that is switched on"""
    print(f"With Settings: {settings}, the following bits are set:")
    current_value = 1
    while settings > 0:
        if settings & 1:
            print(f"- {Settings(current_value).name}")
        settings >>= 1
        current_value <<= 1

def main() -> None:
    """Main program"""
    x = 128
    b = x >> 3
    print(f"{x} >> 3 = {b}")

    x = 16
    b = x << 3
    print(f"{x} << 3 = {b}")

    # Overflow doesn't happen in Python
    x = 64
    b = x << 3
    print(f"{x} << 3 = {b}")

    # Underflow does
    x = 4
    b = x >> 3
    print(f"{x} >> 3 = {b}")
    print()

    print_settings(10)
    print()
    print_settings(randint(0, 15))

if __name__ == "__main__":
    main()
