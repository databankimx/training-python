## Multiple Assignment

One powerful feature of Python is the ability to assign multiple values to
variables in a single statement:

```python
x, y, z = 1, 2, 3
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
```

Output:

```
x = 1
y = 2
z = 3
```

---

This becomes even more useful when working with Python's collection types
(tuples, lists, sets, ranges), which we will cover in later chapters:

```python
# From a range
a, b, c = range(1, 4)
print(a, b, c)

# From a tuple
d, e, f = (1, 2, 3)
print(d, e, f)

# From a list
g, h, i = [1, 2, 3]
print(g, h, i)

# From a set
j, k, l = {1, 2, 3}
print(j, k, l)
```

Output:

```
1 2 3
1 2 3
1 2 3
1 2 3
```

---
