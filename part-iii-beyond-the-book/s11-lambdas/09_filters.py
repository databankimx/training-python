"""Using lambdas to filter and sort lists"""

def sort_list() -> None:
    """Use a lambda to sort the list by a preferred ordering"""
    ids = ["id1", "id2", "id30", "id3", "id22", "id100"]
    print(sorted(ids))
    print(sorted(ids, key=lambda x: int(x[2:])), "\n")

def map_format() -> None:
    """Use a lambda to modify a map"""
    tup = ("cat", "dog", "turtle")
    print(list(map(lambda x: x.capitalize(), tup)))
    print([x.capitalize() for x in tup])
    print()

def list_filter() -> None:
    """Use a lambda to filter a list"""
    print(list(range(2, 11, 2)))
    print([x for x in range(1, 11) if not x % 2])
    # pylint: disable=unnecessary-lambda-assignment
    even = lambda x: not x % 2
    print(list(filter(even, range(1, 11))))
    print()

def main() -> None:
    """Main function"""
    sort_list()
    map_format()
    list_filter()

if __name__ == "__main__":
    main()
