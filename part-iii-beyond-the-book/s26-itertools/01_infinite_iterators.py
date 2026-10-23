"""Infinite iterators: count(), cycle(), and repeat()"""

from itertools import count, cycle, islice, repeat


def count_example() -> None:
    """Count upward forever, taking only the first few values with islice()"""
    print(list(islice(count(10, 5), 4)))
    print()


def cycle_example() -> None:
    """Repeat a sequence forever, taking only the first few values"""
    print(list(islice(cycle("ABC"), 7)))
    print()


def repeat_example() -> None:
    """Repeat one value a fixed number of times"""
    print(list(repeat("ha", 3)))
    print()


def main() -> None:
    """Run each infinite iterator example"""
    count_example()
    cycle_example()
    repeat_example()


if __name__ == "__main__":
    main()
