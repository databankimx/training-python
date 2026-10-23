"""The id function"""


def string_identity_example() -> None:
    """Show that identical string constants can share an address"""
    # Here I am stashing a string in memory
    loc_1 = id("Hello World")
    print(loc_1)

    # Here, we put the same string into a variable
    # Because Python uses a table of all stored string values to minimize
    # memory use, this is at the same address
    my_string = "Hello World"
    loc_2 = id(my_string)
    print(loc_2)
    print()


def changed_value_example() -> None:
    """Show that changing a string's value gives it a new address"""
    my_string = "Hello World"
    loc_2 = id(my_string)
    print(loc_2)

    # When we change the value, however, even though it's the same variable,
    # the string is at a new address
    my_string = "Hello World!"
    loc_3 = id(my_string)
    print(loc_3)
    print()


def main() -> None:
    """Run each id() example"""
    string_identity_example()
    changed_value_example()


if __name__ == "__main__":
    main()
