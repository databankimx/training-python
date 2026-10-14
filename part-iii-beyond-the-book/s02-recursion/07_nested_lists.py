"""Iterating over nested lists"""

def count_leaves(items: list[str | list]) -> int:
    """Recursively count the number of leaves in a (possibly) nested list"""
    print(f"Counting list: {items}")
    count = 0
    for item in items:
        if isinstance(item, list):
            count += count_leaves(item)
        else:
            print(f"Found leaf: {item}")
            count += 1
    return count

def main() -> None:
    """Main function to demonstrate the count_leaves function"""
    names = [
        "Adam",
        [
            "Bob",
            [
                "Chet",
                "Cat"
            ],
            "Barb",
            "Bert"
        ],
        "Alex",
        [
            "Bea",
            "Bill"
        ],
        "Ann"
    ]

    num = len(names)
    print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")
    for index, name in enumerate(names):
        print(index, name)

    print()

    num = count_leaves(names)
    print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")

if __name__ == "__main__":
    main()
