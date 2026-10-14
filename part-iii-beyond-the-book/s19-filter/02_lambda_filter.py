"""Example using a lambda function as a filter"""

def main() -> None:
    """Main function"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    evens = list(filter(lambda n: not n % 2, numbers))
    print(f"Even numbers: {evens}")

    words = ["fig", "apple", "kiwi", "banana"]
    long_words = list(filter(lambda w: len(w) > 4, words))
    print(f"Words longer than 4 letters: {long_words}")

    truthy = list(filter(None, [0, 1, "", "a", None, 2]))
    print(f"Values that are true: {truthy}")

if __name__ == "__main__":
    main()
