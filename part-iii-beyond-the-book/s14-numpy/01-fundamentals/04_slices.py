"""Slicing Arrays"""

import numpy as np

def simple() -> None:
    """Simple slices with arrays"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print("Simple Slices:")
    print(arr)
    print("1 to 5", arr[1:5])
    print("4 to end", arr[4:])
    print("start to 4", arr[:4], "\n")

def negative() -> None:
    """Negative-index slices with arrays"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print("Negative-index Slices:")
    print(arr)
    print("-3 to -1", arr[-3:-1], "\n")

def copy() -> None:
    """Slice copies with arrays"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print("Slice copies:")
    print(arr)
    print("copy", arr[::], "\n")

def stepped() -> None:
    """Stepped slices with arrays"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print("Stepped slices:")
    print(arr)
    print("1 to 5 - every other", arr[1:5:2])
    print("copy - every other", arr[::2], "\n")

def multidimensional() -> None:
    """Slices with multidimensional arrays"""
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("2-D slices:")
    print(arr)
    print("indices 1 to 3 from first array", arr[1, 1:4])
    print("index 2 from first two arrays", arr[0:2, 2])
    print("indices 1 to 3 from first two arrays")
    print(arr[0:2, 1:4], "\n")

def main() -> None:
    """Main Function"""
    simple()
    negative()
    copy()
    stepped()
    multidimensional()

if __name__ == "__main__":
    main()
