"""Lambda Parameters and Arguments"""

from utility_functions import clear_terminal, pause

def positional() -> None:
    """Illustrate positional arguments in a lambda"""
    print("Positional arguments:")
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda x, y, z: x + y + z)(1, 2, 3), "\n")

def positional_default() -> None:
    """Illustrate positional arguments (with default) in a lambda"""
    print("Positional arguments: (with default)")
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda x, y, z=3: x + y + z)(1, 2), "\n")

def positional_keyword() -> None:
    """Illustrate positional and keyword arguments in a lambda"""
    print("Positional and keyword arguments:")
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda x, y, z: x + y + z)(1, 2, z=3), "\n")

def positional_arbitrary() -> None:
    """Illustrate arbitrary positional arguments in a lambda"""
    print("Arbitrary positional arguments:")
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda *args: sum(args))(1, 2, 3), "\n")

def keyword_arbitrary() -> None:
    """Illustrate arbitrary keyword arguments in a lambda"""
    print("Arbitrary keyword arguments:")
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3), "\n")

def keyword_only() -> None:
    """Illustrate arbitrary keyword arguments in a lambda"""
    print("Keyword-only arguments:")
    # pylint: disable=unnecessary-direct-lambda-call
    print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3), "\n")

def main() -> None:
    """Main function"""
    clear_terminal()
    positional()
    pause()

    clear_terminal()
    positional_default()
    pause()

    clear_terminal()
    positional_keyword()
    pause()

    clear_terminal()
    positional_arbitrary()
    pause()

    clear_terminal()
    keyword_arbitrary()
    pause()

    clear_terminal()
    keyword_only()
    pause(True)

if __name__ == "__main__":
    main()
