## Filtering Arrays

It is often necessary to obtain only values from an array that meet
certain criteria. NumPy arrays include methodology for filtering their
contents.

The syntax for obtaining a filtered array is:

```python
# Assuming array `arr` and filter array `filter_arr` exist:
result = arr[filter_arr]
```

Note:

A quick means of generating an array of boolean values is to use a
prime number sieve. Prime calculations have nothing to do with this,
but I used a utility function to generate a boolean index list.

For reference, see: [utility_functions.py](./utility_functions.py)

```python
def sieve(n) -> list[bool]:
    """Get a list of all primes up to `n`"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if not primes[p]:
            continue
        for n in range(p * 2, n + 1, p):
            primes[n] = False
    return primes
```

---

### Filtering with a Boolean Index List

The easiest way to perform filtering is to generate a list of boolean 
values. When used as as index list, any index where the value is 
`True` is included in the filter, and any index where the value is
`False` is excluded.

```python
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Array: {arr}")
filter = sieve(len(arr) - 1)
print(f"Filter: {filter}")
print(f"Filtered array: {arr[filter]}")
```

Output:

```
Array: [0 1 2 3 4 5 6 7 8 9]
Filter: [False, False, True, True, False, True, False, True, False, True]
Filtered array: [2 3 5 7 9]
```

---

### Creating a Filter with a Loop

Another simple way to generate a filter list is with a loop. Here, we
iterate over each element of the array and append a NumPy boolean 
value (`np.True_` or `np.False_`) to the filter based on whether the
element meets some specified criteria (in this case, even numbers).

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Array: {arr}")
filter_arr = []
for element in arr:
    filter_arr.append(element % 2 == 0)
print(f"Filter: {filter_arr}")
print(f"Filtered array: {arr[filter_arr]}")
```

Output:

```
Array: [1 2 3 4 5 6]
Filter: [np.False_, np.True_, np.False_, np.True_, np.False_, np.True_]
Filtered array: [2 4 6]
```

---

### Creating a Filter with a Condition

You can also apply the condition directly to the array itself.

Here, we are using `arr % 2 == 1` to generate a boolean index of all
odd numbers.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Array: {arr}")
filter_arr = arr % 2 == 1
print(f"Filter: {filter_arr}")
print(f"Filtered array: {arr[filter_arr]}")
```

Output:

```
Array: [1 2 3 4 5 6]
Filter: [ True False  True False  True False]
Filtered array: [1 3 5]
```

---
