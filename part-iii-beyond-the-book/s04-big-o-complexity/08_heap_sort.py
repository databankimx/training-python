"""Implements the heap sort algorithm"""

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

@timer
def heap_sort(array: list[int]) -> tuple[list[int], int]:
    """Sort a list using the heap sort algorithm"""
    count = 0

    n = len(array)
    for i in range(n // 2, -1, -1):
        count += 1
        count = make_heap(array, n, i, count)
    for i in range(n - 1, 0, -1):
        count += 1
        array[i], array[0] = array[0], array[i]
        count = make_heap(array, i, 0, count)

    return (array, count)

def make_heap(array: list[int], n: int, i: int, count: int) -> int:
    """Create the heap structure for heap sorting"""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        count += 1
        array[i], array[largest] = array[largest], array[i]
        count = make_heap(array, n, largest, count)

    return count

def main() -> None:
    """Test the heap sort algorithm"""
    numbers = file_to_list(input_file_name, folder)
    result = heap_sort(numbers)
    if not is_sorted(result[0]):
        print("Failed to sort array!")
        sys.exit()
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Heap Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
