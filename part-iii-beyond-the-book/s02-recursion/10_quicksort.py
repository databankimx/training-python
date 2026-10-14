"""Implementation of the Quicksort algorithm"""

from statistics import median
from random import randint

def quicksort(numbers: list[int]) -> list[int]:
    """Sort a list of numbers using the Quicksort algorithm (recursive)"""
    # Base case: 0- or 1-length lists are sorted
    if len(numbers) <= 1:
        return numbers

    # Get the pivot using the median of the first, last and middle numbers
    pivot = median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])

    # Populate sub-lists
    items_less = [n for n in numbers if n < pivot]
    pivot_items = [n for n in numbers if n == pivot]
    items_greater = [n for n in numbers if n > pivot]

    # Recursively reduce until the entire list is sorted
    return quicksort(items_less) + pivot_items + quicksort(items_greater)

def generate_random_list(length: int=10, minimum: int=-100, maximum: int=100):
    """Generate a random, unsorted list of integers to sort"""
    return [randint(minimum, maximum) for _ in range(length)]

def main() -> None:
    """Main program"""
    lists = [
        # Base cases
        [],
        [42],
        # Recursive cases
        [5, 2, 3, 6],
        [10, -3, 21, 6, -8],
        # Random recursive case
        generate_random_list()
    ]
    print()
    for item in lists:
        print(f"{item} sorts to {quicksort(item)}")
    print()

if __name__ == "__main__":
    nums = [randint(-100, 100) for _ in range(10)]
    print(f"Unsorted: {nums}")
    print(f"Sorted: {quicksort(nums)}")
    # main()
