"""Implements the quick sort algorithm"""

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

def quick_sort(array: list[int], count: int=0) -> tuple[list[int], int]:
    """Sort a list using the quick sort algorithm"""
    if len(array) > 1:
        pivot = array.pop()
        greater_array, equal_array, lesser_array = [], [pivot], []
        for element in array:
            count += 1
            if element == pivot:
                equal_array.append(element)
            elif element > pivot:
                greater_array.append(element)
            else:
                lesser_array.append(element)
        array, count = quick_sort(lesser_array, count)
        res = quick_sort(greater_array, count)
        array += equal_array + res[0]
        count = res[1]
    else:
        return (array, count)

    return (array, count)

@timer
def sort_runner(array: list[int]) -> tuple[int, int]:
    """Wraps timer around recursive series"""
    return quick_sort(array)

def main() -> None:
    """Run the quick_sort function"""
    numbers = file_to_list(input_file_name, folder)
    result = sort_runner(numbers[:])
    if not is_sorted(result[0]):
        print("Failed to sort array!")
        sys.exit()
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Quick Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
