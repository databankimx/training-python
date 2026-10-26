## Statistical Significance Tests

Statistical significance asks whether a result is likely to be real, or whether
it could have happened by chance. SciPy's `scipy.stats` module provides tests for
this.

Several terms come up in every test:

* **Null hypothesis**: the assumption that nothing interesting is happening.
  For example, "the two groups have the same mean."
* **Alternative hypothesis**: the claim we accept if the null hypothesis is
  rejected.
* **Alpha** (α): the threshold for significance, usually 0.05. It sets how
  unlikely a result must be before we reject the null hypothesis.
* **p-value**: the probability of a result at least as extreme as ours, if the
  null hypothesis is true.

The decision rule is simple. If the p-value is less than or equal to alpha, we
reject the null hypothesis and call the result statistically significant.
Otherwise, we keep the null hypothesis.

A test can be **one-tailed**, checking for a difference in one direction, or
**two-tailed**, checking for a difference in either direction.

The code for this lesson is in [08_significance_tests.py](./08_significance_tests.py).

---

### The T-Test

A t-test checks whether two samples have the same mean. It is a two-tailed test.

```python
import numpy as np
from scipy.stats import ttest_ind

rng = np.random.default_rng(42)
v1 = rng.normal(size=100)
v2 = rng.normal(size=100)
res = ttest_ind(v1, v2)
print(res.statistic, res.pvalue)
```

`ttest_ind()` returns a result with a `statistic` and a `pvalue`. Both samples
here come from the same distribution, so the p-value is usually large, and we
keep the null hypothesis.

---

### The KS-Test

The Kolmogorov-Smirnov test checks whether a sample follows a given
distribution. The second argument can be the name of a distribution, such as
`"norm"`:

```python
from scipy.stats import kstest

v = rng.normal(size=100)
res = kstest(v, "norm")
print(res.statistic, res.pvalue)
```

---

### Describing a Sample

`describe()` summarizes a sample in one call. It returns the number of
observations, the minimum and maximum, the mean, the variance, the skewness, and
the kurtosis:

```python
from scipy.stats import describe

v = rng.normal(size=100)
desc = describe(v)
print(desc.nobs, desc.mean, desc.skewness)
```

---

### Skewness, Kurtosis, and Normality

* **Skewness** measures symmetry. A normal distribution has skewness 0. A
  negative value means the data leans left, and a positive value means it leans
  right.
* **Kurtosis** measures how heavy the tails are. A normal distribution has
  kurtosis 0 in SciPy's default measure. Positive values mean heavier tails, and
  negative values mean lighter tails.

`normaltest()` combines these two measures and returns a p-value for the null
hypothesis that the data comes from a normal distribution:

```python
from scipy.stats import skew, kurtosis, normaltest

v = rng.normal(size=100)
print(skew(v), kurtosis(v))
print(normaltest(v).pvalue)
```

---

### Try It

Run the script. The random samples use a fixed seed, so you will see the same
numbers each time you run it. Then change the second sample in the t-test so it
has a different mean, for example by adding 1 to every value. Check that the
p-value falls below alpha.

---
