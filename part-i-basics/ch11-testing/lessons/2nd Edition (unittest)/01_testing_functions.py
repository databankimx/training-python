"""Lesson 11.1 (2nd Edition)"""

import unittest

# This function will fail both tests
# def formatted_name(first: str, last: str, middle: str | None="") -> str:
#     """Generate a neatly formatted full name."""
#     ...

# This function will fail the test without a middle name argument
# def formatted_name(first: str, last: str, middle: str | None="") -> str:
#     """Generate a neatly formatted full name."""
#     full_name =  f"{first} {middle} {last}"
#     return full_name.title()

# This function will pass both tests
def formatted_name(first: str, last: str, middle: str | None="") -> str:
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    """Tests for the `formatted_name()` function"""

    def test_with_middle(self) -> None:
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        result = formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(result, "Wolfgang Amadeus Mozart")

    def test_without_middle(self) -> None:
        """Do names like 'Janis Joplin' work?"""
        result = formatted_name("janis", "joplin")
        self.assertEqual(result, "Janis Joplin")

def main():
    """Run the tests"""
    print("Chapter 11:\nExercise 1 - Testing a Function\n")
    unittest.main()

if __name__ == "__main__":
    main()
