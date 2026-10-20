"""Views and Copies in NumPy"""

import numpy as np

def make_copy() -> None:
    """Demonstrate making a copy and changing the original array"""
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    arr[0] = 42
    print("Create copy and change original:")
    print("array:", arr)
    print("copy:", x, "\n")

def view_change_original() -> None:
    """Demonstrate making a view and changing the original array"""
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    arr[0] = 42
    print("Create view and change original:")
    print("array:", arr)
    print("view:", x, "\n")

def view_change_view() -> None:
    """Demonstrate making a view and changing the view"""
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    x[0] = 31
    print("Create view and change view:")
    print("array:", arr)
    print("view:", x, "\n")

def base() -> None:
    """Demonstrate the base property of arrays"""
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    y = arr.view()
    print("Copy versus view `base` property:")
    print("array base =", arr.base)
    print("copy base =", x.base)
    print("view base =", y.base, "\n")

def main() -> None:
    """Main function"""
    make_copy()
    view_change_original()
    view_change_view()
    base()

if __name__ == "__main__":
    main()
