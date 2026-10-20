"""Width, Fill, and Alignment"""

def width() -> None:
    """Set the minimum width of the string"""
    s = "abc"
    print(f"'{s:5}'")
    s = "abcdef"
    print(f"'{s:5}'")
    print(f"'{s:5.5}'\n")

def align() -> None:
    """Set the alignment of the string within the width allotted"""
    s = "abc"
    print(f"left justify:  '{s:<9}'")
    print(f"right justify: '{s:>9}'")
    print(f"center:        '{s:^9}'\n")

def fill() -> None:
    """Fill the string with a character up to the specified width"""
    s = "abc"
    print(f"{s:.>9}")
    print(f"{s:*<9}")
    print(f"{s:~^9}")

def main() -> None:
    """Main program"""
    width()
    align()
    fill()

if __name__ == "__main__":
    main()
