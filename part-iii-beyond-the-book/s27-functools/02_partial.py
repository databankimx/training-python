"""Creating new functions with partial()"""

from functools import partial


def power(base: int, exponent: int) -> int:
    """Raise base to the power of exponent"""
    return base**exponent


def partial_example() -> None:
    """Fix one argument to make two new functions"""
    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    print(square(5))
    print(cube(3))
    print()


def main() -> None:
    """Run the partial example"""
    partial_example()


if __name__ == "__main__":
    main()
