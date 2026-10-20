"""Memoized recursive Fibonacci algorithm"""

from count_calls import CountCalls

# pylint: disable=dangerous-default-value
@CountCalls
def fibonacci(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

def main() -> None:
    """Main program"""
    n = 40
    print(f"Calculated F({n}) = {fibonacci(n):,}")
    print(f"call_count = {fibonacci.call_count:,}")

if __name__ == "__main__":
    main()
