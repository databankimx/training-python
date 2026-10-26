"""Pairing and mapping: zip_longest() and starmap()"""

from itertools import starmap, zip_longest


def zip_longest_example() -> None:
    """Pair items from iterables of different lengths"""
    print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")))
    print()


def starmap_example() -> None:
    """Call a function once per tuple of arguments"""
    print(list(starmap(pow, [(2, 3), (3, 2)])))
    print()


def main() -> None:
    """Run each pairing and mapping example"""
    zip_longest_example()
    starmap_example()


if __name__ == "__main__":
    main()
