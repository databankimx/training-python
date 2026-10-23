"""Caching results with lru_cache()"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth Fibonacci number, using the cache for repeated calls"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def cached_fibonacci_example() -> None:
    """Compute a Fibonacci number and show the cache statistics"""
    print(fib(30))
    print(fib.cache_info())
    print()


def main() -> None:
    """Run the lru_cache example"""
    cached_fibonacci_example()


if __name__ == "__main__":
    main()
