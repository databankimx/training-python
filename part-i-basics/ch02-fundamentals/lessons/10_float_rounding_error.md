## Ch 2 - Lesson 10: Floating-Point Rounding Error

We saw in the previous lesson that floating-point arithmetic can produce
unexpected results. Here is why.

---

### Binary can only approximate most floating-point values

Any number representable in binary can be expressed as an integer multiplied
by an integer power of two. This means:

1. There are no true floating-point decimals inside the computer.
2. Most floating-point values are inexact approximations - the computer
   selects the nearest value it can express.

For example:

$$\small 0.1 \approx 7205759403792794 \times 2^{-56} \approx 0.10000000000000000555$$
$$\small 0.2 \approx 7205759403792794 \times 2^{-55} \approx 0.2000000000000000111$$

Because the discrepancy only appears at the 18th decimal place, you usually
will not see the rounding error in your output:

```python
print(0.1)
print(0.2)
```

Output:

```
0.1
0.2
```

---

At 0.3, the approximation is slightly below the real value, but still does
not show in output:

$$\small 0.3 \approx 5404319552844595 \times 2^{-54} \approx 0.29999999999999998889$$

```python
print(0.3)
```

Output:

```
0.3
```

---

### The sum of two approximations is not an approximation of the real value

The sum of the approximations of 0.1 and 0.2 is not an approximation of 0.3:

$$\small 0.10000000000000000555 + 0.2000000000000000111 \approx 0.000000000000004440$$

Here, the rounding error compounds. Python shows 17 decimal places, and
when the error moves into the 17th position, it becomes visible:

```python
print(0.1 + 0.2)
```

Output:

```
0.30000000000000004
```

---

### What do I do about it?

There are many strategies to mitigate floating-point rounding error. The
most important thing is to be aware that it happens and to structure your
code so it cannot affect your final results in meaningful ways.

For financial or precision-critical work, use Python's `decimal` module,
which provides exact decimal arithmetic at the cost of performance.

---
