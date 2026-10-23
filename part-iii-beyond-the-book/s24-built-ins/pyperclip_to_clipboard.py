"""Copy to the clipboard and paste from it!"""

import pyperclip


def copy_example() -> None:
    """Copy text to the clipboard"""
    # Copies to the clipboard
    pyperclip.copy("Hello")
    print()


def paste_example() -> None:
    """Paste text from the clipboard and print it"""
    # Pastes from the clipboard
    my_var = pyperclip.paste()
    print(my_var)
    print()


def main() -> None:
    """Copy the text, then paste it back"""
    copy_example()
    paste_example()


if __name__ == "__main__":
    main()
