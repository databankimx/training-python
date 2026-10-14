"""Summation of Numpy Arrays"""

import numpy as np

def addition(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Add two arrays"""
    print("Adding:")
    print(f"arr_a:                {arr_a}")
    print(f"arr_b:                {arr_b}")
    print(f"np.add(arr_a, arr_b): {np.add(arr_a, arr_b)}\n")

def summation(arr: np.ndarray) -> None:
    """Sum array"""
    print("Summation:")
    print(f"Array:                {arr}")
    print(f"np.sum(arr):          {np.sum(arr)}\n")

def summation_y(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Sum two arrays"""
    print("Summation (y-Axis):")
    print(f"arr_a:                {arr_a}")
    print(f"arr_b:                {arr_b}")
    print(f"np.sum(arr_a, arr_b): {np.sum([arr_a, arr_b])}\n")

def summation_x(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Sum two arrays"""
    print("Summation (x-Axis):")
    print(f"arr_a:                {arr_a}")
    print(f"arr_b:                {arr_b}")
    print(f"np.sum(arr_a, arr_b): {np.sum([arr_a, arr_b], axis=1)}\n")

def cumulative_summation(arr: np.ndarray) -> None:
    """Cumulative sum of an array"""
    print("Cumulative sum:")
    print(f"Array:                {arr}")
    print(f"np.cumsum(arr):       {np.cumsum(arr)}\n")

def main() -> None:
    """Main function"""
    arr_a = np.array([1, 2, 3, 4])
    arr_b = np.array([5, 6, 7, 8])
    addition(arr_a, arr_b)
    summation(arr_a)
    summation_y(arr_a, arr_b)
    summation_x(arr_a, arr_b)
    cumulative_summation(arr_a)

if __name__ == "__main__":
    main()
