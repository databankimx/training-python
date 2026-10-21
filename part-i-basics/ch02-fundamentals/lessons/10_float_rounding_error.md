## Float Rounding Error

We saw before that floats can produce rounding errors that seem to come out of
nowhere. So why does it happen?

---

### Binary Can Only Represent Some Decimals Exactly

Computers store numbers in binary, base 2, not base 10. A number that binary can
represent exactly is an integer multiplied by a power of two:

$$i = n \times 2^m \quad \text{where } (m, n) \in \mathbb{Z}$$

Numbers like `0.5` (one half) and `0.25` (one quarter) fit that pattern, so the
computer stores them exactly. Most decimals don't fit it. There's no exact binary
form for `0.1`, so the computer stores the closest value it can manage.

Here are the nearest values for `0.1` and `0.2`:

$\small 0.1 \approx 7205759403792794 \times 2^{-56} \approx 0.10000000000000000555$

$\small 0.2 \approx 7205759403792794 \times 2^{-55} \approx 0.2000000000000000111$

Neither one is exact, but the error is so small that it doesn't show up until
around the eighteenth decimal place. So you won't see it in your output, even
though it's there:

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

Now `0.3`. Its nearest stored value is a little *below* the real value, instead
of above it. The error still stays hidden in the output:

$\small 0.3 \approx 5404319552844595 \times 2^{-54} \approx 0.29999999999999998889776975$

```python
print(0.3)
```

Output:

```
0.3
```

---

### Adding Two Approximations Doesn't Give You an Approximation of the Sum

Here's where it gets interesting. Add the two stored values for `0.1` and `0.2`,
and you get a number that isn't the stored value for `0.3`:

$\small 0.10000000000000000555 + 0.2000000000000000111 \approx 0.3000000000000000167$

The computer then has to round that result to the nearest value it can store,
and that value is $\small 0.3000000000000000444$. The gap between that and the
real `0.3` is about $\small 4.44 \times 10^{-17}$.

The computer doesn't know you were hoping for `0.3`. It only knows you asked it to
add two approximations, so it rounds the result and moves on.

Python then prints the shortest string that identifies the stored value. Because
that value isn't the same as the stored value for `0.3`, the extra digit shows up
in your output:

```python
print(0.1 + 0.2)
```

Output:

```
0.30000000000000004
```

Python isn't counting to seventeen decimal places here. It's showing you the one
extra digit that the rounding error pushed out of hiding.

---

### So What Do I Do Now?

You can't make floats exact, but you can plan for the error. Some options:

* **Round for display.** `round(x, 2)` or an f-string format like `:.2f` is fine
  when you only need to show a value.
* **Compare with a tolerance.** Don't ask whether two floats are exactly equal.
  Ask whether they're close enough. The `math.isclose()` function does that for
  you.
* **Use `Decimal` for money.** The `decimal` module stores base-10 values exactly,
  which is what you want for currency.

The main thing is to know that rounding error will happen, and to write your code
so it doesn't decide your final results.

