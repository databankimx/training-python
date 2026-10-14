## Selection Sort - O(*n*²)

Let's have a look at the algorithm for the O(*n*²) **Selection Sort**.

The selection sort is probably the first method a new developer comes up with
for sorting an array. I have always thought of this as the *naive sort
algorithm*.

---

### Selection Sort Algorithm Pseudocode

In a selection sort, we start with the beginning of the array `array[0]` and
find the smallest value in the rest of the array. Then we swap those two values,
move to `array[1]`, and repeat until we reach the end of the array.

```pseudocode
For i from 0 to n-1
    Find smallest element between array[i] and array[n-1]
    Swap smallest element with array[i]
```

#### Complexity Review

Given an array of size *n* elements...

We iterate an outer loop over each element in the array, and within that loop
iterate a second loop over the portion of the array with indices higher than
the current element.

Because the size of the second loop shrinks over time, we will perform fewer
than *n*² iterations. We can compute the iteration count as:

```python
sum(range(n))
```

If we look at the rate that increases, we see this pattern:

|*n*|operations|*n* rate|op rate|
|-:|-:|-:|-:|
|10|45|||
|100|4,950|10|~100|
|1,000|499,500|10|~100|
|10,000|49,995,000|10|~100|
|100,000|4,999,950,000|10|~100|

We can see that when *n* is multiplied by 10, the number of operations is
multiplied by about 100.

And since 100 = 10², we know that this algorithm is O(*n*²)

Additionally, the number of operations is consistently about ½(*n*²). Recall
that we can ignore the constant modifier (in this case ½), which also 
supports the conclusion that this algorithm is O(*n*²)

---

### Programming a Selection Sort

Here is an example of how we might code a simple selection sort...

```python
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
```

---

### Some Sample Data

We will just use a simple example with an unsorted array including the 
numbers 0 through 7:

## <center>[ 7  2  5  4  1  6  0  3 ]</center>

With our array, the process would look like this:

1. Check element `[0]`  
   \- It's currently **7**

2. Scan through all the remaining elements to find the smallest  
   \- Since we stated from zero, we'll compare 7 other elements before we 
   determine that the smallest other element is the **0** at index `[6]`.

3. If that smallest element is less than the value at position `[0]` (0 < 7), 
   then we swap those elements  
   \- After the swap, the array looks like this: `[ 0 2 5 4 1 6 7 3 ]`  
   \- We've successfully got the smallest element in the first position of 
      the array  
        
    ...

We repeat those three step for each position in the array, each time
checking all the elements above the one we're comparing.

The sort process will look like this:

[ 7 2 5 4 1 6 0 3 ] (start)  
[ <span style="color:cornflowerblue">***0***</span> 2 5 4 1 6 
  <span style="color:cornflowerblue">***7***</span> 3 ] (after 8 
  comparisons)  
[ 0 <span style="color:cornflowerblue">***1***</span> 5 4 
  <span style="color:cornflowerblue">***2***</span> 6 7 3 ] (after 7 
  more comparisons)  
[ 0 1 <span style="color:cornflowerblue">***2***</span> 4
  <span style="color:cornflowerblue">***5***</span> 6 7 3 ] (after 6 
  more comparisons)  
[ 0 1 2 <span style="color:cornflowerblue">***3***</span> 5 6 7
  <span style="color:cornflowerblue">***4***</span> ] (after 5 more 
  comparisons)  
[ 0 1 2 3 <span style="color:cornflowerblue">***4***</span> 6 7
  <span style="color:cornflowerblue">***5***</span> ] (after 4 more 
  comparisons)  
[ 0 1 2 3 4 <span style="color:cornflowerblue">***5***</span> 7
  <span style="color:cornflowerblue">***6***</span> ] (after 3 more 
  comparisons)  
[ 0 1 2 3 4 5 <span style="color:cornflowerblue">***6***</span>
  <span style="color:cornflowerblue">***7***</span> ] (after 2 more 
  comparisons)  
[ 0 1 2 3 4 5 6 7 ] (after 1 final verification comparison - done)
    
> You can view an
> [HTML simulation of selection sort](./html/linear_search_animation.html)

---

#### Complexity Review:

Here we had:

* Input *n* = 8
* Number of steps = `sum(range(8))` = 28

This matches our prior computations, so this algorithm must be O(*n*²)

---

### Testing Our Conclusion

We have concluded that this algorithm has O(*n*²) complexity.

I have prepared a test program that you can run with a larger list:

[selection_sort.py](./03_selection_sort.py)

Here is an example of its output:

```
Execution Time: 2.9979 s

Selection Sort performed 49,995,000 operations to sort 10,000 numbers

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
