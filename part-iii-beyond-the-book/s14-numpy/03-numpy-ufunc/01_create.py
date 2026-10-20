"""Creating `ufunc` Functions"""

import numpy as np

def add_up(x: int|list[int], y: int|list[int]) -> int:
    """Add two integers or lists of integers"""
    return x + y

def check_type(f: callable) -> None:
    """Show the types of a function and a ufunc"""
    print(f"{f.__name__} type: {type(f).__name__}")

def add_trad() -> None:
    """Call the add_up function without making a ufunc"""
    print("Calling add_up without a ufunc:")
    check_type(add_up)
    x, y = 5, 3
    print(f"add_up({x}, {y}) yields: {add_up(x, y)}")
    lx, ly = [1, 2, 3], [4, 5, 6]
    print(f"add_up({lx}, {ly}) yields: {add_up(lx, ly)}\n")

def add_np() -> None:
    """Call the add_up function using a ufunc"""
    print("Calling add_up using a ufunc:")
    adder = np.frompyfunc(add_up, 2, 1)
    check_type(adder)
    x, y = 5, 3
    print(f"adder({x}, {y}) yields: {adder(x, y)}")
    lx, ly = [1, 2, 3], [4, 5, 6]
    print(f"adder({lx}, {ly}) yields: {adder(lx, ly)}\n")

def main() -> None:
    """Main function"""
    add_trad()
    add_np()

if __name__ == "__main__":
    main()
