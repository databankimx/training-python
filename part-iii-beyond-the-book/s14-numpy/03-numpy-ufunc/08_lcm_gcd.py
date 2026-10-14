"""Greatest Common Divisor and Least Common Multiple"""

import numpy as np
from utility_functions import timer

def my_gcd(x: int, y: int) -> int:
    """Calculate GCD for two integers"""
    return x if y == 0 else my_gcd(y, x % y)

def my_lcm(x: int, y: int) -> int:
    """Calculate LCM for two integers"""
    return x * y // my_gcd(x, y)

def my_list_gcd(lst: list[int]) -> int:
    """Calculate GCD for multiple integers"""
    lst = list(set(lst))
    gcf = lst[0]
    for n in lst[1:]:
        gcf = my_gcd(gcf, n)
    return gcf

def my_list_lcm(lst: list[int]) -> int:
    """Calculate LCM for multiple integers"""
    lst = list(set(lst))
    lcm = 1
    for n in lst:
        lcm = my_lcm(lcm, n)
    return lcm

@timer
def test_my_gcd(lst: list[int]) -> int:
    """Timed test of my_list_gcd()"""
    return my_list_gcd(lst)

@timer
def test_my_lcm(lst: list[int]) -> int:
    """Timed test of my_list_lcm()"""
    return my_list_lcm(lst)

@timer
def test_np_gcd(arr: np.ndarray) -> int:
    """Timed test of np.gcd.reduce()"""
    return np.gcd.reduce(arr)

@timer
def test_np_lcm(arr: np.ndarray) -> int:
    """Timed test of np.lcm.reduce()"""
    return np.lcm.reduce(arr)

def main() -> None:
    """Main Function"""
    lst = [12, 15, 27, 30]
    arr = np.array(lst)

    print(f"My GCD of the list {lst}: {test_my_gcd(lst)}\n")
    print(f"NumPy GCD of the array {arr}: {test_np_gcd(arr)}\n")

    print(f"My LCM of the list {lst}: {test_my_lcm(lst)}\n")
    print(f"NumPy LCM of the array {arr}: {test_np_lcm(arr)}\n")

if __name__ == "__main__":
    main()
