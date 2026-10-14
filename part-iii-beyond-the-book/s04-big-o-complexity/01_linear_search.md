## Linear Search - O(*n*)

Let's have a look at the algorithm for the O(*n*) **Linear Search**.

---

### Linear Search Algorithm Pseudocode

A linear search checks each element in the array until it finds the target 
value.

If the target value is never found, the algorithm will have checked each 
element once.

The steps in this algorithm are pretty straightforward.

```pseudocode
For every element from 0 to *n* - 1
    If the element contains the target value
        Quit and return the index of the element
    Else
        Continue to the next element

If the target value was not found
    Quit and return some failure state
```

#### Complexity Review:

Given an array of size *n* elements...

In the asymptotic (worst) case, if the target value is not in the array at all, we will have checked each element once (for a total of *n* checks).

---

### Programming a Linear Search

Here is an example of how we might code a simple linear search...

```python
def linear_search(array: list[int], target: int) -> int:
    """Find the index where the target value is stored"""
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
```

---

### Some Sample Data

We will just use a simple example with an unsorted array including the 
numbers 0 through 7:

## <center>[ 7  2  5  4  1  6  0  3 ]</center>

### Looking at the Process:

Imagine that the target value is 3. Following our algorithm, we would take 
the following steps:

1. Check if element 0 is 3 - [`7-------`]  
\- It's 7, not 3, so we continue
2. Check if element 1 is 3 - [`-2------`]  
\- It's 2, not 3, so we continue
3. Check if element 2 is 3 - [`--5-----`]  
\- It's 5, not 3, so we continue
4. Check if element 3 is 3 - [`---4----`]  
\- It's 4, not 3, so we continue
5. Check if element 4 is 3 - [`----1---`]  
\- It's 1, not 3, so we continue
6. Check if element 5 is 3 - [`-----6--`]  
\- It's 6, not 3, so we continue
7. Check if element 6 is 3 - [`------0-`]  
\- It's 0, not 3, so we continue
8. Check if element 0 is 3 - [**`-------3`**]  
\- It's 3, so we can quit, having found the target element

That's a worst case example, since I specifically chose the last number in 
the array as my target, but big-O computations are all about the worst-case.

> You can view an
> [HTML simulation of linear search](./html/linear_search_animation.html)

---

#### Complexity Review:

Here we had:

* Input *n* = 8
* Number of comparisons = 8

Because we are simply cycling through *n* items 1 time, the complexity of 
this algorithm is **O(n)**.

The time to complete the process increases linearly. If we were to change *n* 
to 100, we'd expect to take about 100 comparisons and so on.

This doesn't account for every instruction set to the computer, but we drop 
the constant multiplier and only consider the magnitude for big-O. So any 
constant multiplier (say 10 instructions per comparison) is dropped, and
O(*n*) could describe 3*n* or 12*n* or even 0.5*n*. The important factor is 
that as *n* grows, complexity grows linearly with *n*.

---

### Testing Our Conclusion

We can conclude that a linear search algorithm has O(*n*) complexity.

I have prepared a test program that you can run with a larger list:

[linear_search.py](./01_linear_search.py)

Here is an example of its output:

```
Index of target [3306]: i = [8960]

Linear Search performed 8,961 comparisons to search 10,000 numbers.

Computed complexity: O(n) - linear

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
