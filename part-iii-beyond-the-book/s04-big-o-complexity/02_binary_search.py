"""Implements the binary search algorithm"""

import sys
from random import randint
from sm_utils import timer
from common_functions import file_to_list, efficiency_report

# Pseudocode Algorithm:
# ----------------------------------------------------------------------
# Assume an already ordered array
#
# Loop until done
#     If the element at the middle of the list contains the target value
#         Quit and return the index of the middle element
#     Else
#         If the middle element's value is less than the target value
#             Remove the lower half of the current array
#             Move to the next iteration of the loop
#         Else
#             Remove the upper half of the current array
#             Move to the next iteration of the loop
# If target element not found by end of loop
#     Quit (Return failure state)
# ----------------------------------------------------------------------

folder = "data"
file_name = "ordered_integers.txt"

def binary_search(array: list[int], target: int, low: int=-1,
                  high: int=-1, count: int=0) -> tuple[int, int]:
    """Find the index where the target value is stored"""
    if low == -1:
        low = 0
    if high == -1:
        high = len(array) - 1
    count += 1

    if high >= low:
        mid = (high + low) // 2
        if array[mid] == target:
            return (mid, count)
        if array[mid] < target:
            return binary_search(array, target, mid + 1, high, count)
        return binary_search(array, target, low, mid - 1, count)

    return (-1, count)

@timer
def search_runner(array: list[int], target: int) -> tuple[int, int]:
    """Wraps timer around recursive series"""
    return binary_search(array, target)

def main() -> None:
    """Test the binary search"""
    numbers = file_to_list(file_name, folder)
    seek = randint(min(numbers), max(numbers))
    result = search_runner(numbers, seek)
    if result[0] < 0:
        print(f"\nDid not find value: {seek}")
        sys.exit()
    print(f"\nIndex of target [{seek}]: i = [{result[0]}]")
    efficiency_report("Binary Search", len(numbers), result[1])

if __name__ == "__main__":
    main()
