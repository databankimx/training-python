## The Fast Fourier Transform

The *Fourier transform* breaks a signal into the frequencies that make it up. A
signal that repeats in a regular pattern shows up as a strong peak at its frequency.
It's used in audio processing, vibration analysis, and filtering measurements.

SciPy's `scipy.fft` module provides the *fast Fourier transform* (FFT), an efficient
way to compute the transform for sampled data.

The code for this lesson is in [12_fft.py](./12_fft.py).

---

### Transforming a Simple Wave

Here is a short sample of a cosine wave that completes one full cycle over four
points:

```python
import numpy as np
from scipy import fft

signal = np.array([1.0, 0.0, -1.0, 0.0])
spectrum = fft.fft(signal)
print(f"Signal: {signal}")
```

Output:

```
Signal: [ 1.  0. -1.  0.]
```

`fft()` returns one complex number for each frequency. The size of each number
(its magnitude) shows how strong that frequency is:

```python
print(f"Magnitude of each frequency: [{np.abs(spectrum[0]):.2f} "
      f"{np.abs(spectrum[1]):.2f} {np.abs(spectrum[2]):.2f} {np.abs(spectrum[3]):.2f}]")
```

Output:

```
Magnitude of each frequency: [0.00 2.00 0.00 2.00]
```

The two non-zero values appear at the frequency of the wave. The value at index 0
is the overall average, which is zero here.

---

### Try It

Change the signal to `[0.0, 1.0, 0.0, -1.0]`, which is a sine wave instead of a
cosine. Predict which magnitudes will be non-zero before you run the code.

---
