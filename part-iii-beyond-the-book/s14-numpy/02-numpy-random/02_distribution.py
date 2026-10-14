"""Random Distribution in NumPy."""

import numpy as np
from numpy import random

def distribution_1d(dist_data: dict[int, float]) -> None:
    """Create a 1D array using distribution rules"""
    data = np.array(list(dist_data.keys()))
    prob = np.array(list(dist_data.values()))
    ar_sz = 100
    arr = random.choice(data, p=prob, size=ar_sz)
    print(f"1D array with distribution:\n{arr}")
    u, c = np.unique(arr, return_counts=True)
    counter = dict(zip(u, c))
    for n in data:
        infix = "does not appear"
        if n in counter:
            infix = f"appears {counter[n]} times"
        print(f"• {n} {infix} in the array.")
    print()

def distribution_2d(dist_data: dict[int, float]) -> None:
    """Create a 2D array using distribution rules"""
    data = np.array(list(dist_data.keys()))
    prob = np.array(list(dist_data.values()))
    ar_sz = (10, 10)
    arr = random.choice(data, p=prob, size=ar_sz)
    print(f"2D array with distribution:\n{arr}")
    u, c = np.unique(arr, return_counts=True)
    counter = dict(zip(u, c))
    for n in data:
        infix = "does not appear"
        if n in counter:
            infix = f"appears {counter[n]} times"
        print(f"• {n} {infix} in the array.")
    print()

def main() -> None:
    """Main function."""
    dist_data = {
        3: 0.1,
        5: 0.3,
        7: 0.6,
        9: 0.0
    }
    distribution_1d(dist_data)
    distribution_2d(dist_data)

if __name__ == "__main__":
    main()
