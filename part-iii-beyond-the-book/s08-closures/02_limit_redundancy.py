"""Using an inner function to limit redundancy"""

def factorial(n: int) -> int | None:
    """Calculate the factorial of n (n!)"""
    print(f"Validate input ({n})...")
    if not isinstance(n, int) or n < 0:
        print(f"Invalid input [{n}]! Must be a non-negative integer.")
        return None

    def inner_factorial(n: int) -> int:
        print(f"inner_factorial called with {n}...")
        if n < 2:
            return 1
        return n * inner_factorial(n - 1)

    return inner_factorial(n)

def main() -> None:
    """Main function"""
    n = 5
    print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()
