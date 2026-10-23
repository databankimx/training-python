"""The copy module: shallow copies and deep copies"""

from copy import copy, deepcopy


def shallow_copy_example() -> None:
    """Show that copy() makes a new outer list but shares nested lists"""
    original = [1, 2, [3, 4]]

    # copy() makes a new outer list, but the nested list is still shared
    shallow = copy(original)
    print(f"Equal values: {shallow == original}")
    print(f"Same list object: {shallow is original}")

    # Change the nested list in the original
    original[2].append(5)
    print(f"Original: {original}")
    print(f"Shallow:  {shallow}   (the nested list changed too)")
    print()


def deep_copy_example() -> None:
    """Show that deepcopy() copies nested lists as well"""
    original = [1, 2, [3, 4]]

    # deepcopy() also copies the nested list
    deep = deepcopy(original)

    # Change the nested list in the original
    original[2].append(5)
    print(f"Original: {original}")
    print(f"Deep:     {deep}      (unaffected)")
    print()


def main() -> None:
    """Run the shallow and deep copy examples"""
    shallow_copy_example()
    deep_copy_example()


if __name__ == "__main__":
    main()
