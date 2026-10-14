"""Digit grouping"""

def integer_grouping() -> None:
    """Adding grouping separators to integers"""
    n = 1234567
    print(f"{n:,d}\t{n:_d}")
    print(f"{n:,}\t{n:_}\n")

def float_grouping() -> None:
    """Adding grouping separators to floating point numbers"""
    n = 1234567.89
    print(f"{n:,.2f}\t{n:_.2f}")
    print(f"{n:,}\t{n:_}\n")

def main() -> None:
    """Main program"""
    integer_grouping()
    float_grouping()

if __name__ == "__main__":
    main()
