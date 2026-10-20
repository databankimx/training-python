## Intermediate and Advanced List Comprehensions

We've already explored the use of list comprehensions as an alternative to
loops when populating lists.

Here, we'll review a few more examples of comprehensions and how they can 
be used.

In each example, I will include the example as a loop and then as a 
comprehension.

> Note: the efficiency section uses the `@timer` decorator from the
> [sm_utils](https://pypi.org/project/sm-utils/) package. Install it with
> `python -m pip install sm_utils` before running the `.py` file.

---

### Basic List Comprehension

As a review, here is an example of a basic list comprehension that creates
a list of the numbers 1 through 10.

```python
# Using a Loop
n = 10
numbers = []
for i in range(1, n + 1):
    numbers.append(i)
print(numbers)
```

```python
# Using a List Comprehension
n = 10
numbers = [i for i in range(1, n + 1)]
print(numbers)
```

Output:

The output is the same from either code sample:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### List Comprehension with a Calculation

Because an expression is treated the same as the value it produces, we can
embed expressions in our list comprehensions.

Here is an example of a list comprehension that uses an expression
`i ** 2` to populate a list of the squares of the numbers 1 through 10.

```python
# Using a Loop
n = 10
numbers = []
for i in range(1, n + 1):
    numbers.append(i ** 2)
print(numbers)
```

```python
# Using a List Comprehension
n = 10
numbers = [i ** 2 for i in range(1, n + 1)]
print(numbers)
```

Output:

The output is the same from either code sample:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

### Filtering a List Comprehension using an `if` Statement

We can append a condition to the end of a comprehension to include only the
values that match the condition as a filter.

This is an example of a list comprehension that uses a conditional
`if i % 2 == 0` to populate a list of only the even squares of the numbers 
1 through 10.

```python
# Using a Loop
n = 10
numbers = []
for i in range(1, n + 1):
    if i % 2 == 0:
        numbers.append(i ** 2)
print(numbers)
```

```python
# Using a List Comprehension
n = 10
numbers = [i ** 2 for i in range(1, n + 1) if i % 2 == 0]
print(numbers)
```

Output:

The output is the same from either code sample:

```
[4, 16, 36, 64, 100]
```

---

### Efficiency

Looking at how comprehensions are structured, it's easy to assume that
there isn't a measurable difference between explicitly using a loop and
embedding the scope of the loop in a comprehension.

But assumptions aren't ever wise in programming. Let's test the 
proposition.

You can use whatever timing mechanism you want, but in my example, we'll 
use the `@timer` decorator from the `sm_utils` library.

Here, we'll compare the time it takes to compute a list containing the
squares of the first million integers using a loop versus a comprehension.

```python
from sm_utils import timer

@timer
def timed_for_loop(n: int) -> list[int]:
    """Calculate the square of numbers from 0 to n using a for loop"""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

@timer
def timed_list_comprehension(n: int) -> list[int]:
    """Calculate the square of numbers from 0 to n using list comprehension"""
    return [i ** 2 for i in range(n)]

n = 10 ** 6
print("First million squares:\n")
print("Using for_loop...")
timed_for_loop(n)
print("Using list_comprehension...")
timed_list_comprehension(n)
```

Output:

```
First million squares:

Using for_loop...
Execution Time: 50.344 ms

Using list_comprehension...
Execution Time: 41.93 ms
```

In one test run, the list comprehension was slightly faster than the explicit
loop. The gap is small and changes from run to run, so run the example yourself
to see your own timings.

---

### Nested List Comprehensions

Just like loops, we can nest comprehensions.

Here is an example of a nested list comprehension that produces a 3x3 2D 
matrix.

```python
# Using a Loop
n = 3
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(i * j)
    matrix.append(row)
for row in matrix:
    print(row)
```

```python
# Using a List Comprehension
n = 3
matrix = [[i * j for j in range(n)] for i in range(n)]
for row in matrix:
    print(row)
```

Output:

```
[0, 0, 0]
[0, 1, 2]
[0, 2, 4]
```

You can see that when nesting, the list comprehension takes much less code
and is substantially more readable.

---
