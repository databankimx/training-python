## Other Distributions

This lesson covers a few more distributions. Each one follows the same pattern
as the earlier lessons: we create a sample with a NumPy generator, plot its
KDE curve, and compare it with a normal distribution.

When we generate a distribution, we should use a NumPy generator instance
rather than calling the function off of `random` itself. In the code
examples, I will use the `random.default_rng()` random number generator.

The plots are drawn when you run the code, so this lesson shows only the code.

---

### The Multinomial Distribution

The *multinomial distribution* generalizes the binomial distribution to more
than two possible outcomes. For example, rolling a die six times gives six
possible faces on each roll.

`rng.multinomial()` takes the number of trials, the probability of each
outcome, and the output size. Each row of the result holds the count of each
outcome for one experiment.

Here, each experiment is six rolls of a fair die, and we plot how many times one
face (the first column) comes up:

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
counts = rng.multinomial(6, [1/6] * 6, size=1000)
dist = counts[:, 0]
norm = rng.normal(size=1000)
sns.kdeplot(dist, fill=True, color="blue", label="Multinomial")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.legend()
plt.show()
```

The `counts` array has one row per experiment and one column per face, so its
shape is `(1000, 6)`. Plotting a single column gives a one-dimensional
distribution we can compare with the normal curve.

---

### The Exponential Distribution

The *exponential distribution* describes the time between events that occur
at a constant average rate, such as the time between customer arrivals.

The `scale` argument is the mean of the distribution. For a rate of λ events per
unit of time, use `scale=1/λ`.

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
dist = rng.exponential(size=1000)
norm = rng.normal(size=1000)
sns.kdeplot(dist, fill=True, color="blue", label="Exponential")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.legend()
plt.show()
```

Exponential values are never negative, and most fall near zero, with a long
tail toward larger values. The normal curve, by contrast, is centered on zero
and extends into negative values.

---

### The Chi-Square Distribution

The *chi-square distribution* is the distribution of the sum of the squares of
independent standard normal values. Its single parameter, `df`, is the number of
degrees of freedom, which is the number of squared normal values added together.

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
dist = rng.chisquare(df=2, size=1000)
norm = rng.normal(size=1000)
sns.kdeplot(dist, fill=True, color="blue", label="Chi Square")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.legend()
plt.show()
```

Chi-square values are never negative. Their shape changes with `df`: small
values of `df` give a curve skewed toward zero, and larger values make it more
symmetric.

---

### The Rayleigh Distribution

The *Rayleigh distribution* describes the length of a two-dimensional vector
whose components are independent normal values with the same spread. It is often
used for wind speeds and for the magnitude of signals.

The `scale` argument controls the spread of the distribution.

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
dist = rng.rayleigh(scale=2, size=1000)
norm = rng.normal(size=1000)
sns.kdeplot(dist, fill=True, color="blue", label="Rayleigh")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.legend()
plt.show()
```

Rayleigh values are never negative, and the curve rises to a peak before tapering
off.

---

### The Pareto Distribution

The *Pareto distribution* describes quantities with a heavy tail, where a small
number of values are very large. It is often used to model wealth or the sizes
of certain events.

NumPy's `pareto()` function draws from the Lomax form of the distribution, also
called Pareto II, which starts at zero. The `a` argument is the shape parameter.
Smaller values of `a` give heavier tails.

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
dist = rng.pareto(a=2, size=1000)
norm = rng.normal(size=1000)
sns.kdeplot(dist, fill=True, color="blue", label="Pareto")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.legend()
plt.show()
```

Pareto values are never negative. Most fall near zero, but the tail stretches much
further than a normal curve.

---

### The Zipf Distribution

The *Zipf distribution* is a discrete distribution, where the frequency of the
k-th most common value falls off as a power of k. It is often used to describe word
frequencies in language, where a few words appear very often and most words are
rare.

The `a` argument must be greater than 1. The values start at 1.

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
dist = rng.zipf(a=2, size=1000)
norm = rng.normal(size=1000)
sns.kdeplot(dist, fill=True, color="blue", label="Zipf")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.legend()
plt.show()
```

Zipf values are whole numbers starting at 1, so the distribution is clustered at
the low end, with a long tail of rare, large values.

---
