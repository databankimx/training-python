"""Grouping items with groupby()"""

from itertools import groupby

DATA = [("fruit", "apple"), ("fruit", "pear"), ("veg", "kale"), ("fruit", "plum")]


def print_groups(rows: list[tuple[str, str]]) -> None:
    """Print each group's key and its items"""
    for key, group in groupby(rows, key=lambda row: row[0]):
        items = ", ".join(item for _, item in group)
        print(f"{key}: {items}")


def unsorted_groupby_example() -> None:
    """Show that groupby() only groups neighboring items"""
    print_groups(DATA)
    print()


def sorted_groupby_example() -> None:
    """Sort the data first so that each key forms one group"""
    print_groups(sorted(DATA, key=lambda row: row[0]))
    print()


def main() -> None:
    """Run each groupby example"""
    unsorted_groupby_example()
    sorted_groupby_example()


if __name__ == "__main__":
    main()
