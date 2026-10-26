## Probability Distributions with `scipy.stats`

The `scipy.stats` module has an object for each probability distribution. Each object
provides the same set of functions, which makes the distributions easy to compare.

* `pdf(x)`: the probability density at `x` (the height of the curve)
* `cdf(x)`: the probability that a value is less than or equal to `x`
* `ppf(p)`: the value below which a fraction `p` of the distribution falls (the inverse of `cdf`)

The code for this lesson is in [11_stats_distributions.py](./11_stats_distributions.py).

> Note: The earlier lesson on distribution types used NumPy to generate random samples.
> This lesson uses SciPy to calculate the exact values of the distribution.

---

### The Standard Normal Distribution

`stats.norm` is the normal distribution with mean 0 and standard deviation 1:

```python
from scipy import stats

print(f"Density at 0 (pdf): {stats.norm.pdf(0):.4f}")
print(f"Probability below 0 (cdf): {stats.norm.cdf(0):.4f}")
print(f"Probability below 1.96 (cdf): {stats.norm.cdf(1.96):.4f}")
```

Output:

```
Density at 0 (pdf): 0.3989
Probability below 0 (cdf): 0.5000
Probability below 1.96 (cdf): 0.9750
```

Half of the distribution lies below 0, and about 97.5% lies below 1.96.

---

### Finding a Value from a Probability

`ppf()` runs the process in reverse. Give it a probability, and it returns the
value that has that much of the distribution below it:

```python
print(f"Value with 97.5% below it (ppf): {stats.norm.ppf(0.975):.4f}")
```

Output:

```
Value with 97.5% below it (ppf): 1.9600
```

This is the value used for many 95% confidence intervals.

---

### A Shifted and Scaled Normal Distribution

Pass `loc` (the mean) and `scale` (the standard deviation) to create a distribution
with other values:

```python
dist = stats.norm(loc=10, scale=2)
print(f"Mean: {dist.mean():.1f}")
print(f"Standard deviation: {dist.std():.1f}")
print(f"Probability below 12 (cdf): {dist.cdf(12):.4f}")
```

Output:

```
Mean: 10.0
Standard deviation: 2.0
Probability below 12 (cdf): 0.8413
```

The value 12 is one standard deviation above the mean, so about 84% of values fall
below it.

---

### Try It

Use `stats.norm.cdf()` to find the probability that a value from `norm(loc=10, scale=2)`
falls between 8 and 12. Hint: subtract the cdf at 8 from the cdf at 12.

---
