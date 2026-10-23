## Floating-Point Decimals

Any number with a decimal point is a floating-point number, or `float`. (The
complex numbers are the exception, and they're beyond the scope of this course.)

The name comes from how the number is stored. The decimal point isn't fixed in
one spot. It "floats" to wherever it needs to be, based on the size of the
number. That's a neat trick, and it's also the source of most float surprises.

Unlike integers, floats in Python are fixed-size, 64-bit, signed values
(equivalent to the `double` type in C#), and they follow the
[IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) standard. That fixed size is
why integers can grow without limit and floats can't.

---

Most of the time, floats behave the way you'd expect from ordinary arithmetic:

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

Mix a float into an operation, and the result is always a float, even when the
answer is a whole number:

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

Here's the catch. Computers store floats in binary, and many decimal values
can't be stored exactly in binary. `0.5` and `0.25` can, which is why they're
tidy. `0.1` and `0.3` can't, so the computer keeps an approximation. Sometimes
that approximation shows up in the output, with more decimal places than you
expected. (The next lesson explains why.)

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

Notice that `0.3` prints cleanly on its own, and the trouble only appears once
arithmetic gets involved. That's the part that bites people.

---
