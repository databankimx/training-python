"""Rounding Functions"""

import numpy as np

def main() -> None:
    """Main Function"""
    arr = np.array([-3.1666, 3.6667])
    print(f"Array:    {arr}")
    print(f"Truncate: {np.trunc(arr)}")
    print(f"Fix:      {np.fix(arr)}")
    print(f"Around:   {np.around(arr, 2)}")
    print(f"Round:    {np.around(arr, 2)}")
    halves = np.array([2.5, 3.5])
    print(f"Halves:   {halves}")
    print(f"Around:   {np.around(halves)}")
    print(f"Round:    {np.around(halves)}")
    print(f"Floor:    {np.floor(arr)}")
    print(f"Ceil:     {np.ceil(arr)}")

if __name__ == "__main__":
    main()
