"""Formulaic recursive Fibonacci algorithm"""

from count_calls import CountCalls

PHI = (1 + 5 ** 0.5) / 2

@CountCalls
def fibonacci(n):
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    return int((PHI ** n - (1 - PHI) ** n) / (PHI - (1 - PHI)))

def main() -> None:
    """Main program"""
    n = 40
    print(f"Calculated F({n}) = {fibonacci(n):,}")
    print(f"call_count = {fibonacci.call_count:,}")

if __name__ == "__main__":
    main()
