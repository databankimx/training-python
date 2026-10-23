## Finding Peaks in Data

Many measurements have peaks: a heart rate spikes during exercise, a sensor
reading jumps when an event happens, or a signal reaches a maximum at each cycle.
Finding those peaks is often the first step in analyzing the data.

SciPy's `scipy.signal` module has the `find_peaks()` function for this task.

The code for this lesson is in [13_signal_peaks.py](./13_signal_peaks.py).

---

### Finding All Peaks

A *peak* is a value that is higher than the values on either side of it. `find_peaks()`
returns the index of every peak, along with a dictionary of extra information that
we don't need here:

```python
import numpy as np
from scipy.signal import find_peaks

data = np.array([0, 1, 0, 2, 0, 1, 0])
peaks, _ = find_peaks(data)
print(f"Data: {data}")
print(f"Peak indices: {peaks}")
```

Output:

```
Data: [0 1 0 2 0 1 0]
Peak indices: [1 3 5]
```

The values at indices 1, 3, and 5 are each higher than their neighbors. The
endpoints do not count as peaks, because they have only one neighbor.

---

### Filtering Peaks by Height

Use the `height` argument to keep only the peaks that are at least a given value:

```python
peaks, _ = find_peaks(data, height=1.5)
print(f"Peaks at least 1.5 high: {peaks}")
```

Output:

```
Peaks at least 1.5 high: [3]
```

Only the peak with a value of 2 is tall enough. This is useful for ignoring small
bumps in noisy data.

---

### Try It

Add a `distance` argument to `find_peaks()` set to 2, and predict how it changes
the result for a list of values with two peaks that are right next to each other.

---
