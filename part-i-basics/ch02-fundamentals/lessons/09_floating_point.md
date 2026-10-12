## Ch 2 - Lesson 9: Floating-Point Decimals

Floating point (`float`) numbers are used for all non-integer numerical values (except for `complex`, which is beyond the scope of our course) in
Python. The term "floating point" refers to the fact that the number of
decimal places to the right of the decimal point is not a fixed value.

Unlike integers, floating point numbers in Python are fixed-size, 64-bit, 
signed values (equivalent to the `double` type in C#) and conform to the
[IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) standard.

---

In general, you can expect floating point numbers to behave as they do in
normal arithmetic.

For example:

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

And, in Python, when you perform arithmetic operations, if any operand is a
float, then the result will always be a float.

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

### Programmer Warning!

However, because floating point numbers are always approximations when
calculated in binary, sometimes, you'll see a seemingly arbitrary number of
decimal places (this is explained in the next lesson):

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

---
