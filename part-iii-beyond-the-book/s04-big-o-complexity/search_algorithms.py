"""Search algorithms"""

def linear_search(array: list[int], target: int) -> int:
    """Find the index where the target value is stored"""
    for i, elem in enumerate(array):
        if elem == target:
            return i
    return -1

def binary_search(array: list[int], target: int, low: int=-1, high: int=-1) -> int:
    """Find the index where the target value is stored"""
    if low == -1:
        low = 0
    if high == -1:
        high = len(array) - 1

    if high >= low:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            return binary_search(array, target, mid + 1, high)
        return binary_search(array, target, low, mid - 1)

    return -1
