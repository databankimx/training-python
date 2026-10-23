"""Common Lambda Mistakes"""

# pylint: disable=line-too-long

def throw(ex: Exception) -> None:
    """Raise an exception"""
    raise ex

def throw_from_lambda() -> None:
    """Raise an exception"""
    try:
        # pylint: disable=unnecessary-direct-lambda-call
        (lambda: throw(Exception("Caught an error!")))()
    # pylint: disable=broad-except
    except Exception as ex:
        print(ex)

def cryptic_lambda() -> None:
    """Execute a lambda that is hard to read"""
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda _: list(map(lambda _: _ // 2, _)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "\n") #NOSONAR

def readable_function() -> None:
    """Execute the same code in a more readable format"""
    # pylint: disable=unnecessary-lambda-assignment
    div_by_two = lambda n: n // 2
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(div_by_two, lst)), "\n") #NOSONAR

def map_for_side_effects() -> None:
    """Misuse map() to run a side effect"""
    # pylint: disable=unnecessary-lambda
    print(list(map(lambda x: print(x), [1, 2, 3]))) #NOSONAR

def mutable_default() -> None:
    """Show how a mutable default in a lambda is shared between calls"""
    # pylint: disable=unnecessary-lambda-assignment
    add_to = lambda x, lst=[]: lst + [x] #NOSONAR
    print(add_to(1))
    print(add_to(2))

    # pylint: disable=unnecessary-lambda-assignment
    add_and_show = lambda x, lst=[]: (lst.append(x), lst)[1] #NOSONAR
    print(add_and_show(1))
    print(add_and_show(2))

def sort_key_mistake() -> None:
    """Forget to call the method in a sort key lambda"""
    words = ["banana", "Apple", "cherry"]
    try:
        print(sorted(words, key=lambda s: s.lower)) #NOSONAR
    except TypeError:
        print("TypeError raised")
    print(sorted(words, key=lambda s: s.lower())) #NOSONAR

def lambda_name() -> None:
    """Show that a lambda has no name of its own"""
    # pylint: disable=unnecessary-lambda-assignment
    f = lambda x: 1 / x #NOSONAR
    print(f.__name__)

def main() -> None:
    """Main function"""
    throw_from_lambda()
    cryptic_lambda()
    readable_function()
    map_for_side_effects()
    mutable_default()
    sort_key_mistake()
    lambda_name()

if __name__ == "__main__":
    main()
