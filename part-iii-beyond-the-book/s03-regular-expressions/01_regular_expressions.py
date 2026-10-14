"""Working with regular expressions"""

import re
from sm_utils import pause, clear_terminal

def test_regex_matching(data: list[str], patterns: dict[str, str]) -> None:
    """Test matching patterns with regular expressions"""

    for name, pattern in patterns.items():
        clear_terminal()
        print(f"Using the {name} pattern `{pattern}`")
        print("Matched the following values:")
        regex = re.compile(pattern)
        for item in data:
            if regex.search(item):
                print(f"• {item}")
        pause()

def main() -> None:
    """Main function"""
    phone_numbers = [
        "7134833111",
        "713-483-3111",
        "713.483.3111",
        "713,483,3111",
        "(713) 483-3111",
        "(713) 483-3111 ext: 42",
        "Don't match this one: (713) 483-3111 - BAD"
    ]

    regex_examples = {
        "naive": r"\d{10}",
        "bad": r"\d{3}-\d{3}-\d{4}",
        "mediocre": r"\d{3}[-.,]\d{3}[-.,]\d{4}",
        "not bad": r"\(?\d{3}\)?\s?[-.,]?\d{3}[-.,]?\d{4}",
        "ok": r"^\(?\d{3}\)?[-.,]?\s?\d{3}[-.,]?\d{4}$",
        "good": r"^\(?\d{3}\)?[-.,]?\s?\d{3}[-.,]?\d{4}\s?e?x?t?:?\s?\d*$"
    }

    test_regex_matching(phone_numbers, regex_examples)

if __name__ == "__main__":
    main()
