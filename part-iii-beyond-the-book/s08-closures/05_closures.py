"""Closures"""

def generate_power(exponent: int) -> callable:
    """Closure factory (creates a new closure each time it is called)"""
    def power(base: int) -> int:
        """Inner function will be created with the exponent known"""
        return base ** exponent
    return power

def main() -> None:
    """Instantiating and using a closure"""
    squared = generate_power(2)
    print("\ncalling `squared()`...")
    for n in range(1, 6):
        print(f"{n}² = {squared(n)}")

    cubed = generate_power(3)
    print("\ncalling `cubed()`...")
    for n in range(1, 6):
        print(f"{n}³ = {cubed(n)}")

    print("\ncalling `squared()` again...")
    for n in range(1, 6):
        print(f"{n}² = {squared(n)}")

if __name__ == "__main__":
    main()
