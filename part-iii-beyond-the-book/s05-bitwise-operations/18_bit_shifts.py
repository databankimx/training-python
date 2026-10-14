"""Bit Shifts"""

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

    flag = 0b01010101
    print(f"In value [{flag}], the following bits are set:")
    currentValue = 1
    while flag > 0:
        if flag & 1:
            print(currentValue)
        flag >>= 1
        currentValue <<= 1

if __name__ == "__main__":
    main()
