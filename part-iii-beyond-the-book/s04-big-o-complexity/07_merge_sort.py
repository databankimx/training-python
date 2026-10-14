"""Implements the merge sort algorithm"""

import sys
from common_functions import file_to_list, efficiency_report, list_to_file, is_sorted
from sm_utils import timer

# pylint: disable=fixme

# Pseudocode Algorithm:
# --------------------------------------------------------------
# O(n log n)
# TODO: Describe algorithm
# --------------------------------------------------------------

folder = "data"
input_file_name = "unordered_integers.txt"
output_file_name = "sorted_integers.txt"

def merge_sort(array: list[int], count: int=0) -> tuple[list[int], int]:
    """Sort a list using the merge sort algorithm"""
    if len(array) == 1:
        return (array, count)
    mid = (len(array) - 1) // 2

    array_1, count = merge_sort(array[:mid + 1], count)
    array_2, count = merge_sort(array[mid + 1:], count)

    result, count = merge(array_1, array_2, count)

    return (result, count)

def merge(array_1: list[int], array_2: list[int], count: int) -> tuple[list[int], int]:
    """Merge two lists used in merge sort"""
    merged = []
    i = 0
    j = 0
    while(i <= len(array_1) - 1 and j <= len(array_2) - 1):
        count += 1
        if array_1[i] < array_2[j]:
            merged.append(array_1[i])
            i += 1
        else:
            merged.append(array_2[j])
            j += 1
    if i > len(array_1)-1:
        while j <= len(array_2) - 1:
            count += 1
            merged.append(array_2[j])
            j += 1
    else:
        while i <= len(array_1) - 1:
            count += 1
            merged.append(array_1[i])
            i += 1
    return (merged, count)

@timer
def sort_runner(array: list[int]) -> tuple[int, int]:
    """Wraps timer around recursive series"""
    return merge_sort(array)

def main() -> None:
    """Test the merge sort"""
    numbers = file_to_list(input_file_name, folder)
    result = sort_runner(numbers)
    if not is_sorted(result[0]):
        print("Failed to sort array!")
        sys.exit()
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Merge Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
