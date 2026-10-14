"""Implementation of several Fibonacci methods"""

from count_calls import CountCalls

@CountCalls
def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number (naive algorithm)"""
    if n in [0, 1]:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# pylint: disable=dangerous-default-value
@CountCalls
def fibonacci_recursive_memo(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_recursive_memo(n - 1, cache) + fibonacci_recursive_memo(n - 2, cache)
    return cache[n]

@CountCalls
def fibonacci_iterative(n: int) -> int:
    """Return the nth Fibonacci number (iterative algorithm)"""
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]

@CountCalls
def fibonacci_formulaic(n):
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    phi = (1 + 5 ** 0.5) / 2
    return int((phi ** n - (1 - phi) ** n) / (phi - (1 - phi)))
