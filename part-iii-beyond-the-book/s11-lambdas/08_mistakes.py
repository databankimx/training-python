"""Common Lambda Mistakes"""

def throw(ex: Exception) -> None:
    """Raise an exception"""
    raise ex

def throw_from_lambda() -> None:
    """Raise an exception"""
    try:
        # pylint: disable=unnecessary-direct-lambda-call
        (lambda: throw(Exception("\nCaught an error!\n")))()
    # pylint: disable=broad-except
    except Exception as ex:
        print(ex)

def cryptic_lambda() -> None:
    """Execute a lambda that is hard to read"""
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda _: list(map(lambda _: _ // 2, _)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "\n")

def readable_function() -> None:
    """Execute the same code in a more readable format"""
    # pylint: disable=unnecessary-lambda-assignment
    div_by_two = lambda n: n // 2
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(div_by_two, lst)), "\n")

def main() -> None:
    """Main function"""
    throw_from_lambda()
    cryptic_lambda()
    readable_function()

if __name__ == "__main__":
    main()
