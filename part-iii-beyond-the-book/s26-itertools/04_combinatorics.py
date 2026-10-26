"""Combinations, permutations, and products"""

from itertools import combinations, permutations, product


def combinations_example() -> None:
    """Choose items where the order does not matter"""
    print(list(combinations("ABC", 2)))
    print()


def permutations_example() -> None:
    """Arrange items where the order matters"""
    print(list(permutations("ABC", 2)))
    print()


def product_example() -> None:
    """Pair every item from one iterable with every item from another"""
    print(list(product([1, 2], ["x", "y"])))
    print()


def main() -> None:
    """Run each combinatorics example"""
    combinations_example()
    permutations_example()
    product_example()


if __name__ == "__main__":
    main()
