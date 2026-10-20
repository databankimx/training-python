"""Control the number of decimal places shown"""

import math

def format_pi() -> None:
    """Control the number of decimal places shown of π"""
    print(f"π = {math.pi}")
    print(f"π = {math.pi:.5f}")
    print(f"π = {math.pi:.6f}")

def format_currency(val: float) -> None:
    """Always show two decimal places for currency values"""
    print(f"${val}")
    print(f"${val:.2f}")

def main() -> None:
    """Main function"""
    format_pi()
    price = 1.75
    qty = 2
    format_currency(price * qty)

if __name__ == "__main__":
    main()
