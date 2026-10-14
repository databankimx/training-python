"""Dimensions in Arrays"""

import numpy as np

def scalar() -> None:
    """Example of a zero-dimensional array (scalar)"""
    arr = np.array(42)
    print(f"Scalar ({arr.ndim}-D):", type(arr).__name__)
    print(arr, "\n")

def unidimensional() -> None:
    """Example of a one-dimensional array (unidimensional)"""
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Unidimensional ({arr.ndim}-D):", type(arr).__name__)
    print(arr, "\n")

def matrix() -> None:
    """Example of a two-dimensional array (matrix)"""
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Matrix ({arr.ndim}-D):", type(arr).__name__)
    print(arr, "\n")

def tensor() -> None:
    """Example of a three-dimensional array (3rd-order tensor)"""
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    n = arr.ndim
    print(f"{n}{ordinal(n)}-Order Tensor ({n}-D):", type(arr).__name__)
    print(arr, "\n")

def higher() -> None:
    """Example of a five-dimensional array (5th-order tensor)"""
    arr = np.array([1, 2, 3, 4], ndmin=5)
    n = arr.ndim
    print(f"{n}{ordinal(n)}-Order Tensor ({n}-D):", type(arr).__name__)
    print(arr, "\n")

def ordinal(n: int) -> str:
    """Get the ordinal suffix of a number"""
    if n // 10 % 10 != 1:
        # Logic
        if n % 10 == 1:
            return "st"
        if n % 10 == 2:
            return "nd"
        if n % 10 == 3:
            return "rd"
    return "th" 

def main() -> None:
    """Main Function"""
    scalar()
    unidimensional()
    matrix()
    tensor()
    higher()

if __name__ == "__main__":
    main()
