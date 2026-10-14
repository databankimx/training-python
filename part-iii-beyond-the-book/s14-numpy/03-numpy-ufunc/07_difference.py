"""Differences of Numpy Arrays"""

import numpy as np
from utility_functions import ord_suffix

def subtraction(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Subtract an array"""
    print("Subtraction:")
    print(f"arr_a:  {arr_a}")
    print(f"arr_b:  {arr_b}")
    print("np.subtract(arr_a, arr_b):")
    print(f"{np.subtract(arr_a, arr_b)}\n")

def difference(arr: np.ndarray) -> None:
    """Calculate the difference of an array"""
    print("Difference:")
    print(f"arr:    {arr}")
    print("np.diff(arr):")
    print(f"{np.diff(arr)}\n")

def difference_repeat(arr: np.ndarray) -> None:
    """Calculate the 2nd-degree difference of an array"""
    print("Higher-Degree Difference:")
    print(f"arr:    {arr}")
    for i in range(len(arr) - 1):
        print("...")
        r = i + 1
        print(f"np.diff(arr, n={r}):")
        print(f"{r}{ord_suffix(r)}-degree: {np.diff(arr, n=r)}")
    print()

def difference_y(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Calculate the difference between two arrays"""
    print("Difference (y-Axis):")
    print(f"arr_a:  {arr_a}")
    print(f"arr_b:  {arr_b}")
    print("np.diff([arr_a, arr_b], axis=0):")
    print(f"{np.diff([arr_a, arr_b], axis=0)}\n")

def difference_x(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Calculate the difference between two arrays"""
    print("Difference (x-Axis):")
    print(f"arr_a:  {arr_a}")
    print(f"arr_b:  {arr_b}")
    print("np.diff([arr_a, arr_b], axis=1):")
    print(f"{np.diff([arr_a, arr_b], axis=1)}\n")

def main() -> None:
    """Main Function"""
    arr_a = np.array([3, 9, 6, 1, 4])
    arr_b = np.array([5, 8, 7, 2, 0])
    subtraction(arr_a, arr_b)
    difference(arr_a)
    difference_repeat(arr_a)
    difference_y(arr_a, arr_b)
    difference_x(arr_a, arr_b)

if __name__ == "__main__":
    main()
