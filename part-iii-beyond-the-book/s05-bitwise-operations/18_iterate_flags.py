"""Using bit-shifts to iterate through bit flags"""

from enum import IntFlag
from random import randint

class Settings(IntFlag):
    """Define settings as a bit-flag"""
    DebugMode = 1
    InteractiveMode = 2
    RememberSettings = 4
    Optimize = 8

def main() -> None:
    """Main program"""
    settings = randint(0, 15)
    print(f"With Settings: {settings}, the following bits are set:")
    currentValue = 1
    while settings > 0:
        if settings & 1:
            print(f"- {Settings(currentValue).name}")
        settings >>= 1
        currentValue <<= 1

if __name__ == "__main__":
    main()
