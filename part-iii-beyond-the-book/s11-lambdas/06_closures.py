"""Lambdas as Closures"""

def outer_func_function(x: int) -> callable:
    """Outer function"""
    y = 4
    def inner_func(z: int) -> int:
        """Inner function"""
        return x + y + z
    return inner_func

def outer_func_lambda(x: int) -> callable:
    """Outer function with lambda"""
    y = 4
    return lambda z: x + y + z

def main() -> None:
    """Main function"""
    for i in range(3):
        closure = outer_func_function(i)
        print(f"closure({i + 5}) = {closure(i + 5)}")

    print()

    for i in range(3):
        closure = outer_func_lambda(i)
        print(f"closure({i + 5}) = {closure(i + 5)}")

if __name__ == "__main__":
    main()
