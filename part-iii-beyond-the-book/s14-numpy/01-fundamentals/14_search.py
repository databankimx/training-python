"""Searching Arrays"""

import numpy as np

def indices_1d_by_loop() -> None:
    """Loop through an array and find all indices of a value"""
    arr = np.array([1, 2, 3, 4, 6, 5, 4, 4])
    print(f"Array: {arr}")
    indices = []
    n = 4
    print(f"Search Value: {n}")
    indices = np.array([i for i in range(len(arr)) if arr[i] == n])
    print(f"Found {n} at indices:", np.array(indices), "\n")

def indices_1d_by_value() -> None:
    """Get the index of a value in a 1D array"""
    arr = np.array([1, 2, 3, 4, 6, 5, 4, 4])
    print(f"Array: {arr}")
    n = 4
    print(f"Search Value: {n}")
    indices = np.where(arr == n)
    print(f"Found {n} at indices:", indices, "\n")

# pylint: disable=fixme
# TODO: Research how to use np.where() for 2D arrays
#       This does not work as expected
# def indices_2d_by_value() -> None:
#     """Get the index of a value in a 2D array"""
#     arr = np.array([[1, 2, 3, 4], [6, 5, 4, 4]])
#     print(f"Array: {arr}")
#     n = 4
#     indices = np.where(arr == n)
#     print(f"Found {n} at indices:", indices, "\n")

def indices_1d_by_formula() -> None:
    """Get the index of a calculated value in a 1D array"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Array: {arr}")
    odds = np.where(arr % 2 == 1)
    evens = np.where(arr % 2 == 0)
    print(f"Found Odd values at indices: {odds}")
    print(f"Found Even values at indices: {evens}\n")

def is_sorted(arr: np.ndarray) -> bool:
    """Check if an array is sorted in ascending order"""
    return np.all(np.diff(arr) >= 0)
    # return lambda arr: np.all(arr[:-1] <= arr[1:])

def search_sorted() -> None:
    """Get the index of a value in a sorted 1D array"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 7, 8])
    print(f"Array: {arr}")
    if not is_sorted(arr):
        arr = np.sort(arr)
    n = 7
    print(f"Search Value: {n}")
    l = np.searchsorted(arr, n)
    r = np.searchsorted(arr, n, side="right")
    print(f"Can insert {n} from index {l} to {r}\n")

def search_sorted_multiple() -> None:
    """Get the indices of multiple values in a sorted 1D array"""
    arr = np.array([1, 2, 2, 3, 4, 4, 4, 6])
    print(f"Array: {arr}")
    if not is_sorted(arr):
        arr = np.sort(arr)
    vals = [2, 4, 5]
    print(f"Search Values: {np.array(vals)}")
    l = np.searchsorted(arr, vals)
    r = np.searchsorted(arr, vals, side="right")
    for i, left in enumerate(l):
        if left == r[i]:
            print(f"Can insert {vals[i]} at index {l[i]}")
            continue
        print(f"Can insert {vals[i]} from index {l[i]} to {r[i]}")
    print()

def main() -> None:
    """Main Function"""
    indices_1d_by_loop()
    indices_1d_by_value()
    indices_1d_by_formula()
    search_sorted()
    search_sorted_multiple()

if __name__ == "__main__":
    main()
