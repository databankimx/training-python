"""Handling command line arguments"""

import sys

def parse_args() -> None:
    """Read the command-line arguments"""
    separator = "\\" if "\\" in sys.argv[0] else "/"
    script_name = sys.argv[0].split(separator)[-1]
    print(f"I am running {script_name}")

    print("My command line arguments are")

    for i in range(1, len(sys.argv)):
        print(f" - {sys.argv[i]}")

def greet_user() -> None:
    """Read the user's first and last names from the command line and greet"""

    if len(sys.argv) < 3:
        print("Usage: filename.py first_name last_name")
        sys.exit()

    first_name = sys.argv[1].title()
    last_name = sys.argv[2].title()

    print(f"Hello, {first_name} {last_name}")

def main() -> None:
    """Main function"""
    parse_args()
    greet_user()

if __name__ == "__main__":
    main()
