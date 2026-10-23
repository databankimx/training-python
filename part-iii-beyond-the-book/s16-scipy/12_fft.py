"""Fast Fourier transform with SciPy"""

import numpy as np
from scipy import fft

def simple_wave() -> None:
    """Transform a short sampled cosine wave"""
    signal = np.array([1.0, 0.0, -1.0, 0.0])
    spectrum = fft.fft(signal)
    print(f"Signal: {signal}")
    print(f"Magnitude of each frequency: [{np.abs(spectrum[0]):.2f} "
          f"{np.abs(spectrum[1]):.2f} {np.abs(spectrum[2]):.2f} {np.abs(spectrum[3]):.2f}]")

def main() -> None:
    """Main function"""
    simple_wave()

if __name__ == "__main__":
    main()
