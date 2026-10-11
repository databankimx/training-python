## Ch 2 - Lesson 9: Floating-Point Decimals

Floating-point (`float`) numbers are used for all non-integer numerical
values in Python. The term "floating point" refers to the fact that the
number of decimal places is not fixed.

Unlike integers, Python floats are fixed-size 64-bit signed values
(equivalent to `double` in C#) conforming to the
[IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) standard.

---

In general, floating-point arithmetic behaves as expected:

```python
print(f"0.1 + 0.1 = {0.1 + 0.1}")
print(f"0.2 + 0.2 = {0.2 + 0.2}")
print(f"2 * 0.1 = {2 * 0.1}")
print(f"2 * 0.2 = {2 * 0.2}")
```

Output:

```
0.1 + 0.1 = 0.2
0.2 + 0.2 = 0.4
2 * 0.1 = 0.2
2 * 0.2 = 0.4
```

---

When any operand is a float, the result will always be a float:

```python
x = 3
y = 2.0
z = 4
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"({x} + {y}) * {z} = {(x + y) * z}")
```

Output:

```
3 + 2.0 = 5.0
3 - 2.0 = 1.0
3 * 2.0 = 6.0
3 / 2.0 = 1.5
(3 + 2.0) * 4 = 20.0
```

---

### Programmer Warning

Because floating-point numbers are approximations in binary, you will
sometimes see an apparently arbitrary number of decimal places:

```python
print(f"0.3 = {0.3}")
print(f"0.2 + 0.1 = {0.2 + 0.1}")
print(f"3 * 0.1 = {3 * 0.1}")
```

Output:

```
0.3 = 0.3
0.2 + 0.1 = 0.30000000000000004
3 * 0.1 = 0.30000000000000004
```

This is explained in the next lesson.

---
