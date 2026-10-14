"""Module to define recursion"""

import sys

def recursion_overflow() -> None:
    """Demonstrates exceeding max recursion depth"""
    recursion_overflow()

def main() -> None:
    """Main process"""
    print(f"Max recursion depth: {sys.getrecursionlimit()}")
    recursion_overflow()

if __name__ == "__main__":
    main()
