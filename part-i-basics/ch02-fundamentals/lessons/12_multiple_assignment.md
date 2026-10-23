## Multiple Assignment

One of Python's handiest features is assigning several values to several
variables in a single line.

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

This may seem trivial when you're working with single, stand-alone values. The
real payoff shows up when you swap two values.

---

### Swapping Values

Say you want two variables to trade places. The obvious approach needs a third
variable to hold one of the values while you move the other:

```python
a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)
```

Output:

```
2 1
```

Multiple assignment lets you skip the temporary variable entirely:

```python
a = 1
b = 2
a, b = b, a
print(a, b)
```

Output:

```
2 1
```

Python evaluates the entire right side first, building the pair `(2, 1)`, and only
then assigns the values to `a` and `b`. Both values are safe before anything gets
overwritten.

---

### Unpacking Collections

Multiple assignment is also called *unpacking*, because it takes apart a
collection and spreads its values across variables. In later chapters, you'll
meet several collection types: tuples, lists, sets, and more. Unpacking works on
all of them.

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

One caution about that last example. A set has no guaranteed order, so Python
doesn't promise that unpacking a set gives you the values in the order you wrote
them. This time, it did. Don't count on it happening every time.

---

### When the Counts Don't Match

The number of variables has to match the number of values. If it doesn't, Python
stops with a `ValueError`:

```python
a, b = 1, 2, 3
```

```
ValueError: too many values to unpack (expected 2)
```

And the other way around:

```python
a, b, c = 1, 2
```

```
ValueError: not enough values to unpack (expected 3, got 2)
```

The message tells you what it expected and what it got, so the fix is usually
obvious. Count your names and your values.

---
