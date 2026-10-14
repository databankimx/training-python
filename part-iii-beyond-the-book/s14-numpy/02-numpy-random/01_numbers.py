"""Random numbers in NumPy."""

import numpy as np
from numpy import random

def random_int() -> None:
    """Generate a random integer between 1 and 100."""
    min_n, max_n = 1, 100
    x = random.randint(min_n, max_n + 1)
    print(f"Random integer ({min_n} to {max_n}):\n{x}\n")

def random_float() -> None:
    """Generate a random floating-point number between 0 and 1."""
    x = random.rand()
    print(f"Random floating-point number (0 to 1):\n{x:.2}\n")

def random_array_1d_int() -> None:
    """Generate a 1D array of random integers between 1 and 100."""
    ar_sz = 5
    min_n, max_n = 1, 100
    arr = random.randint(1, 101, ar_sz)
    print(f"Random 1D int array ({min_n} to {max_n})", end=" ")
    print(f"size: ({ar_sz}):\n{arr}\n")

def random_array_2d_int() -> None:
    """Generate a 2D array of random integers between 1 and 100."""
    ar_sz = (5, 3)
    min_n, max_n = 1, 100
    arr = random.randint(1, 101, size=ar_sz)
    print(f"Random 2D int array ({min_n} to {max_n})", end=" ")
    print(f"size: {ar_sz}:\n{arr}\n")

def random_array_1d_float() -> None:
    """Generate a 1D array of random floats between 0 and 1."""
    ar_sz = 5
    arr = random.rand(ar_sz)
    print("Random 1D float array", end=" ")
    print(f"size: ({ar_sz}):\n{arr}\n")

def random_array_2d_float() -> None:
    """Generate a 1D array of random floats between 0 and 1."""
    ar_sz = (5, 3)
    arr = random.rand(*ar_sz)
    print("Random 2D float array", end=" ")
    print(f"size: {ar_sz}:\n{arr}\n")

def choose_element() -> None:
    """Select an element at random from an array."""
    arr = np.array(range(1, 101))
    x = random.choice(arr)
    print(f"Random element from array (1 to 100):\n{x}\n")

def choose_1d_array_elements() -> None:
    """Select a 1D array of elements at random from an array."""
    arr = np.array(range(1, 101))
    ar_sz = 5
    new_arr = random.choice(arr, size=ar_sz)
    print(f"Random array of {ar_sz} elements from array (1 to 100):")
    print(f"{new_arr}\n")

def choose_2d_array_elements() -> None:
    """Select a 1D array of elements at random from an array."""
    arr = np.array(range(1, 101))
    ar_sz = (5, 3)
    new_arr = random.choice(arr, size=ar_sz)
    print(f"Random array of {ar_sz} elements from array (1 to 100):")
    print(f"{new_arr}\n")

def main() -> None:
    """Run the main program."""
    random_int()
    random_float()
    random_array_1d_int()
    random_array_2d_int()
    random_array_1d_float()
    random_array_2d_float()
    choose_element()
    choose_1d_array_elements()
    choose_2d_array_elements()

if __name__ == "__main__":
    main()
