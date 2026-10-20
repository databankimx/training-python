"""Indexing in NumPy Arrays"""

import numpy as np

def unidimensional():
    """Indexing a one-dimensional array"""
    arr = np.array([1, 2, 3, 4])
    print("1-D:")
    print(arr, "\n")
    print("arr[0] =", arr[0])
    print("arr[1] =", arr[1])
    print("arr[2] + arr[3] =", arr[2] + arr[3], "\n")

def matrix() -> None:
    """Indexing a two-dimensional array"""
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("2-D:")
    print(arr, "\n")

    print("2nd element on 1st row: arr[0][1] =", arr[0][1])
    print("5th element on 2nd row: arr[1][4] =", arr[1][4])

    print("2nd element on 1st row: arr[0, 1] =", arr[0, 1])
    print("5th element on 2nd row: arr[1, 4] =", arr[1, 4], "\n")

def tensor() -> None:
    """Indexing a three-dimensional array"""
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("3-D:")
    print(arr, "\n")

    print("arr[0][1][2] =", arr[0][1][2])
    print("arr[0, 1, 2] =", arr[0, 1, 2], "\n")

    print("arr[1][1] =", arr[1][1])
    print("arr[1, 1] =", arr[1, 1], "\n")

    print("arr[-1][-1] =", arr[-1][-1])
    print("arr[-1, -1] =", arr[-1, -1], "\n")

def main() -> None:
    """Main Function"""
    unidimensional()
    matrix()
    tensor()

if __name__ == "__main__":
    main()
