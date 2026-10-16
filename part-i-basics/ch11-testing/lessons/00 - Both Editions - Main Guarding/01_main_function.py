"""Lesson 11.1"""

from sm_utils import pause, clear_terminal

def main() -> None:
    """Main Function: Test Main Guarding"""
    print("Chapter 11:")
    print("Exercise 1 - Using a `main()` Function\n")

    # pylint: disable=unused-import
    # pylint: disable=import-outside-toplevel

    pause()
    clear_terminal()

    print("Importing unguarded module:\n")
    import hello_no_guard

    pause()
    clear_terminal()

    print("Importing guarded module:\n")
    import hello_with_guard

if __name__ == "__main__":
    main()
