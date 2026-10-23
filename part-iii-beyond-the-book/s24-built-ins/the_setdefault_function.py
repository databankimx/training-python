"""The setdefault function"""

from pprint import pprint


def add_missing_key_example() -> None:
    """Add a key with setdefault() when the key is missing"""
    my_dict = {"name": "fido", "age": 3}
    print(my_dict)

    # This will add the default value like my_dict["animal"] = dog
    my_dict.setdefault("animal", "dog")
    print(my_dict)
    print()


def keep_existing_value_example() -> None:
    """Show that setdefault() leaves an existing key unchanged"""
    my_dict = {"name": "fido", "age": 3}
    my_dict.setdefault("animal", "dog")

    # But, while my_dict["animal"] = cat would overwrite the value for key = animal, this will not
    my_dict.setdefault("animal", "cat")
    print(my_dict)
    print()


def pprint_example() -> None:
    """Pretty-print a dictionary with one key per line"""
    my_dict = {"name": "fido", "age": 3, "animal": "dog"}

    # While we're here, let's demonstrate pretty-print
    pprint(my_dict, width=1)
    print()


def main() -> None:
    """Run each setdefault() example"""
    add_missing_key_example()
    keep_existing_value_example()
    pprint_example()


if __name__ == "__main__":
    main()
