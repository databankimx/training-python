"""Recursive vs iterative performance comparison"""

from time import perf_counter_ns
from functools import reduce
from math import factorial

def factorial_rec(n: int) -> int | None:
    """Recursively calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    if n < 2:
        return 1
    return n * factorial_rec(n - 1)

def factorial_iter(n: int) -> int | None:
    """Iteratively calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def factorial_red(n: int) -> int | None:
    """Calculate the factorial of n using `reduce()`"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])

def factorial_def(n: int) -> int | None:
    """Calculate the factorial of n using `math.factorial()`"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    return factorial(n)

def check_performance(func: callable, n: int, r: int) -> int:
    """Evaluate how long it takes to calculate n! r times"""
    start = perf_counter_ns()
    for _ in range(r):
        func(n)
    end = perf_counter_ns()
    return end - start

def main() -> None:
    """Compare the performance of different factorial calculation methods"""
    n = 10
    repeat = 1_000_000
    functions = {
        "Recursive": factorial_rec,
        "Iterative": factorial_iter,
        "Using functools.reduce()": factorial_red,
        "Using math.factorial()": factorial_def
    }
    print(f"Testing {n}! {repeat:,} times for each algorithm...")
    for name, func in functions.items():
        dur = check_performance(func, n, repeat) / 1_000_000_000
        print(f"\n{name}:\n{dur} sec")

if __name__ == "__main__":
    main()
