"""Implements the selection sort algorithm"""

import sys
from common_functions import file_to_list, efficiency_report, list_to_file, is_sorted
from sm_utils import timer

# Pseudocode Algorithm:
# --------------------------------------------------------------
# For i from 0 to n-1
#     Find the smallest element between array[i] and array[n-1].
#     Swap the smallest element with array[i]
# --------------------------------------------------------------

folder = "data"
input_file_name = "unordered_integers.txt"
output_file_name = "sorted_integers.txt"

@timer
def selection_sort(array: list[int]) -> tuple[list[int], int]:
    """Sort a list using the selection sort algorithm"""
    count = 0

    n = len(array)
    i = 0

    while i < n - 1:
        count += 1
        pos = i
        for j in range(i + 1, n):
            count += 1
            if array[j] < array[pos]:
                pos = j
        if pos != i:
            array[i], array[pos] = array[pos], array[i]
        i += 1

    return (array, count)

def main() -> None:
    """Test the selection sort"""
    numbers = file_to_list(input_file_name, folder)
    result = selection_sort(numbers)
    if not is_sorted(result[0]):
        print("Failed to sort array!")
        sys.exit()
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Selection Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
