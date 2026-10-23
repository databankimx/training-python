"""Running totals with accumulate()"""

from itertools import accumulate


def sum_accumulate_example() -> None:
    """Build a running total with the default operation, addition"""
    print(list(accumulate([1, 2, 3, 4])))
    print()


def max_accumulate_example() -> None:
    """Track the largest value seen so far"""
    print(list(accumulate([3, 1, 4, 1, 5], max)))
    print()


def main() -> None:
    """Run each accumulate example"""
    sum_accumulate_example()
    max_accumulate_example()


if __name__ == "__main__":
    main()
