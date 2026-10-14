"""Sort arrays"""

import numpy as np

def sort_1d_int() -> None:
    """Sort a 1D array of integers in ascending order"""
    arr = np.array([3, 1, 2, 5, 4])
    print("Original array:", arr)
    sorted_arr = np.sort(arr)
    print("Sorted array:  ", sorted_arr, "\n")

def sort_1d_str() -> None:
    """Sort a 1D array of strings in ascending order"""
    arr = np.array(["banana", "cherry", "apple"])
    print("Original array:", arr)
    sorted_arr = np.sort(arr)
    print("Sorted array:  ", sorted_arr, "\n")

def sort_2d_int() -> None:
    """Sort a 2D array of integers in ascending order"""
    arr = np.array([[3, 2, 4], [5, 0, 1]])
    print("Original array:\n", arr)
    sorted_arr = np.sort(arr)
    print("Sorted array:\n", sorted_arr, "\n")

def main() -> None:
    """Main Function"""
    sort_1d_int()
    sort_1d_str()
    sort_2d_int()

if __name__ == "__main__":
    main()
