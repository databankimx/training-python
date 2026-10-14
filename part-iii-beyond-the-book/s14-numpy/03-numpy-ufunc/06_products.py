"""Products of Numpy Arrays"""

import numpy as np

def multiplication(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Multiply two arrays"""
    print("Multiplying:")
    print(f"arr_a:                     {arr_a}")
    print(f"arr_b:                     {arr_b}")
    print(f"np.multiply(arr_a, arr_b): {np.multiply(arr_a, arr_b)}\n")

def product(arr: np.ndarray) -> None:
    """Product of array"""
    print("Array Product:")
    print(f"Array:                       {arr}")
    print(f"np.prod(arr):                {np.prod(arr)}\n")

def product_y(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Product of two arrays"""
    print("Product (y-Axis):")
    print(f"arr_a:                       {arr_a}")
    print(f"arr_b:                       {arr_b}")
    print(f"np.prod([arr_a, arr_b]):     {np.prod([arr_a, arr_b])}\n")

def product_x(arr_a: np.ndarray, arr_b: np.ndarray) -> None:
    """Product of two arrays"""
    print("Product (x-Axis):")
    print(f"arr_a:                       {arr_a}")
    print(f"arr_b:                       {arr_b}")
    print(f"np.prod([arr_a, arr_b]):     {np.prod([arr_a, arr_b], axis=1)}\n")

def cumulative_product(arr: np.ndarray) -> None:
    """Cumulative product of an array"""
    print("Cumulative product:")
    print(f"Array:                       {arr}")
    print(f"np.cumprod(arr):             {np.cumprod(arr)}\n")

def main() -> None:
    """Main Function"""
    arr_a = np.array([1, 2, 3, 4])
    arr_b = np.array([5, 6, 7, 8])
    multiplication(arr_a, arr_b)
    product(arr_a)
    product_y(arr_a, arr_b)
    product_x(arr_a, arr_b)
    cumulative_product(arr_a)

if __name__ == "__main__":
    main()
