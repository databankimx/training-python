"""Even Numbers using Bitwise AND"""

def is_even_mod(n: int) -> bool:
    """Check if a number is even (using modulo)"""
    return not n % 2

def is_even_and(n: int) -> bool:
    """Check if a number is even (using bitwise AND)"""
    return not n & 1

def main() -> None:
    """Main function"""
    for n in [42, 73]:
        print(f"Using 'n % 2', {n} is {('even' if is_even_mod(n) else 'odd')}")
        print(f"Using 'n & 1', {n} is {('even' if is_even_and(n) else 'odd')}")

if __name__ == "__main__":
    main()
