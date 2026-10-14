## The Poisson Distribution

The *Poisson Distribution*, named for French mathematician Siméon Denis
Poisson, is used to estimate the probability that an event will occur a
specified number of times within some period of time.

Another way to think of the time interval is the limit of a binomial 
distribution.

The formula for the Poisson distribution is:

<img src="../images/poisson_formula.png" style="width:200px">

Where ***k; λ*** is the observed interval and ***k*** is the number of
occurrences.

The graph of a Poisson distribution looks like this:

<img src="../images/poisson_dist.png" style="width:260px">

The `random.poisson()` function expects two arguments:

* `lam`: Expected number of events (can be a float or array of floats)
* `size`: Output array shape

When we generate a distribution, we should use a NumPy generator instance
rather than calling the function off of `random` itself. In the code
examples, I will use the `random.default_rng()` random number generator.

---

### An Example with `λ=2`

Given that we have a known expected event frequency `2`, let's construct a
Poisson distribution based on performing the experiment 1000 times:

#### Poisson KDE Curve

Here, we're returning the KDE curve for the Poisson distribution:

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
poi = rng.poisson(lam=2, size=1000)
sns.kdeplot(poi)
plt.show()
```

Output:

<img src="../images/poisson_kde.png" style="width:300px">

---

#### Poisson Histogram#

Here, we're returning the histogram for the Poisson distribution:

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
poi = rng.poisson(lam=2, size=1000)
sns.histplot(poi)
plt.show()
```

Output:

<img src="../images/poisson_hist.png" style="width:300px">

---

### Comparing Poisson vs Normal Distributions

Here is an example showing a Poisson distribution and a normal 
distribution with its mean equivalent to λ.

> Note: These are not comparing the same data. The idea is to visually
> understand how a Poisson plot compares to a normal distribution plot.

```python
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

rng = random.default_rng()
poi = rng.poisson(lam=2, size=1000)
norm = rng.normal(loc=2, scale=1, size=1000)
sns.kdeplot(poi, fill=True, color="blue", label="Poisson")
sns.kdeplot(norm, fill=True, color="red", label="Normal")
plt.show()
```

Output:

<img src="../images/poisson_compare.png" style="width:300px">

---
