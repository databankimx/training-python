## Insertion Sort - O(*n*²)

Let's have a look at the algorithm for the O(*n*²) **Insertion Sort**.

An insertion sort examines each element in the array and then locates and
moves it to its correct (sorted) position by comparing it against each of the 
prior elements (items with lower indices) in the array.

```pseudocode
For element indices `i` 1 to n-1
    For element indices `j` = i+1 to 1 (descending)
        If array[j-1] is less than array[j]
            break
        Else
            Swap elements array[j] and array[j-1]
```

#### Complexity Review

Given an array of size *n* elements...

We have an outer loop that executes *n* times, because although we start from 
the second element, we have one extra check at the end.

Additionally, we have an inner loop on each execution that can execute up to
*n*/2 times.  
Note: As *n* increases, this approaches *n*/4 times.

That would result in:

* **½ *n*²** for low values of *n*  
  and
* **¼ *n*²** for high values of *n* 

The shift in the constant multiplier does not matter, since we only care
about the highest magnitude.

So this algorithm (though faster than selection or bubble sorts) is O(*n*²)

---

### Programming an Insertion Sort

Here is an example of how we might code a simple selection sort...

```python
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
```

---

### Some Sample Data

We will just use a simple example with an unsorted array including the 
numbers 0 through 7:

## <center>[ 7  2  5  4  1  6  0  3 ]</center>

With our array, the process would look like this:

1. Set i = `1`

2. Select element `[i]`  
   \- Its value is **2**

3. Compare it with element j = `[i-1]`  
   \- **7** is greater than **2**, so we swap them  
   \- If the compared element was not larger, we'd skip to step 5

4. Decrement `j`  
   \- If we were not at the head and we did a swap, repeat from
      step 3

5. We're at the head of the array, so we increment `i` and repeat from
   step 2  
     
   ...

The sort process will look like this:

[7 <span style="color:salmon">***2***</span>, 5, 4, 1, 6, 0, 3]
 (select current element arr[1] -> 2)  
[7, <span style="color:cornflowerblue">***7***</span>, 5, 4, 1, 6, 0, 3] 
 (swap in the larger number)  
[<span style="color:cornflowerblue">***2***</span>, 7, 5, 4, 1, 6, 0, 3] 
 (swap in the current number)    
[2, 7, <span style="color:salmon">***5***</span>, 4, 1, 6, 0, 3]  
[2, 7, <span style="color:cornflowerblue">***7***</span>, 4, 1, 6, 0, 3]  
[2, <span style="color:cornflowerblue">***5***</span>, 7, 4, 1, 6, 0, 3]  
[2, 5, 7, <span style="color:salmon">***4***</span>, 1, 6, 0, 3]  
[2, 5, 7, <span style="color:cornflowerblue">***7***</span>, 1, 6, 0, 3]  
[2, 5, <span style="color:cornflowerblue">***5***</span>, 7, 1, 6, 0, 3]  
[2, <span style="color:cornflowerblue">***4***</span>, 5, 7, 1, 6, 0, 3]  
[2, 4, 5, 7, <span style="color:salmon">***1***</span>, 6, 0, 3]  
[2, 4, 5, 7, <span style="color:cornflowerblue">***7***</span>, 6, 0, 3]  
[2, 4, 5, <span style="color:cornflowerblue">***5***</span>, 7, 6, 0, 3]  
[2, 4, <span style="color:cornflowerblue">***4***</span>, 5, 7, 6, 0, 3]  
[2, <span style="color:cornflowerblue">***2***</span>, 4, 5, 7, 6, 0, 3]  
[<span style="color:cornflowerblue">***1***</span>, 2, 4, 5, 7, 6, 0, 3]  
[1, 2, 4, 5, 7, <span style="color:salmon">***6***</span>, 0, 3]  
[1, 2, 4, 5, 7, <span style="color:cornflowerblue">***7***</span>, 0, 3]  
[1, 2, 4, 5, <span style="color:cornflowerblue">***6***</span>, 7, 0, 3]  
[1, 2, 4, 5, 6, 7, <span style="color:salmon">***0***</span>, 3]  
[1, 2, 4, 5, 6, 7, <span style="color:cornflowerblue">***7***</span>, 3]  
[1, 2, 4, 5, 6, <span style="color:cornflowerblue">***6***</span>, 7, 3]  
[1, 2, 4, 5, <span style="color:cornflowerblue">***5***</span>, 6, 7, 3]  
[1, 2, 4, <span style="color:cornflowerblue">***4***</span>, 5, 6, 7, 3]  
[1, 2, <span style="color:cornflowerblue">***2***</span>, 4, 5, 6, 7, 3]  
[1, <span style="color:cornflowerblue">***1***</span>, 2, 4, 5, 6, 7, 3]  
[<span style="color:cornflowerblue">***0***</span>, 1, 2, 4, 5, 6, 7, 3]  
[0, 1, 2, 4, 5, 6, 7, <span style="color:salmon">***3***</span>]  
[0, 1, 2, 4, 5, 6, 7, <span style="color:cornflowerblue">***7***</span>]  
[0, 1, 2, 4, 5, 6, <span style="color:cornflowerblue">***6***</span>, 7]  
[0, 1, 2, 4, 5, <span style="color:cornflowerblue">***5***</span>, 6, 7]  
[0, 1, 2, 4, <span style="color:cornflowerblue">***4***</span>, 5, 6, 7]  
[0, 1, 2, <span style="color:cornflowerblue">***3***</span>, 4, 5, 6, 7]  
[0, 1, 2, 3, 4, 5, 6, 7]

HTML simulation of insertion sort coming soon!

---

#### Complexity Review:

Here we had:

* Input *n* = 8
* Number of steps = ½*n*² = 32

This matches our prior computations, so this algorithm must be O(*n*²)

---

### Testing Our Conclusion

We have concluded that this algorithm has O(*n*²) complexity.

I have prepared a test program that you can run with a larger list:

[insertion_sort.py](./05_insertion_sort.py)

Here is an example of its output:

```
Execution Time: 2.4051 s

Insertion Sort performed 24,988,362 operations to sort 10,000 numbers

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
