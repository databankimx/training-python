"""Bitwise AND"""

def main() -> None:
    """Test bitwise AND"""
    a = 0b10011100 # 156
    b = 0b00110100 # 52
    print(f"{bin(a & b)[2:]:>08}") # --> 00010100 (20)

    x = 156
    y = 52
    print(x & y) # --> 20

if __name__ == "__main__":
    main()
