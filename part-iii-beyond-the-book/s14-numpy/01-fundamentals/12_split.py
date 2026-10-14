"""Splitting Arrays"""

import numpy as np

def print_2d(arr: list[np.ndarray]) -> None:
    """Print out 2D split results"""
    print("Split array:\n[")
    for ar in arr:
        print(f" array({','.join(str(ar).splitlines())})")
    print("]\n")

def split_1d_to_3() -> None:
    """Split a 1D array into three parts"""
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"Original array:\n{arr}")
    new_arr = np.array_split(arr, 3)
    print(f"Split array:\n{new_arr}\n")

def split_1d_to_4() -> None:
    """Split a 1D array into four parts"""
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"Original array:\n{arr}")
    new_arr = np.array_split(arr, 4)
    print(f"Split array:\n{new_arr}\n")

def split_1d_to_missing() -> None:
    """Split a 1D array into three parts"""
    arr = np.array([1, 2, 3, 4])
    print(f"Original array:\n{arr}")
    new_arr = np.array_split(arr, 5)
    print(f"Split array:\n{new_arr}\n")

def split_2d_to_3() -> None:
    """Split a 2D array into three parts"""
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    print(f"Original array:\n{arr}")
    new_arr = np.array_split(arr, 3)
    print_2d(new_arr)

def split_2d_to_3_by_row() -> None:
    """Split a 2D array into three parts by row"""
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    print(f"Original array:\n{arr}")
    new_arr = np.array_split(arr, 3, axis=1)
    print_2d(new_arr)

def hsplit_2d_to_3() -> None:
    """Split a 2D array into three parts horizontally"""
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    print(f"Original array:\n{arr}")
    new_arr = np.hsplit(arr, 3)
    print_2d(new_arr)

def vsplit_2d_to_3() -> None:
    """Split a 2D array into three parts vertically"""
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    print(f"Original array:\n{arr}")
    new_arr = np.vsplit(arr, 3)
    print_2d(new_arr)

def main() -> None:
    """Main function"""
    split_1d_to_3()
    split_1d_to_4()
    split_1d_to_missing()
    split_2d_to_3()
    split_2d_to_3_by_row()
    hsplit_2d_to_3()
    vsplit_2d_to_3()

if __name__ == "__main__":
    main()
