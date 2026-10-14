## Data Distribution

Data (or probability) distribution is a list of all possible values, and 
how often each value occurs.

Such lists are important when working with statistics and data science.

The `numpy.random` module offer methods that returns randomly generated 
data distributions.

---

### Random Distributions

A random distribution is a set of random numbers that follow a certain 
probability density function (a function that describes a continuous 
probability).

Generating a random distribution requires two sets of data:

* A list or array of possible values that may appear
* A list or array of the probability that each value appear

For example, we might have four possible values: 3, 5, 7 or 9 with the
following probabilities of appearance:

* Value 3 probability of appearance is 10%
* Value 5 probability of appearance is 30%
* Value 7 probability of appearance is 60%
* Value 9 probability of appearance is  0%

We could express these like this:

```python
import numpy as np

dist_data = {
    3: 0.1,
    5: 0.3,
    7: 0.6,
    9: 0.0
}
data = np.array(list(dist_data.keys()))
prob = np.array(list(dist_data.values()))
```

Note: Probabilities range from 0 to 1, where:

* 1 = The value will *always* occur
* 0 = The value will *never* occur

The sum of probabilities in the list should equal 1.

---

#### Side-Lesson: `numpy.unique()`

The `numpy.unique()` function that I use below returns an array of the
unique values in the array passed to it. If we add the 
`return_counts=True` argument, it returns a tuple including a second
array, which contains the counts of each of the unique values.

So, if we have this array:

```python
import numpy as np

arr = np.array([1, 1, 1, 2, 2, 3])
```

We can extract the unique values and their counts like this:

```python
unique_vals, val_counts = np.unique(arr, return_counts=True)
```

---

### Generating a 1D Random Distribution

We'll use the `data` and `prob` variables we created above and generate a
one-dimensional array containing a random distribution of values 
according to the probability distribution provided:

```python
from numpy import random

# -- SNIP --

ar_sz = 100
arr = random.choice(data, p=prob, size=ar_sz)
print(f"1D array with distribution:\n{arr}")
u, c = np.unique(arr, return_counts=True)
counter = dict(zip(u, c))
for n in data:
    infix = "does not appear"
    if n in counter:
        infix = f"appears {counter[n]} times"
    print(f"• {n} {infix} in the array.")
```

Output:

```
1D array with distribution:
[7 7 5 3 5 5 5 7 7 7 7 7 5 5 3 7 3 7 7 7 5 5 7 7 7 7 7 5 7 7 7 7 7 7 7 5 7
 7 7 3 5 7 5 7 7 3 5 7 3 3 3 5 5 7 5 3 7 5 7 5 7 5 5 5 5 7 7 5 5 5 5 5 7 7
 7 7 7 7 7 7 5 3 5 7 7 3 5 7 7 7 3 7 7 7 3 7 7 7 7 5]
• 3 appears 13 times in the array.
• 5 appears 31 times in the array.
• 7 appears 56 times in the array.
• 9 does not appear in the array.
```

---

### Generating a 2D Random Distribution

We can repeat the process to generate a random distribution in two
dimensions:

```python
from numpy import random

# -- SNIP --

ar_sz = (10, 10)
arr = random.choice(data, p=prob, size=ar_sz)
print(f"2D array with distribution:\n{arr}")
u, c = np.unique(arr, return_counts=True)
counter = dict(zip(u, c))
for n in data:
    infix = "does not appear"
    if n in counter:
        infix = f"appears {counter[n]} times"
    print(f"• {n} {infix} in the array.")
print()
```

Output:

```
2D array with distribution:
[[7 7 7 7 7 7 5 3 5 7]
 [7 5 7 5 7 7 5 7 3 3]
 [7 3 7 7 7 5 7 7 7 5]
 [7 7 7 3 7 7 7 7 3 7]
 [5 3 7 5 7 7 7 5 7 7]
 [7 7 7 7 7 7 5 3 7 7]
 [5 7 7 7 5 7 7 7 5 5]
 [7 7 7 7 3 5 5 3 7 7]
 [5 5 5 5 5 7 5 7 7 7]
 [7 7 7 5 7 7 7 7 7 7]]
• 3 appears 10 times in the array.
• 5 appears 24 times in the array.
• 7 appears 66 times in the array.
• 9 does not appear in the array.
```

---
