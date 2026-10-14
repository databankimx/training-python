## Merge Sort - O(*n* log *n*)

Let's look at the algorithm for the O(*n* log *n*) **Merge Sort**.

Merge sort is another divide-and-conquer algorithm. It splits the array in half,
sorts each half, and then *merges* the two sorted halves into one sorted list.

---

### Merge Sort Algorithm Pseudocode

```pseudocode
If the array has 1 element
    It is already sorted, so return it
Split the array into a left half and a right half
Merge sort the left half
Merge sort the right half
Merge the two sorted halves:
    Compare the first unused element of each half
    Add the smaller one to the result
    Repeat until one half is empty
    Add the remaining elements of the other half
```

#### Complexity Review:

Splitting the array in half repeatedly gives about log₂*n* levels. At each
level, the merge step looks at every element once, so the work at each level is
about *n*. The total is about *n* × log₂*n*.

Unlike quick sort, merge sort always splits the array in half, so the
worst case is also O(*n* log *n*).

---

### Programming a Merge Sort

```python
def merge_sort(array: list[int]) -> list[int]:
    """Sort a list using the merge sort algorithm"""
    if len(array) == 1:
        return array
    mid = (len(array) - 1) // 2

    array_1 = merge_sort(array[:mid + 1])
    array_2 = merge_sort(array[mid + 1:])

    return merge(array_1, array_2)

def merge(array_1: list[int], array_2: list[int]) -> list[int]:
    """Merge two lists used in merge sort"""
    merged = []
    i = 0
    j = 0
    while i <= len(array_1) - 1 and j <= len(array_2) - 1:
        if array_1[i] < array_2[j]:
            merged.append(array_1[i])
            i += 1
        else:
            merged.append(array_2[j])
            j += 1
    merged.extend(array_1[i:])
    merged.extend(array_2[j:])
    return merged
```

The `merge()` function uses two indices, one for each sorted half. The
`extend()` calls at the end add whatever is left over from the half that
still has elements.

---

### Testing Our Conclusion

I have prepared a test program that you can run with a larger list:

[merge_sort.py](./07_merge_sort.py)

Run the program and compare its comparison count with the O(*n*²) sorts:

```pwsh
python 07_merge_sort.py
```

---
