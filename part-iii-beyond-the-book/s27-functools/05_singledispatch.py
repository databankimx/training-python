"""Dispatching by argument type with singledispatch()"""

from functools import singledispatch


@singledispatch
def describe(_value: object) -> str:
    """Describe any value that has no specific handler"""
    return "something"


@describe.register(int)
def _(_value: int) -> str:
    """Describe an integer"""
    return "an integer"


@describe.register(list)
def _(value: list) -> str:
    """Describe a list by its length"""
    return f"a list of {len(value)} items"


def dispatch_example() -> None:
    """Call describe() with values of different types"""
    print(describe(3))
    print(describe([1, 2]))
    print(describe("hi"))
    print()


def main() -> None:
    """Run the singledispatch example"""
    dispatch_example()


if __name__ == "__main__":
    main()
