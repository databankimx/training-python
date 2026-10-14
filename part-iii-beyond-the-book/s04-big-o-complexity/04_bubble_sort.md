## Bubble Sort - O(*n*²)

Let's have a look at the algorithm for the O(*n*²) **Bubble Sort**.

---

### Selection Sort Algorithm Pseudocode

In a bubble sort, we iterate across the array looking at each element and the
one next to it. If the next element is smaller, we swap them and then move on.

After reaching the end of the array, we move back to the beginning and repeat
the process. We do this until we iterate across the array once without
performing any swaps (which means that the array is sorted).

Even though the idea is less obvious than selection sort was, is is actually
even less efficient (most of the time). There is an edge case where, if the
array is already sorted (or mostly sorted), bubble sort can be more efficient 
than selection.

```pseudocode
Repeat n-1 times
    For i from 0 to n-2
        If list[i] and list[i+1] are out of order
            Swap them
  * If no swaps occurred (this optional step will explain our edge case)
        Quit
```

#### Complexity Review

Given an array of size *n* elements...

We're iterating over n - 1 elements and then repeating that process n times.
The fact that we have to check every possible pair of elements so many times
results nearly *n*² operations for any list that is not already sorted.

So we can conclude that this algorithm is O(*n*²)

---

### Programming a Bubble Sort

Here is an example of how we might code a simple bubble sort...

```python
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
```

---

### Some Sample Data

We will just use a simple example with an unsorted array including the 
numbers 0 through 7:

## <center>[ 7  2  5  4  1  6  0  3 ]</center>

With our array, the process would look like this:

For the element 0 pass...

1. Compare elements 0 and 1  
   \- They are out of order (7 > 2), so we swap them

2. Compare elements 1 and 2  
   \- They are out of order (7 > 5), so we swap them  &nbsp;  ...  
   continue to the end of the array...

3. At this point, the largest element is in the last position, but nothing
   else is necessarily sorted.

Repeat steps 1-3 for every position, with each traversal of the array, moving the next largest element to the last remaining position.

The The sort process will look like this:

[ 7 2 5 4 1 6 0 3 ] (start)  
[<span style="color:cornflowerblue"> ***2 7*** </span>5 4 1 6 0 3 ]  
[ 2<span style="color:cornflowerblue"> ***5 7*** </span>4 1 6 0 3 ]  
[ 2 5<span style="color:cornflowerblue"> ***4 7*** </span>1 6 0 3 ]  
[ 2 5 4<span style="color:cornflowerblue"> ***1 7*** </span>6 0 3 ]  
[ 2 5 4 1<span style="color:cornflowerblue"> ***6 7*** </span>0 3 ]  
[ 2 5 4 1 6<span style="color:cornflowerblue"> ***0 7*** </span>3 ]  
[ 2 5 4 1 6 0<span style="color:cornflowerblue"> ***3 7*** </span>]  
[<span style="color:cornflowerblue"> ***2 5*** </span>4 1 6 0 3 7 ]
 (we still check, even when we don't have to swap)  
[ 2<span style="color:cornflowerblue"> ***4 5*** </span>1 6 0 3 7 ]  
[ 2 4<span style="color:cornflowerblue"> ***1 5*** </span>6 0 3 7 ]  
[ 2 4 1<span style="color:cornflowerblue"> ***5 6*** </span>0 3 7 ]  
[ 2 4 1 5<span style="color:cornflowerblue"> ***0 6*** </span>3 7 ]  
[ 2 4 1 5 0<span style="color:cornflowerblue"> ***3 6*** </span>7 ]  
[ 2 4 1 5 0 3<span style="color:cornflowerblue"> ***6 7*** </span>]  
[<span style="color:cornflowerblue"> ***2 4*** </span>1 5 0 3 6 7 ]  
[ 2<span style="color:cornflowerblue"> ***1 4*** </span>5 0 3 6 7 ]  
[ 2 1<span style="color:cornflowerblue"> ***4 5*** </span>0 3 6 7 ]  
[ 2 1 4<span style="color:cornflowerblue"> ***0 5*** </span>3 6 7 ]  
[ 2 1 4 0<span style="color:cornflowerblue"> ***3 5*** </span>6 7 ]  
[ 2 1 4 0 3<span style="color:cornflowerblue"> ***5 6*** </span>7 ]  
[ 2 1 4 0 3 5<span style="color:cornflowerblue"> ***6 7*** </span>]  
[<span style="color:cornflowerblue"> ***1 2*** </span>4 0 3 5 6 7 ]  
[ 1<span style="color:cornflowerblue"> ***2 4*** </span>0 3 5 6 7 ]  
[ 1 2<span style="color:cornflowerblue"> ***0 4*** </span>3 5 6 7 ]  
[ 1 2 0<span style="color:cornflowerblue"> ***3 4*** </span>5 6 7 ]  
[ 1 2 0 3<span style="color:cornflowerblue"> ***4 5*** </span>6 7 ]  
[ 1 2 0 3 4<span style="color:cornflowerblue"> ***5 6*** </span>7 ]  
[ 1 2 0 3 4 5<span style="color:cornflowerblue"> ***6 7*** </span>]  
[<span style="color:cornflowerblue"> ***1 2*** </span>0 3 4 5 6 7 ]  
[ 1<span style="color:cornflowerblue"> ***0 2*** </span>3 4 5 6 7 ]  
[ 1 0<span style="color:cornflowerblue"> ***2 3*** </span>4 5 6 7 ]  
[ 1 0 2<span style="color:cornflowerblue"> ***3 4*** </span>5 6 7 ]  
[ 1 0 2 3<span style="color:cornflowerblue"> ***4 5*** </span>6 7 ]  
[ 1 0 2 3 4<span style="color:cornflowerblue"> ***5 6*** </span>7 ]  
[ 1 0 2 3 4 5<span style="color:cornflowerblue"> ***6 7*** </span>]  
[<span style="color:cornflowerblue"> ***0 1*** </span>2 3 4 5 6 7 ]  
[ 0<span style="color:cornflowerblue"> ***1 2*** </span>3 4 5 6 7 ]  
[ 0 1<span style="color:cornflowerblue"> ***2 3*** </span>4 5 6 7 ]  
[ 0 1 2<span style="color:cornflowerblue"> ***3 4*** </span>5 6 7 ]  
[ 0 1 2 3<span style="color:cornflowerblue"> ***4 5*** </span>6 7 ]  
[ 0 1 2 3 4<span style="color:cornflowerblue"> ***5 6*** </span>7 ]  
[ 0 1 2 3 4 5<span style="color:cornflowerblue"> ***6 7*** </span>]  
[<span style="color:cornflowerblue"> ***0 1*** </span>2 3 4 5 6 7 ]
 (This is the start of the pass with no swaps)  
[ 0<span style="color:cornflowerblue"> ***1 2*** </span>3 4 5 6 7 ]  
[ 0 1<span style="color:cornflowerblue"> ***2 3*** </span>4 5 6 7 ]  
[ 0 1 2<span style="color:cornflowerblue"> ***3 4*** </span>5 6 7 ]  
[ 0 1 2 3<span style="color:cornflowerblue"> ***4 5*** </span>6 7 ]  
[ 0 1 2 3 4<span style="color:cornflowerblue"> ***5 6*** </span>7 ]  
[ 0 1 2 3 4 5<span style="color:cornflowerblue"> ***6 7*** </span>]  
Done!
    
> You can view an
> [HTML simulation of bubble sort](./html/bubble_sort_animation.html)

---

#### Complexity Review:

Here we had:

* Input *n* = 8
* Number of comparisons = 49 = (*n* - 1)² = *n*² - 2*n* + 1

As always, we ignore the other factors (-2*n* + 1) and take the magnitude of the highest power expression, so this algorithm is O(*n*²), and the complexity grows quadratically (polynomial time) with the square of *n*.

Again, this is the worst Big-O complexity for which it's easy to calculate the actual number of comparisons. For numbers larger than 100 or so, exponential and factorial time would exceed the max size of a 64-bit long integer.

Let's consider an edge case, where the data is already sorted. In this case, the process looks like this:

[ 0 1 2 3 4 5 6 7 ] (start)  
[<span style="color:cornflowerblue"> ***0 1*** </span>2 3 4 5 6 7 ]  
[ 0<span style="color:cornflowerblue"> ***1 2*** </span>3 4 5 6 7 ]  
[ 0 1<span style="color:cornflowerblue"> ***2 3*** </span>4 5 6 7 ]  
[ 0 1 2<span style="color:cornflowerblue"> ***3 4*** </span>5 6 7 ]  
[ 0 1 2 3<span style="color:cornflowerblue"> ***4 5*** </span>6 7 ]  
[ 0 1 2 3 4<span style="color:cornflowerblue"> ***5 6*** </span>7 ]  
[ 0 1 2 3 4 5<span style="color:cornflowerblue"> ***6 7*** </span>]  
Done!

This time, we had:

* Input *n* = 8
* Number of comparisons = 7 = *n* - 1

Because this is a best case (only occurs when all the data is sorted), we 
don't refer to this as big-O, instead using the symbol capital omega. So, 
ignoring the -1 component, we can describe the best case as Ω(*n*)

---

### Testing Our Conclusion

We have concluded that this algorithm has O(*n*²) complexity.

I have prepared a test program that you can run with a larger list:

[bubble_sort.py](./04_bubble_sort.py)

Here is an example of its output:

```
Execution Time: 8.7033 s

Bubble Sort performed 98,760,123 operations to sort 10,000 numbers

Computed complexity: O(n²) - quadratic (polynomial)

Approximate values for reference:
 • n!       = Value omitted - too large to calculate!
 • 2ⁿ       = 1.99 * 10^3009
 • n²       = 100,000,000
 • n log n  = 132,878
 • n        = 10,000
 • log n    = 14
 • const    = 1

Check file: ./data/sorted_integers.txt to validate results
```

Run the program a few times and see what output you get.

---
