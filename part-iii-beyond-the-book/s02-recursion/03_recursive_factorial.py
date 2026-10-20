"""Compute factorials using recursion"""

def factorial(n: int) -> int | None:
    """Calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    if n < 2:
        return 1
    return n * factorial(n - 1)

def main() -> None:
    """Main process to test factorial function"""
    for n in range(10):
        print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()
