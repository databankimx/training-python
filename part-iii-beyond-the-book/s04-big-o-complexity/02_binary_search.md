## Binary Search - O(log *n*)

Let's have a look at the algorithm for the O(log *n*) **Binary Search**.

We can improve performance tremendously by implementing a better algorithm for
searching our data.

However, there is a caveat: the data must be sorted first. As we'll see in
later lessons, sorting is generally of much higher complexity than searching.
Because of this, the developer needs consider the value of fast search
against the cost of sorting.

---

### Binary Search Algorithm Pseudocode

A binary search algorithm checks the middle element of a sorted list. If the
target value is greater than the middle element, discard the lower half of
the array, and if the target value is less than the middle element, discard 
the upper half. Repeat this process until the target value is found.

If the target value is never found, the algorithm will have checked log₂*n*
(rounded up) elements.

```pseudocode
# Assume an already ordered array

Loop until done
    If the element at the middle of the list contains the target value
        Quit and return the index of the middle element
    Else
        If the middle element's value is less than the target value
            Remove the lower half of the current array
            Move to the next iteration of the loop
        Else
            Remove the upper half of the current array
            Move to the next iteration of the loop
If target element not found by end of loop
    Quit (Return failure state)
```

#### Complexity Review:

Given an array of size *n* elements...

Since we divide the size of the array in half on each iteration, the maximum
number of operations required (in the worst case, where the target value 
is not in the array) is equal to the number of times the array can be divided
in half until its length is 1. This is the same as the smallest power of two
that is equal to or greater than the number of elements (log₂*n*).

---

### Programming a Binary Search

Here is an example of how we might code a simple binary search...

> Note: I chose to use a recursive function for my solution, but this could
> just as easily be implemented as an iterative function using a while loop.
>
> Consider constructing that version of the function as a study assignment.

```python
def binary_search(array: list[int], target: int, low: int=-1, high: int=-1) -> int:
    """Find the index where the target value is stored"""
    if low == -1: low = 0
    if high == -1: high = len(array) - 1
    
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            return binary_search(array, target, mid + 1, high)
        return binary_search(array, target, low, mid - 1)
    else:
        return -1
```

---

### Some Sample Data

We will just use a simple example with a sorted array including the
numbers 0 through 7

---

# <center>[ 0  1  2  3  4  5  6  7 ]</center>

Imagine that the target value is 3. Following our algorithm, we would take 
the following steps:

1. Find the middle element  
   \* Note: I'm going to choose `i = 4` since the middle is between 3 & 4
2. Compare the value there.  
   (4) is greater than 3, so we drop the upper half of the array and restart 
   with `[ 0 1 2 3 ]`
3. Find the new middle element
4. Compare the value there.  
   (2) is less than 3, so we drop the lower half of the array and restart 
   with `[ 3 ]`
5. The middle is the only element left
6. Compare the value there.
    (3) is the target, so we return the index of the middle element (3)
    
> You can view an
> [HTML simulation of binary search](./html/linear_search_animation.html)

---

#### Complexity Review:

Here we had:

* Input *n* = 8
* Number of comparisons = 3

In math, a logarithm is the power to which you need to raise the base (in 
computers, we use base 2) in order to reach the specified value.

* 2 has to be raised to the third power to get 8 (*n*)
* So, log₂8 = 3

Comparing the number of comparisons we performed (3) to the base-2 log of *n* 
(3), it's fairly obvious that this algorithm's complexity is **O(log *n*)**.  
\* Note that when we omit the base in a log statement in computer science, we 
assume base 2

Now, it might seem like we're only getting a little better than twice the 
speed, but consider the rate at which the logarithm grows compared to *n*

| *n* | log₂*n* | | *n* | log₂*n* |
|-----|---------|-|-----|---------| 
| 1 | 1 | | 32 | 5 |
| 2 | 1 | | 64 | 6 |
| 4 | 2 | | 128 | 7 |
| 8 | 3 | | 256 | 8 |
| 16 | 4 | | 512 | 9 |

By the time we get to, say, an array where *n* is 10,000 elements, log₂*n* is only around 13 (2¹³ = 8196 & 2¹⁴ = 16384)

Even if we assume 14, we still have a comparative speed versus O(*n*) of 10,000/14 : over 700 times faster, and that difference continues to become greater with very large numbers (when *n* is around a million, log₂*n* is about 20 : 50,000 times faster)

The important thing is that O(log *n*) complexity grows very slowly by comparison to *n*

---

### Testing Our Conclusion

We can conclude that a binary search algorithm has O(log *n*) complexity.

I have prepared a test program that you can run with a larger list:

[binary_search.py](./02_binary_search.py)

Here is an example of its output:

```
Index of target [2110]: i = [7109]

Binary Search performed 13 comparisons to search 10,000 numbers.

Computed complexity: O(log(n)) - logarithmic

Approximate values for reference:
 · n!       = Value omitted - too large to calculate!
 · 2ⁿ       = Value omitted - too large to calculate!
 · n²       = 100,000,000
 · n log(n) = 132,878
 · n        = 10,000
 · log(n)   = 14
 ```

Run the program a few times and see what output you get.

---
