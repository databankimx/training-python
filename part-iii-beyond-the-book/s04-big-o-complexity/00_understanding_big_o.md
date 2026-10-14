## Understanding Big-O Complexity in Programming

> Measuring programming progress by lines of code is like measuring aircraft 
> building progress by weight.  
> ~ Bill Gates

Big-O (or "order of") is a term used to describe the complexity of a 
programming algorithm in relation to the size of the input.

That's kind of a mouthful, so let's break it down.

---

### What is an Algorithm?

An algorithm is a process that performs some specific task.

* First of all, it's important to remember where an algorithm falls into 
  problem solving.
    * The solution to a problem consists of three parts
        * **Input**  
          This is the incoming, unprocessed data
            * The size of this input can vary
            * We'll refer to the input size as ***n***
        * **Process**  
          This is how we transform the input into the output
            * Typically, we describe this in terms of an algorithm (a process 
              with defined steps that takes us from the input to the output)
            * This algorithm is where we need to focus on complexity in 
              relation to the size of ***n***
        * **Output**  
          This is the processed result of the program

---

### What is Complexity?

* Next, it's useful to explain what we mean by complexity
    * First of all, with big-O, we're referring to asymptotic complexity
        * This is the *worst-case* complexity as ***n*** grows very large
    * Complexity means how quickly the process grows as the input size 
      ***n*** gets bigger.
        * For example, if we have an *n*-length unsorted array, it will 
          require (in the worst case) separately examining *n* elements to 
          search for a specific piece of information.
            * This means that the process is linear, which we express as 
              order of *n* or O(*n*)
            * Meaning that the complexity grows at the same rate as the input
        * Other algorithms might take less time
            * If the same array is already sorted, then a binary search can 
              be completed in log₂*n* operations, which we would describe as O
              (log *n*)
        * Or they might take much more time
            * Sorting the array in the first place almost always requires at 
              least *n* * log₂*n* or O(*n* log *n*)

---

### Where Can I Reduce Complexity?

* Deciding where to reduce complexity in order to improve performance is a 
  critical step in your design process.
    * Looking at the above example of an *n*-length unsorted array:
        * If we're only going to search it once (or very few times):
            * The total time cost to sort and search would be...
                * *n* * (log₂*n*)² for both the sort and one search
                * For *n* = 10,000 this would be around 1.7 million total 
                  operations
                * Since this is far more than the *n* operations it takes to 
                  search the unsorted array, in this instance, we'd probably 
                  choose not to sort the data.
        * On the other hand, if we're going to search the results many times 
          after they're sorted<br>(say 10,000 searches)...
            * Then we have a cost of:
                * *n* * (log₂*n*)² * 2 operations for one sort followed by 
                  ten thousand searches
                * Or around 3.4 million total operations
                * Contrast that with 10,000 * n (around 100 million total 
                  operations) of repeated linear search, and the pre-sort 
                  cost is now very economical.

---

### Common Big-O Complexity Levels

Here is a list of the major Big-O complexities:

#### O(1) → Constant Time

* In O(1), it takes a constant time to run an algorithm, regardless of the 
  size of the input. Examples include:
    * Setting the value of a variable
    * Performing a math operation
    * Accessing an array by index
    * Code Sample:

    ```python
    small = [1, 2, 3, 4]
    large = [1, 2, 3, ..., 10_000_000]

    def get_first_element(array: list[int]) -> int:
        # No matter which array we pass, this takes the same amount of time
        return array[0]
    ```

---

#### O(*n*) → Linear Time

* In O(*n*), the run-time increases at the same pace as the input (or a 
  constant multiple thereof). Examples include:
    * Traversing an array one time in such methods as
        * forEach
        * map
        * reduce
    * Find() Methods
        * Keeping in mind that Big-O is worst case, even though built-in find 
          methods frequently don't check every element, they are still O(*n*).
    * Code Sample:
  
    ```python
    small = [1, 2, 3, 4]
    large = [1, 2, 3, ..., 10_000_000]

    def print_all_elements(array: list[int]) -> int:
        # The run-time increases at the same pace as the array length
        for n in array:
            print(n)
    ```

---

### O(*n*²) → Quadratic Time  

* In O(*n*²), run-time increases with the square of the input. Examples 
  include:
    * Some sort algorithms
    * Nested foreach loops
        * Notes:
            * This assumes that each loop is traversing the same list.
            * If traversing different lists, we have the less common notation 
              O(*n* * *m*) or O(*nm*), which is similarly bad in terms of 
              efficiency, but is subtly different.
            * Nesting a third (or more) loop inside the second would be the 
              less common O(*n*³) → Cubic Time, etc.
            * In general O(*n*ˣ), where *x* is 2 or more, is referred to as 
              Polynomial Time
    * Code Sample:
  
    ```python
    small = [1, 2, 3, 4]
    large = [1, 2, 3, ..., 10_000_000]

    def check_duplicates(array: list[int]) -> dict[int, int]:
        # In the worst case (where there are no duplicates), this will take
        # n² iterations

        result = {}

        # Traversing the array one time
        for i in range(len(array)):
            if i in result:
                continue

            # Traversing the array again inside each outer traversal
            duplicates = 0
            for j in range(i, len(array)):
                if j != i and array[j] == array[i]:
                    duplicates += 1
            
            result[i] = duplicates
    ```

---

#### O(log *n*) → Logarithmic Time

* In O(log *n*), the running time grows in proportion to the logarithm 
  (base 2) of the input size.  Examples include:
    * Searching an ordered array by repeatedly checking the midpoint
    * Finding a value in a binary tree
    * Basically, any time the number of inputs to check is divided by 2 on 
      each iteration, it is In O(log *n*)
    * When an O(log *n*) has to be repeated in relation to the input size 
      (like in a merge sort), this becomes O(*n* log *n*) → Loglinear Time
    * Code Sample:
  
    ```python
    import math

    # Assuming the arrays are sorted
    small = [1, 2, 3, 4]
    large = [1, 2, 3, ..., 10_000_000]

    def binary_search(arr: lit[int], target: int, high: int, low: int) -> int:
        if high >= low:
            # With each iteration, we cut the array in half
            mid = int(math.floor((high + low) / 2))
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return binary_search(arr, target, mid + 1, high)
            else:
                return binary_search(arr, target, low, mid - 1)
        else:
            return -1
    ```

---

### How Much Difference Can it Make?

Here is a table showing the number of operations *n* = the first few powers 
of 2 for each of the major Big-O orders:

>| log₂*n* | *n* | *n* * log₂*n* |  *n*² |     2*ⁿ*      |     *n*!     |
>|--------:|----:|--------------:|------:|--------------:|-------------:|
>|       1 |   2 |             2 |     4 |             4 |            2 |
>|       2 |   4 |             8 |    16 |            16 |           24 |
>|       3 |   8 |            24 |    64 |           256 |        40320 |
>|       4 |  16 |            64 |   256 |        65,536 |   ~ 2 × 10¹³ |
>|       5 |  32 |           160 | 1,024 | 4,294,967,296 | ~ 2.6 × 10³⁵ |

You can see how quickly less efficient algorithms can get out of hand.

The image below illustrates the impact that the big-O of an algorithm can 
have on performance.  ![](./images/big_o_chart.png)

---

### OK - Let's Explore This

We'll explore the idea of complexity by reviewing several search and sort 
algorithms.

* Search Algorithms
    * O(*n*)
        * [Linear Search](./01_linear_search.md)
    * O(log *n*)
        * [Binary Search](./02_binary_search.md)

* Sort Algorithms
    * O(*n*²)
        * [Bubble Sort](./03_bubble_sort.md)
        * [Selection Sort](./04_selection_sort.md)
        * [Insertion Sort](./05_insertion_sort.md)
    * O(*n* log *n*)
        * [Quick Sort](./06_quick_sort.md)
        * [Merge Sort](./07_merge_sort.md)
        * [Heap Sort](./08_heap_sort.md)
        * [Shell Sort](./09_shell_sort.md)

These are by no means an exhaustive list of algorithms. There are literally
thousands of sorting algorithms to explore, but this list gives a good
overview of the types of approaches taken to solve these problems.

---
