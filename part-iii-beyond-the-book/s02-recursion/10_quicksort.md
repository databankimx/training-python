## *Real* Real-World Example: Quicksort

Let's look at a real-world example that is actually implemented recursively: 
*Quicksort*

The Quicksort algorithm is an efficient sorting algorithm developed by 
British computer scientist Tony Hoare in 1959.

### The Algorithm

Quicksort is a divide-and-conquer algorithm:

Suppose you have a list of objects to sort.

The steps of the algorithm are as follows:
* Choose the pivot item.
* Partition the list into two sub-lists:
    1. Those items that are less than the pivot item
    2. Those items that are greater than the pivot item
* Quicksort the sub-lists recursively.

Each partitioning produces smaller sub-lists, so the algorithm is reductive.

The base cases occur when the sub-lists are either empty or have one element, 
as these conditions are inherently sorted.

### Choosing the Pivot Item

The Quicksort algorithm will work no matter which item in the list is the 
pivot.

So, we could just do this:

```python
from random import randint

# Assume we have an unsorted list called `numbers`
pivot = numbers[randint(0, len(numbers) - 1)]
```

However, some choices are better than others.

Remember that when partitioning, two sub-lists that are created:

1. Those items that are less than the pivot item
2. Those items that are greater than the pivot item

Ideally, the two sub-lists are roughly equal length, but that is true only 
when the halves are somewhat sorted already.

Because we don't know how sorted a list already is, we'll choose the median 
of the first, last, and middle elements.

```python
from statistics import median

# Assume we have an unsorted list called `numbers`
pivot = median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])
```

---

### The Code

With a strategy in place to choose the pivot, we can now build our function:

```python
from statistics import median

def quicksort(numbers: list[int]) -> list[int]:
    """Sort a list of numbers using the Quicksort algorithm (recursive)"""
    if len(numbers) <= 1:
        return numbers
    
    pivot = median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])

    items_less = [n for n in numbers if n < pivot]
    pivot_items = [n for n in numbers if n == pivot]
    items_greater = [n for n in numbers if n > pivot]

    return quicksort(items_less) + pivot_items + quicksort(items_greater)
```

---

### Testing

Let's test our Quicksort function:

```python
from random import randint

numbers = [randint(-100, 100) for _ in range(10)]
print(f"Unsorted: {numbers}")
print(f"Sorted:   {quicksort(numbers)}")
```

Output (your numbers will vary):

```
Unsorted: [20, 77, 45, -26, -87, 63, -94, -2, -66, 45]
Sorted:   [-94, -87, -66, -26, -2, 20, 45, 45, 63, 77]
```

---

### What About an Iterative Solution?

Yes, as usual, you can create an iterative solution for quicksort. It'll
quickly get messy though.

Try creating one. You'll probably return to recursion as the best choice here.

---
