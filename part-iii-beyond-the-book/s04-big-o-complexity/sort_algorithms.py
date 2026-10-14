"""Sort algorithms"""

from math import ceil, log2

def selection_sort(array: list[int]) -> list[int]:
    """Sort a list using the selection sort algorithm"""
    n = len(array)
    i = 0
    while i < n - 1:
        pos = i
        for j in range(i + 1, n):
            if array[j] < array[pos]:
                pos = j
        if pos != i:
            array[i], array[pos] = array[pos], array[i]
        i += 1
    return array

def bubble_sort(array: list[int]) -> list[int]:
    """Sort a list using the bubble sort algorithm"""
    for _ in range(len(array)):
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        if not swap:
            break
    return array

def insertion_sort(array: list[int]) -> list[int]:
    """Sort a list using the insertion sort algorithm"""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def quick_sort(array: list[int]) -> list[int]:
    """Sort a list using the quick sort algorithm"""
    if len(array) > 1:
        pivot = array.pop()
        greater_array, equal_array, lesser_array = [], [pivot], []
        for element in array:
            if element == pivot:
                equal_array.append(element)
            elif element > pivot:
                greater_array.append(element)
            else:
                lesser_array.append(element)
        array = quick_sort(lesser_array) + equal_array + quick_sort(greater_array)
    else:
        return array
    return array

def merge_sort(array: list[int]) -> list[int]:
    """Sort a list using the merge sort algorithm"""
    if len(array) == 1:
        return array
    mid = (len(array) - 1) // 2

    array_1 = merge_sort(array[:mid + 1])
    array_2 = merge_sort(array[mid + 1:])

    result = merge(array_1, array_2)

    return result

def merge(array_1: list[int], array_2: list[int]) -> list[int]:
    """Merge two lists used in merge sort"""
    merged = []
    i = 0
    j = 0
    while(i <= len(array_1) - 1 and j <= len(array_2) - 1):
        if array_1[i] < array_2[j]:
            merged.append(array_1[i])
            i += 1
        else:
            merged.append(array_2[j])
            j += 1
    if i > len(array_1)-1:
        while j <= len(array_2) - 1:
            merged.append(array_2[j])
            j += 1
    else:
        while i <= len(array_1) - 1:
            merged.append(array_1[i])
            i += 1
    return merged

def heap_sort(array: list[int]) -> list[int]:
    """Sort a list using the heap sort algorithm"""
    n = len(array)
    for i in range(n // 2, -1, -1):
        make_heap(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        make_heap(array, i, 0)

    return array

def make_heap(array: list[int], n: int, i: int) -> None:
    """Create the heap structure for heap sorting"""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        make_heap(array, n, largest)

def shell_sort(array: list[int]) -> list[int]:
    """Sort a list using the shell sort algorithm"""
    n = len(array)
    k = int(ceil(log2(n)))
    while True:
        interval = 2 ** k - 1
        if interval <= 0:
            break
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1

    return array
