"""Lambdas"""

def identity(x: any) -> any:
    """The identity function simply returns its argument"""
    return x

def plus_one(x: int) -> int:
    """Add one to the argument"""
    return x + 1

def main() -> None:
    """Main function"""
    n = 42

    print(f"identity(n) returns: {identity(n)}")
    # pylint: disable=unnecessary-direct-lambda-call
    print(f"(lambda x: x)(n) returns: {(lambda x: x)(n)}")

    print(f"plus_one(n) returns: {plus_one(n)}")
    print(f"(lambda x: x + 1)(n) returns: {(lambda x: x + 1)(n)}")

    # pylint: disable=unnecessary-lambda-assignment
    plus_two = lambda x: x + 2
    print(f"plus_two(n) = (lambda x: x + 2)(n), returns: {plus_two(n)}")

    a = 21
    b = a

    sum_args = lambda x, y: x + y
    print(f"sum_args(a, b) returns: {sum_args(a, b)}")
    print(f"(lambda x, y: x + y)(a, b) returns: {(lambda x, y: x + y)(a, b)}")

if __name__ == "__main__":
    main()
