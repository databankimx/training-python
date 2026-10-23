"""Joining and slicing iterators: chain() and islice()"""

from itertools import chain, islice


def chain_example() -> None:
    """Join several iterables into one sequence"""
    print(list(chain([1, 2], [3], [4, 5])))
    print()


def chain_from_iterable_example() -> None:
    """Join a collection of iterables without unpacking it"""
    print(list(chain.from_iterable([[1, 2], [3, 4]])))
    print()


def islice_example() -> None:
    """Take a slice of any iterable, including one that is not a list"""
    print(list(islice(range(10), 2, 8, 2)))
    print()


def main() -> None:
    """Run each chain and islice example"""
    chain_example()
    chain_from_iterable_example()
    islice_example()


if __name__ == "__main__":
    main()
