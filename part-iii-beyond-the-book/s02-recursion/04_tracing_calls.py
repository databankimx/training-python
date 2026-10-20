"""Tracing recursive calls"""

def factorial(n: int) -> int | None:
    """Calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None

    print(f"factorial({n}) called...")
    f = 1 if n < 2 else n * factorial(n - 1)
    print(f"factorial({n}) returns {f}...")
    return f

def main() -> None:
    """Main function"""
    n = 5
    print(f"\n{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()
