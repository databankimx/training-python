"""Implements the selection sort algorithm"""

import sys
from common_functions import file_to_list, efficiency_report, list_to_file, is_sorted
from sm_utils import timer

# Pseudocode Algorithm:
# ------------------------------------------------------------------
# For element indices `i` 1 to n-1
#     Select element `j` = i+1
#     Compare current element with each element j-1 to 0
#         Swap it with the lowest index element whose value is
#           greater than the current element
#         Re-index remaining compared elements
#     Increment i and repeat
# ------------------------------------------------------------------

folder = "data"
input_file_name = "unordered_integers.txt"
output_file_name = "sorted_integers.txt"

@timer
def insertion_sort(array: list[int]) -> tuple[list[int], int]:
    """Sort a list using the insertion sort algorithm"""
    count = 0

    for i in range(1, len(array)):
        count += 1
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            count += 1
            array[j + 1] = array[j]
            j -= 1

        count += 1
        array[j + 1] = key

    return (array, count)

def main() -> None:
    """Runs the insertion sort algorithm"""
    numbers = file_to_list(input_file_name, folder)
    result = insertion_sort(numbers)
    if not is_sorted(result[0]):
        print("Failed to sort array!")
        sys.exit()
    list_to_file(result[0], output_file_name, folder)
    efficiency_report("Insertion Sort", len(numbers), result[1])
    print(f"Check file: ./{folder}/{output_file_name} to validate results")

if __name__ == "__main__":
    main()
