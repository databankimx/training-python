"""Iterating over an Array with a Loop"""

import numpy as np

def iter_one_d() -> None:
    """Iterating over a one-dimensional array"""
    arr = np.array([1, 2, 3])
    print(f"1D Array:\n{arr}\nLooping...")
    for el in arr:
        print(el)
    print()

def iter_two_d() -> None:
    """Iterating over a two-dimensional array"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr}\nLooping...")
    for el in arr:
        print(el)
    print()

def iter_two_d_elem() -> None:
    """Iterating over all two-dimensional array elements"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr}\nLooping rows...")
    for row in arr:
        print(" Looping elements in row...")
        for el in row:
            print(f"  {el}")
    print()

def iter_three_d_elem() -> None:
    """Iterating over all three-dimensional array elements"""
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(f"3D Array:\n{arr}\nLooping pages...")
    for page in arr:
        print(" Looping rows in page...")
        for row in page:
            print("  Looping elements in row...")
            for el in row:
                print(f"   {el}")

def main():
    """Main Function"""
    iter_one_d()
    iter_two_d()
    iter_two_d_elem()
    iter_three_d_elem()

if __name__ == "__main__":
    main()
