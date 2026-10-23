"""Bitwise AND, and even-number checks using modulo and bitwise AND"""

def is_even_mod(n: int) -> bool:
    """Check if a number is even (using modulo)"""
    return not n % 2

def is_even_and(n: int) -> bool:
    """Check if a number is even (using bitwise AND)"""
    return not n & 1

def main() -> None:
    """Test bitwise AND"""
    a = 0b10011100 # 156
    b = 0b00110100 # 52
    print(f"{bin(a & b)[2:]:>08}") # --> 00010100 (20)

    x = 156
    y = 52
    print(x & y) # --> 20

    for n in [42, 73]:
        print(f"Using 'n % 2', {n} is {('even' if is_even_mod(n) else 'odd')}")
        print(f"Using 'n & 1', {n} is {('even' if is_even_and(n) else 'odd')}")

if __name__ == "__main__":
    main()
