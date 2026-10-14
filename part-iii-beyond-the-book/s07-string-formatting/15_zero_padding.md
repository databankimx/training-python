## Zero Padding

Especially when interacting with older data (and you *will* have to interact
with old data), it can be important to ensure that a string field contains an
exact amount of characters. When working with numerical data, this often
means that you will need to pad the string with leading zeros.

Zero-padding works a little differently from the fill patterns we saw in the
previous example. While a pad character precedes the alignment indicator, the
`0` character for padding precedes the width value (after the alignment).

---

### Padding Numbers

The most common use of zero padding is on numerical data.

```python
nums = [1, -7, 123]
for n in nums:
    print(f"{n:>05d}, {n:>06.1f}")
```

Output:

```
00001, 0001.0
000-7, 00-7.0
00123, 0123.0
```

---

### Padding Strings

Although it has fewer use-cases, you can (of course) add zero-padding to a
string value (not just to a number).

```python
s = "abc"
print(f"{s:>05}")
```

Output:

```
00abc
```

---

### Fills Trump Zero Padding

If you specify bot a fill character and zero padding, the fill character will
be used, and the zero padding will be ignored.

```python
nums = [1, -7, 123]
for n in nums:
    print(f"{n:•>05d}, {n:•>06.1f}")
```

Output:

```
••••1, •••1.0
•••-7, ••-7.0
••123, •123.0
```

---
