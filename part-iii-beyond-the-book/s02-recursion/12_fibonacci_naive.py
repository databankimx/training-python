"""Naive recursive Fibonacci algorithm"""

from count_calls import CountCalls

@CountCalls
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (naive algorithm)"""
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main() -> None:
    """Main function"""
    n = 40
    print(f"Calculated F({n}) = {fibonacci(n):,}")
    print(f"call_count = {fibonacci.call_count:,}")

if __name__ == "__main__":
    main()
