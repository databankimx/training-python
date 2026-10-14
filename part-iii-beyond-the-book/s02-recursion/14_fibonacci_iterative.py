"""Iterative Fibonacci algorithm"""

from count_calls import CountCalls

@CountCalls
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (iterative algorithm)"""
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]

def main() -> None:
    """Main function to test the Fibonacci function"""
    n = 40
    print(f"Calculated F({n}) = {fibonacci(n):,}")
    print(f"call_count = {fibonacci.call_count:,}")

if __name__ == "__main__":
    main()
