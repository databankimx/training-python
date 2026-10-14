"""Filtering Arrays"""

import numpy as np
from sieve import sieve

def boolean_index_list() -> None:
    """Filter an array using a boolean index list"""
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"Array: {arr}")
    arr_filter = sieve(len(arr) - 1)
    print(f"Filter: {arr_filter}")
    print(f"Filtered array: {arr[arr_filter]}\n")

def loop_filter() -> None:
    """Filter an array using a loop"""
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"Array: {arr}")
    filter_arr = []
    for element in arr:
        filter_arr.append(element % 2 == 0)
    print(f"Filter: {filter_arr}")
    print(f"Filtered array: {arr[filter_arr]}\n")

def condition_filter() -> None:
    """Filter an array using a condition"""
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"Array: {arr}")
    filter_arr = arr % 2 == 1
    print(f"Filter: {filter_arr}")
    print(f"Filtered array: {arr[filter_arr]}\n")

def main() -> None:
    """Main Function"""
    boolean_index_list()
    loop_filter()
    condition_filter()

if __name__ == "__main__":
    main()
