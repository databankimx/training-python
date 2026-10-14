## Digit Grouping

When an output number is long, it can be very difficult to quickly identify
its magnitude. For example, is 2000000000 two billion or two hundred million?

Hovering the mouse and hand-counting zeros should not be necessary is a
properly designed solution.

When humans write long numbers, we use grouping symbols, like 2,000,000,000.
With the commas in place, we can immediately see that this is two billion.

Python supports grouping using either a comma `,` or an underscore `_`.

---

### Grouping with Integers

To add grouping symbols to integers, we can specify the symbol we want, with
or without the type parameter.

```python
n = 1234567
print(f"{n:,d}\t{n:_d}")
print(f"{n:,}\t{n:_}\n")
```

Output:

```
1,234,567       1_234_567
1,234,567       1_234_567
```

I personally prefer to omit the type parameter, but it's not obvious why with 
integers.

---

### Grouping with Floats

With floats, the type indicator is still optional, but here, there is a
difference in behavior when it is included versus when it is not.

```python
n = 1234567.89
print(f"{n:,f}\t{n:_f}")
print(f"{n:,}\t{n:_}\n")
```

Output:

```
1,234,567.890000        1_234_567.890000
1,234,567.89    1_234_567.89
```

As you can see, when we exclude the type parameter, Python is smart enough to
remove unnecessary trailing zeros, but when it is included, those zeros are
present.

---

We can fix this by specifying the decimal precision (covered in the next lesson).

```python
    n = 1234567.89
    print(f"{n:,.2f}\t{n:_.2f}")
    print(f"{n:,}\t{n:_}\n")
```

Output:

```
1,234,567.89    1_234_567.89
1,234,567.89    1_234_567.89
```

As you can see, when we exclude the type parameter, Python is smart enough to
remove unnecessary trailing zeros, but when it is included, those zeros are
present.

> Rule of Thumb: 
>
> * Include the `f` type indicator along with decimal precision when you want
>   to control the number of decimal places shown.
> * Omit the `f` type indicator to allow Python to show precision to the
>   rightmost non-zero digit.
>
> Note: Neither of these is the "right" or "wrong" way. The choice is
> situational.

---
