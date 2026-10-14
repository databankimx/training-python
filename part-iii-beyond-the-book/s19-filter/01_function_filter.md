## The `filter()` Function

In Python, the `filter()` function is a built-in function that allows a
programmer to filter a sequence of values based on a certain condition.

---

### Using a Function as a Filter

Frequently, it is useful to have a function that checks a condition on its
input. For example, here is a function that checks if a number is even:

```python
def even(n: int) -> bool:
    """Check if a number is even"""
    return not n % 2
```

If we have a list of numbers, like this one:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

We have a couple of ways to obtain the even numbers from the list.

### Using a Loop

We could use out tried-and-true `for` loop to iterate across the list:

```python
def even_loop(numbers: list[int]) -> list[int]:
    """Get even numbers using a loop"""
    even_numbers = []
    for n in numbers:
        if even(n):
            even_numbers.append(n)
    return even_numbers
```

```python
print(even_loop(numbers))
```

Output:

```
[2, 4, 6, 8, 10]
```

---

### Using a List Comprehension

We can also use a list comprehension to get the even numbers:

```python
def even_comprehension(numbers: list[int]) -> list[int]:
    """Get even numbers using a list comprehension"""    
    return [n for n in numbers if even(n)]
```

```python
print(even_comprehension(numbers))
```

Output:

```
[2, 4, 6, 8, 10]
```

---

### Using the `filter()` Function

We can also use the `filter()` function to get the even numbers:

```python
def even_filter(numbers: list[int]) -> list[int]:
    """Get even numbers using the filter function"""
    return list(filter(even, numbers))
```

```python
print(even_filter(numbers))
```

Output:

```
[2, 4, 6, 8, 10]
```

---

### Summary

In a scenario like the above, where we have a small dataset and a simple
condition, the `filter()` function doesn't have a strong advantage over
a comprehension or a loop. But in more complex scenarios, the `filter()`
function can be very useful.

---
