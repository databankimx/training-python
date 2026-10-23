"""any() and all(): test whether some or every item is true"""


def any_example() -> None:
    """Test whether at least one item is true with any()"""
    scores = [88, 92, 75]
    print(any(score > 90 for score in scores))
    print()


def all_example() -> None:
    """Test whether every item is true with all()"""
    scores = [88, 92, 75]
    print(all(score > 80 for score in scores))
    print()


def empty_collection_example() -> None:
    """Show the results of any() and all() for an empty list"""
    print(any([]))
    print(all([]))
    print()


def short_circuit_example() -> None:
    """Show that any() stops at the first true item"""

    def loud(value: int) -> bool:
        """Report that a value was checked, then test it"""
        print("checking", value)
        return value > 10

    print(any(loud(n) for n in [5, 20, 30]))
    print()


def main() -> None:
    """Run each any() and all() example"""
    any_example()
    all_example()
    empty_collection_example()
    short_circuit_example()


if __name__ == "__main__":
    main()
