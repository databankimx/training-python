## Heap Sort - O(*n* log *n*)

Let's look at the algorithm for the O(*n* log *n*) **Heap Sort**.

A *heap* is a tree-shaped structure stored in an array. In a max-heap, every
parent is larger than or equal to its children, so the largest value is always
at the top. Heap sort uses this property: it repeatedly takes the largest value
off the top of the heap and places it at the end of the array.

---

### How the Array Becomes a Heap

An array of *n* elements can be viewed as a binary tree. For the element at
index `i`:

* its left child is at index `2i + 1`
* its right child is at index `2i + 2`

The `make_heap()` function fixes one subtree at a time. If a parent is smaller
than one of its children, it swaps them and fixes the subtree that the value
moved into.

---

### Heap Sort Algorithm Pseudocode

```pseudocode
Build a max-heap from the whole array
For each position from the last element back to the second:
    Swap the top of the heap (the largest value) with that position
    Shrink the heap by one element
    Fix the heap from the top
```

#### Complexity Review:

Fixing the heap at one node takes time proportional to the height of the tree,
which is log₂*n*. Building the heap calls this for about *n* nodes, and sorting
calls it once for each of the *n* elements. The total is about *n* × log₂*n*.

---

### Programming a Heap Sort

```python
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
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[largest] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        make_heap(array, n, largest)
```

---

### Testing Our Conclusion

Press **Visualize** in the lesson runner to step through the heap operations in your
browser.

I have prepared a test program that you can run with a larger list:

[heap_sort.py](./08_heap_sort.py)

```pwsh
python 08_heap_sort.py
```

---
