## Intermediate and Advanced List Comprehensions

We've already explored list comprehensions as an alternative to loops when populating
lists. Here, we'll look at a few more examples and how they can be used.

In each example, I'll show the loop first, then the comprehension that does the same job.

> Note: the efficiency section uses the `@timer` decorator from the
> [sm_utils](https://pypi.org/project/sm-utils/) package. Install it with
> `python -m pip install sm_utils` before running the `.py` file.

---

### Basic List Comprehension

As a review, here's a basic list comprehension that creates a list of the numbers 1
through 10.

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

Anywhere a value can go in a comprehension, you can put an expression that computes it.
The expression runs once for each item, and its result goes into the list.

Here's a comprehension that uses the expression `i ** 2` to build a list of the squares of
the numbers 1 through 10.

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

### Filtering a List Comprehension Using an `if` Statement

You can add a condition to the end of a comprehension, so only the values that match it
make it into the list.

This comprehension uses the conditional `if i % 2 == 0` to build a list of only the even
squares of the numbers 1 through 10.

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

It's easy to assume that a comprehension and an explicit loop run at the same speed, since
they look so much alike. Assumptions are a bad idea in programming, so let's test it.

You can use whatever timing method you like. In my example, we'll use the `@timer`
decorator from the `sm_utils` library.

#### What's a Decorator?

A decorator is a function that wraps another function. The `@timer` line above `timed_for_loop`
hands that function to `timer`, which runs it, measures how long it took, and reports the
result. You don't have to change the function itself. Functions get their own chapter, and
decorators come up there, so for now, think of `@timer` as a stopwatch you can clip onto
any function.

Here, we'll compare the time it takes to build a list of the squares of the first million
integers, using a loop and then a comprehension.

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

In one test run, the list comprehension was slightly faster than the explicit loop. The gap
is small and changes from run to run, so run the example yourself to see your own timings.

---

### Nested List Comprehensions

Just like loops, comprehensions can nest.

Here's a nested comprehension that produces a 3x3 two-dimensional matrix.

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

The comprehension takes much less code, and once you're used to the pattern, it's easier to
read too.

---

> **About the `.py` file:** the file wraps these examples in functions, and it uses `def`
> and type hints such as `list[int]`. Functions are covered in Chapter 8, so for now, read
> those parts as packaging. The loops and comprehensions are the same ones shown above.
>
> The file also calls `pause()` and `clear_terminal()` from `sm_utils`. `pause()` waits for you before it continues, and `clear_terminal()` clears the screen. In the
> runner, expect a pause between examples, and a fresh screen when the example changes.

---
