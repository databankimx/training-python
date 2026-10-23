"""Finding peaks in data with SciPy"""

import numpy as np
from scipy.signal import find_peaks

def simple_peaks() -> None:
    """Find the local maxima in a short list of values"""
    data = np.array([0, 1, 0, 2, 0, 1, 0])
    peaks, _ = find_peaks(data)
    print(f"Data: {data}")
    print(f"Peak indices: {peaks}")

def tall_peaks() -> None:
    """Find only the peaks that are at least a given height"""
    data = np.array([0, 1, 0, 2, 0, 1, 0])
    peaks, _ = find_peaks(data, height=1.5)
    print(f"Peaks at least 1.5 high: {peaks}")

def main() -> None:
    """Main function"""
    simple_peaks()
    tall_peaks()

if __name__ == "__main__":
    main()
