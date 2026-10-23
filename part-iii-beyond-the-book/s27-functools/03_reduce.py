"""Reducing a sequence to one value with reduce()"""

from functools import reduce


def product_example() -> None:
    """Multiply all the numbers in a list together"""
    print(reduce(lambda total, value: total * value, [1, 2, 3, 4]))
    print()


def initial_value_example() -> None:
    """Start the reduction from a given value"""
    print(reduce(lambda total, value: total + value, [1, 2, 3], 10))
    print()


def maximum_example() -> None:
    """Pass a built-in function to reduce()"""
    print(reduce(max, [3, 9, 4]))
    print()


def main() -> None:
    """Run each reduce() example"""
    product_example()
    initial_value_example()
    maximum_example()


if __name__ == "__main__":
    main()
