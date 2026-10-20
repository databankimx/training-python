"""Joining Arrays"""

import numpy as np

def join_1d() -> None:
    """Join two 1D arrays into a single 1D array"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Array 1: {arr1}\nArray 2: {arr2}")
    arr = np.concatenate((arr1, arr2))
    print(f"Joined 1D Array: {arr}\n")

def join_2d_cols() -> None:
    """Join two 2D arrays into a single 2D array by column"""
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
    arr = np.concatenate((arr1, arr2))
    print(f"Joined 2D Array (by column):\n{arr}\n")

def join_2d_rows() -> None:
    """Join two 2D arrays into a single 2D array by row"""
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
    arr = np.concatenate((arr1, arr2), axis=1)
    print(f"Joined 2D Array (by row):\n{arr}\n")

def stack_2d() -> None:
    """Stack two 1D arrays into a single 2D array"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Array 1: {arr1}\nArray 2: {arr2}")
    arr = np.stack((arr1, arr2))
    print(f"Stacked 2D Array (by row):\n{arr}\n")

def stack_2d_rows() -> None:
    """Stack two 1D arrays into a single 2D array"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Array 1: {arr1}\nArray 2: {arr2}")
    arr = np.stack((arr1, arr2), axis=1)
    print(f"Stacked 2D Array (by column):\n{arr}\n")

def hstack_1d() -> None:
    """Stack two 1D arrays into a single 1D array"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Array 1: {arr1}\nArray 2: {arr2}")
    arr = np.hstack((arr1, arr2))
    print(f"Horizontally Stacked 1D Array:\n{arr}\n")

def hstack_2d() -> None:
    """Stack two 1D arrays into a single 2D array"""
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
    arr = np.hstack((arr1, arr2))
    print(f"Horizontally Stacked 2D Array:\n{arr}\n")

def vstack_1d() -> None:
    """Stack two 1D arrays into a single 2D array"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Array 1: {arr1}\nArray 2: {arr2}")
    arr = np.vstack((arr1, arr2))
    print(f"Vertically Stacked 2D Array:\n{arr}\n")

def vstack_2d() -> None:
    """Stack two 2D arrays into a single 2D array"""
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
    arr = np.vstack((arr1, arr2))
    print(f"Vertically Stacked 2D Array:\n{arr}\n")

def dstack_1d() -> None:
    """Stack two 1D arrays into a single 3D array"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"Array 1: {arr1}\nArray 2: {arr2}")
    arr = np.dstack((arr1, arr2))
    print(f"Depth Stacked 3D Array:\n{arr}\n")

def dstack_2d() -> None:
    """Stack two 2D arrays into a single 3D array"""
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f"Array 1:\n{arr1}\nArray 2:\n{arr2}")
    arr = np.dstack((arr1, arr2))
    print(f"Depth Stacked 3D Array:\n{arr}\n")

def main() -> None:
    """Main function"""
    join_1d()
    join_2d_cols()
    join_2d_rows()
    stack_2d()
    stack_2d_rows()
    hstack_1d()
    hstack_2d()
    vstack_1d()
    vstack_2d()
    dstack_1d()
    dstack_2d()

if __name__ == "__main__":
    main()
