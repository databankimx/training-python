"""Implements the shell sort algorithm"""

import sys
from math import log2, ceil
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

@timer
def shell_sort(array: list[int]) -> tuple[list[int], int]:
    """Sort a list using the shell sort algorithm"""
    count = 0

    n = len(array)
    k = int(ceil(log2(n)))
    while True:
        interval = 2 ** k - 1
        if interval <= 0:
            break
        for i in range(interval, n):
            count += 1
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1

    return (array, count)

def main() -> None:
    """Test the shell sort"""
    numbers = file_to_list(input_file_name, folder)
    result = shell_sort(numbers)
    if not is_sorted(result[0]):
        print("Failed to sort array!")
        sys.exit()
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Shell Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
