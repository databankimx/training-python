"""Filtering with takewhile(), dropwhile(), filterfalse(), and compress()"""

from itertools import compress, dropwhile, filterfalse, takewhile


def takewhile_example() -> None:
    """Keep items from the start until a test first fails"""
    print(list(takewhile(lambda x: x < 4, [1, 2, 3, 4, 1])))
    print()


def dropwhile_example() -> None:
    """Skip items from the start until a test first fails"""
    print(list(dropwhile(lambda x: x < 4, [1, 2, 3, 4, 1])))
    print()


def filterfalse_example() -> None:
    """Keep the items for which a test is false"""
    print(list(filterfalse(lambda x: x % 2 == 0, range(6))))
    print()


def compress_example() -> None:
    """Keep the items whose matching selector is true"""
    print(list(compress("ABCDE", [1, 0, 1, 0, 1])))
    print()


def main() -> None:
    """Run each filtering example"""
    takewhile_example()
    dropwhile_example()
    filterfalse_example()
    compress_example()


if __name__ == "__main__":
    main()
