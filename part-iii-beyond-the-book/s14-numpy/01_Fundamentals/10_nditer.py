"""nditer()"""

import numpy as np

def scalar_elements() -> None:
    """Iterate over each element in a 3D array"""
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"Array:\n{arr}\nEach element:")
    for n in np.nditer(arr):
        print(n)
    print()

def conversions() -> None:
    """Convert elements to strings during iteration"""
    arr = np.array([1, 2, 3])
    print(f"Array:\n{arr}\nElements as strings:")
    for x in np.nditer(arr, flags=["buffered"], op_dtypes=["U"]):
        print("..." + x + "...")
    print()

def different_steps() -> None:
    """Use different step sizes per dimension"""
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(f"Array:\n{arr}\nDifferent step sizes:")
    for n in np.nditer(arr[:, ::2]):
        print(n)
    print()

def enumerated_1d() -> None:
    """Enumerate over each element in a 1D array"""
    arr = np.array([1, 2, 3])
    print(f"Array:\n{arr}\nEnumerated 1D Iteration:")
    for idx, x in np.ndenumerate(arr):
        print(idx, x)
    print()

def enumerated_2d() -> None:
    """Enumerate over each element in a 2D array"""
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(f"Array:\n{arr}\nEnumerated 2D Iteration:")
    for idx, x in np.ndenumerate(arr):
        print(idx, x)
    print()

def main() -> None:
    """Main Function"""
    scalar_elements()
    conversions()
    different_steps()
    enumerated_1d()
    enumerated_2d()

if __name__ == "__main__":
    main()
