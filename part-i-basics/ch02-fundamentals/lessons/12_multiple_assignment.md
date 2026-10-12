## Multiple Assignment

One powerful feature of Python is the ability to assign multiple values to
variables in a single assignment.

```python
x, y, z, = 1, 2, 3
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

That may seem trivial when working with single, stand-alone values.

However, as we progress into later chapters, Python includes various 
collection types (tuples, lists, sets, etc.), and multiple assignment can be used to deconstruct these.

```python
# From a range
a, b, c = range(1, 4)
print(a, b, c)

# From a tuple
d, e, f, = (1, 2, 3)
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
