## Special Functions

Some mathematical functions appear so often in science and statistics that they
have their own names. `scipy.special` provides a large collection of them, with
implementations that are accurate and fast.

The code for this lesson is in [14_special.py](./14_special.py).

---

### Combinations

`comb(n, k)` counts the number of ways to choose `k` items from a group of `n`,
where the order does not matter. It is the number of combinations used in
probability calculations:

```python
from scipy import special

print(f"Ways to choose 2 items from 5: {special.comb(5, 2):.0f}")
```

Output:

```
Ways to choose 2 items from 5: 10
```

---

### The Gamma Function

The gamma function extends the idea of a factorial to values that are not whole
numbers. For a whole number `n`, `gamma(n)` equals `(n - 1)!`:

```python
print(f"Gamma(5) = {special.gamma(5):.1f}")
```

Output:

```
Gamma(5) = 24.0
```

Since 4! = 24, the output matches. The gamma function is used in many probability
distributions, such as the chi-square and gamma distributions.

---

### The Error Function

The error function `erf()` is closely related to the normal distribution. For a
standard normal value, `erf(x / √2)` gives the probability that the value falls
within `x` standard deviations of the mean:

```python
print(f"erf(0) = {special.erf(0):.1f}")
print(f"erf(1) = {special.erf(1):.4f}")
```

Output:

```
erf(0) = 0.0
erf(1) = 0.8427
```

At 0, the error function is zero. At 1, it is about 0.8427.

---

### Try It

Use `special.comb()` to find how many ways there are to choose 3 cards from a
deck of 52. Check your answer by hand before you run the code.

---
