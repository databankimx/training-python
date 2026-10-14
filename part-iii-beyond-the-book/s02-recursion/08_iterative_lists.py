"""Traversing a nested list without recursion"""

def count_leaves(items: list[str | list]) -> int:
    """Iteratively count the number of leaves in a (possibly) nested list"""
    count = 0
    stack = []
    current_list = items
    i = 0
    while True:
        if i == len(current_list):
            if current_list == items:
                return count
            current_list, i = stack.pop()
            i += 1
            continue
        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1

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
    num = count_leaves(names)
    print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")

if __name__ == "__main__":
    main()
