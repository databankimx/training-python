## Shell Sort - depends on the gap sequence (worst case O(*n*^(3/2)) with 2ᵏ - 1 gaps)

Let's look at the algorithm for **Shell Sort**. Its complexity depends on the
gap sequence it uses, so it sits between the O(*n*²) and O(*n* log *n*) sorts.

Shell sort is an improvement on insertion sort. Insertion sort is slow when a
small value is far to the right of where it belongs, because it can only move
one position at a time. Shell sort first compares elements that are far apart,
using a large *gap*, and then gradually reduces the gap. Each pass leaves the
array closer to sorted, so the final pass with gap 1 has less work to do.

---

### Shell Sort Algorithm Pseudocode

```pseudocode
Choose a sequence of gaps, largest first
For each gap:
    For each element from the gap to the end:
        Insert it into its place among the elements that are
        gap positions apart, moving larger values one gap to the right
```

#### Complexity Review:

The running time depends on the gap sequence. The script uses gaps of the form
2ᵏ - 1, starting from the largest power of two at or below *n*. With these gaps,
the work is roughly O(*n*^(3/2)) in the worst case, and it is much faster on
data that is already partly sorted. Other gap sequences give other results,
which is why the complexity of shell sort is usually described as a range.

---

### Programming a Shell Sort

```python
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
```

The `ceil()` and `log2()` functions come from the `math` module. The gap starts
at `2 ** k - 1` and halves each time through the loop, so the last pass uses a
gap of 1, which is an ordinary insertion sort on an array that is now nearly
sorted.

---

### Testing Our Conclusion

I have prepared a test program that you can run with a larger list:

[shell_sort.py](./09_shell_sort.py)

```pwsh
python 09_shell_sort.py
```

---
