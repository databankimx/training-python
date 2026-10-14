"""Reshaping Arrays"""

import numpy as np

def one_to_two_d(arr: np.ndarray) -> None:
    """Reshape a 1D array to a 2D array"""
    new_arr = arr.reshape(4, 3)
    print(f"Reshaped 2D array:\n{new_arr}")
    print(f"Shape = {new_arr.shape}\n")

def one_to_three_d(arr: np.ndarray) -> None:
    """Reshape a 1D array to a 3D array"""
    new_arr = arr.reshape(2, 3, 2)
    print(f"Reshaped 3D array:\n{new_arr}")
    print(f"Shape = {new_arr.shape}\n")

def one_three_unknown(arr: np.ndarray) -> None:
    """Reshape a 1D array to a 3D array"""
    new_arr = arr.reshape(2, 2, -1)
    print(f"Reshaped 3D array:\n{new_arr}")
    print(f"Shape = {new_arr.shape}\n")

def flatten_array(arr: np.ndarray) -> None:
    """Flatten a 2D array to a 1D array"""
    new_arr = arr.reshape(-1)
    print(f"Reshaped 1D array:\n{new_arr}")
    print(f"Shape = {new_arr.shape}\n")
    new_arr = arr.flatten()
    print(f"Flattened 1D array:\n{new_arr}")
    print(f"Shape = {new_arr.shape}\n")

def main():
    """Main Function"""
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(f"Original 1D array:\n{arr}\n")
    one_to_two_d(arr)
    one_to_three_d(arr)
    one_three_unknown(arr)

    arr = np.array([[1, 2], [3, 4], [5, 6]])
    print(f"Original 2D array:\n{arr}\n")
    flatten_array(arr)

if __name__ == "__main__":
    main()
