## Quick Sort - O(*n* log *n*)

Let's look at the algorithm for the O(*n* log *n*) **Quick Sort**.

Quick sort is a divide-and-conquer algorithm. It picks one element as a
*pivot*, moves the smaller elements to one side and the larger elements to the
other, and then repeats the process on each side.

---

### Quick Sort Algorithm Pseudocode

```pseudocode
If the array has 0 or 1 elements
    It is already sorted, so return it
Choose a pivot element
Split the remaining elements into:
    lesser  - elements smaller than the pivot
    equal   - elements equal to the pivot
    greater - elements larger than the pivot
Quick sort the lesser and greater groups
Return lesser + equal + greater
```

#### Complexity Review:

Each split divides the array into two smaller groups, so the number of levels
of recursion is about log₂*n* when the pivot splits the data evenly. Each level
examines every element once, so the total work is about *n* × log₂*n*.

In the worst case, the pivot is always the smallest or largest element, and
each split only removes one element. That gives O(*n*²). The pivot is chosen
at the end of the list here, which is a common choice that can be slow on
data that is already sorted.

---

### Programming a Quick Sort

```python
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
```

The `pop()` call removes the pivot from the end of the list, so the function
changes the list it is given. The script version counts comparisons so that
they can be compared with the other algorithms.

---

### Testing Our Conclusion

I have prepared a test program that you can run with a larger list:

[quick_sort.py](./06_quick_sort.py)

Run the program a few times, and compare its comparison count with the O(*n*²)
algorithms from the earlier lessons:

```pwsh
python 06_quick_sort.py
```

---
