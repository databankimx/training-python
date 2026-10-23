"""Keeping a decorated function's metadata with wraps()"""

from functools import wraps


def logged(func):
    """Print a message before calling the decorated function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Log the call, then run the original function"""
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logged
def greet(name: str) -> str:
    """Return a greeting for the given name"""
    return f"Hello, {name}"


def wraps_example() -> None:
    """Call a decorated function and check its name and docstring"""
    print(greet("Ana"))
    print(greet.__name__)
    print(greet.__doc__)
    print()


def main() -> None:
    """Run the wraps example"""
    wraps_example()


if __name__ == "__main__":
    main()
