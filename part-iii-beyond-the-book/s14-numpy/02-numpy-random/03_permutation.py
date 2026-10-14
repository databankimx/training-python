"""Permutations in NumPy"""

import numpy as np
from numpy import random

def shuffle_array() -> None:
    """Shuffle an array"""
    arr = np.array(range(1, 11))
    print(f"Original Array: {arr}")
    random.shuffle(arr)
    print(f"Shuffled Array: {arr}")
    print(f"Original Array: {arr}\n")

def permute_array() -> None:
    """Permute an array"""
    arr = np.array(range(1, 11))
    print(f"Original Array: {arr}")
    new_arr = random.permutation(arr)
    print(f"Permuted Array: {new_arr}")
    print(f"Original Array: {arr}\n")

def main() -> None:
    """Main function"""
    print("Permutations in NumPy")
    shuffle_array()
    permute_array()

if __name__ == "__main__":
    main()
