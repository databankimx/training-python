## What Is SciPy?

SciPy is a scientific computation library built on top of NumPy. It adds
functions for optimization, statistics, integration, signal processing, and
more.

Where NumPy provides the n-dimensional arrays and the basic operations on them,
SciPy provides the tools for analyzing that data: solving equations, fitting
curves, testing hypotheses, and working with the frequencies in a signal.

### What This Section Covers

The lessons in this section introduce the main SciPy modules:

* [Constants](./01_constants.md): physical and unit conversion constants
* [Optimizers](./02_optimizers.md): finding roots and minimum values
* [Sparse Data](./03_sparse.md): storing and working with mostly-empty arrays
* [Graphs](./04_graphs.md): connected components and shortest paths
* [Spatial Data](./05_spatial_data.md): triangulation, convex hulls, and distance metrics
* [MATLAB Arrays](./06_matlab_arrays.md): reading and writing `.mat` files
* [Interpolation](./07_interpolation.md): estimating values between known points
* [Significance Tests](./08_significance_tests.md): testing whether results are likely to be real
* [Integration](./09_integrate.md): estimating the area under a curve
* [Linear Algebra](./10_linalg.md): solving systems of equations, determinants, and inverses
* [Probability Distributions](./11_stats_distributions.md): exact distribution functions in `scipy.stats`
* [Fourier Transform](./12_fft.md): finding the frequencies in a signal
* [Finding Peaks](./13_signal_peaks.md): locating maxima in data
* [Special Functions](./14_special.md): combinations, the gamma function, and the error function

---

### Installation

To install the SciPy library, run the following command:

```
python -m pip install scipy
```

---

### Verify Installation

Once the SciPy library is installed, you can verify with this code:

```python
import scipy

print(f"Running SciPy version: {scipy.__version__}")
```

Output:

```
Running SciPy version: 1.14.0
```

Your version number may be newer. The lessons were written with SciPy 1.14.

---

> Note: Graphs appearing in the accompanying lessons were produced using
> the [desmos](https://www.desmos.com/calculator) online graphing
> calculator.

---
