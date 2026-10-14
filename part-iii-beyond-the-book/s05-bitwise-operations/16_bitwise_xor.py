"""Bitwise XOR"""

def swap_values(a: int, b: int) -> tuple[int, int]:
    """Swap the values of two variables"""
    a = a ^ b
    b = b ^ a
    a = a ^ b
    return a, b

def main() -> None:
    """Test bitwise XOR"""
    a = 0b10011100 # 156
    b = 0b00110100 # 52
    print(f"{(a ^ b):>08b}") # --> 10101000 (168)

    x = 156
    y = 52
    print(x ^ y) # --> 168

    a = 5
    b = 8
    print(f"a = {a}, b = {b}")

    # We know we could do this natively in Python
    # a, b = b, a

    # But to illustrate the XOR method, we'll do this:
    a, b = swap_values(a, b)
    print(f"a = {a}, b = {b}")

if __name__ == "__main__":
    main()
