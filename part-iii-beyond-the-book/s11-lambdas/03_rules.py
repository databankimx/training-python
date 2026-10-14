"""Lambda Rules"""

def main() -> None:
    """Main function"""
    # pylint: disable=unnecessary-lambda-assignment
    even_odd = lambda x: x % 2 and "odd" or "even"
    print(even_odd(2))
    print(even_odd(3), "\n")

if __name__ == "__main__":
    main()
