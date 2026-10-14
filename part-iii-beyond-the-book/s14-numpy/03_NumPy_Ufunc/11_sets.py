"""NumPy Set Operations"""

import numpy as np

def arr_set(arr: np.ndarray) -> None:
    """Show only the unique values in an array"""
    print(f"Original Array: {arr}")
    print(f"Unique Values: {np.unique(arr)}\n")

def arr_union(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Find the union of two arrays"""
    print(f"Array A: {arr_a}")
    print(f"Array B: {arr_b}")
    print(f"Union: {np.union1d(arr_a, arr_b)}\n")

def arr_intersection(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Find the intersection of two arrays"""
    print(f"Array A: {arr_a}")
    print(f"Array B: {arr_b}")
    print(f"Intersection: {np.intersect1d(arr_a, arr_b)}\n")

def arr_difference(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Find the difference between two arrays"""
    print(f"Array A: {arr_a}")
    print(f"Array B: {arr_b}")
    print(f"Difference: {np.setdiff1d(arr_a, arr_b)}\n")

def arr_symmetric_diff(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Find the symmetric difference between two arrays"""
    print(f"Array A: {arr_a}")
    print(f"Array B: {arr_b}")
    print(f"Symmetric Difference: {np.setxor1d(arr_a, arr_b)}\n")

def main() -> None:
    """Main Function"""
    arr = np.array([1, 2, 3, 2, 1, 4, 5, 5, 6, 2, 3])
    arr_set(arr)
    arr_a = np.array([1, 2, 3, 4])
    arr_b = np.array([3, 4, 5, 6])
    arr_union(arr_a, arr_b)
    arr_intersection(arr_a, arr_b)
    arr_difference(arr_a, arr_b)
    arr_symmetric_diff(arr_a, arr_b)

if __name__ == "__main__":
    main()
