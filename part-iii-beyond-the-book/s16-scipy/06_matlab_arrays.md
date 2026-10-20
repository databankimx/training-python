## MATLAB Arrays

Many engineers and scientists have data stored in MATLAB's `.mat` format. SciPy
can read and write these files, which lets Python code share data with MATLAB
without converting it by hand.

SciPy provides these functions in the `scipy.io` module:

* `savemat()` writes a dictionary of arrays to a `.mat` file
* `loadmat()` reads a `.mat` file back into a dictionary

The code for this lesson is in [06_matlab_arrays.py](./06_matlab_arrays.py).

---

### Exporting Data to MATLAB

The `savemat()` function takes a file name and a dictionary. Each key in the
dictionary becomes a variable name in the file:

```python
import numpy as np
from scipy import io

arr = np.arange(10)
io.savemat("arr.mat", {"vec": arr})
```

The dictionary key `"vec"` is the name the variable will have in MATLAB.

The function also accepts an optional `do_compression` argument. When it is
`True`, the file is compressed. The default is `False`.

---

### Importing Data from MATLAB

The `loadmat()` function reads the file and returns a dictionary. Each key is a
variable name from the file, and each value is the data for that variable:

```python
my_data = io.loadmat("arr.mat")
print(f"Loaded shape: {my_data['vec'].shape}")
print(f"Loaded values: {my_data['vec']}")
```

Output:

```
Loaded shape: (1, 10)
Loaded values: [[0 1 2 3 4 5 6 7 8 9]]
```

The shape is `(1, 10)`, not `(10,)`. MATLAB stores vectors as two-dimensional
arrays, and SciPy keeps that shape when it loads them. The dictionary also
includes some header entries that MATLAB files need, which begin with two
underscores.

---

### Removing Extra Dimensions

Setting `squeeze_me=True` removes dimensions that have a length of one:

```python
my_data = io.loadmat("arr.mat", squeeze_me=True)
print(f"Squeezed shape: {my_data['vec'].shape}")
print(f"Squeezed values: {my_data['vec']}")
```

Output:

```
Squeezed shape: (10,)
Squeezed values: [0 1 2 3 4 5 6 7 8 9]
```

Use `squeeze_me=True` when you want a plain one-dimensional array that works
with the NumPy functions from earlier lessons.

---

### Try It

Run the script. It saves the file to the same folder as the script, so you can
open `arr.mat` in MATLAB or Octave to check the variable. Then change the
array to store a two-dimensional table, and check how the shape comes back.

---
