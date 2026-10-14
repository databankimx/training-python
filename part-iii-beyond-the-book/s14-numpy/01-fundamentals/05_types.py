"""Data types in NumPy arrays"""

import numpy as np

def integer() -> None:
    """Look at type of integer array"""
    arr = np.array([1, 2, 3, 4])
    print(arr, "type =", arr.dtype, "\n")

def string() -> None:
    """Look at type of string array"""
    arr = np.array(["apple", "banana", "cherry"])
    print(arr, "type =", arr.dtype, "\n")

def floating_point() -> None:
    """Look at type of explicit float array"""
    arr = np.array([1, 2, 3, 4], dtype="f")
    print(arr, "type =", arr.dtype, "\n")

def sized_int() -> None:
    """Look at type of explicitly-sized integer array"""
    arr = np.array([1, 2, 3, 4], dtype="i1")
    print(arr, "type =", arr.dtype, "\n")

def conv_error() -> None:
    """Error if unable to convert value to desired type"""
    try:
        arr = np.array(["a", "2", "3"], dtype="i")
        print(arr, "type =", arr.dtype, "\n")
    except ValueError as e:
        print(f"----------\n{e}\n----------\n")

def type_change() -> None:
    """Changing the type of an array"""
    arr = np.array([0.1, 2.1, 3.1])
    print("Original:", arr, "type =", arr.dtype, "\n")

    new_arr = arr.astype("i1")
    print("New ('i1'):", new_arr, "type =", new_arr.dtype)

    new_arr = arr.astype(int)
    print("New (int):", new_arr, "type =", new_arr.dtype)

    new_arr = arr.astype(np.int16)
    print("New (np.int16):", new_arr, "type =", new_arr.dtype)

    new_arr = new_arr.astype(bool)
    print("New from new (bool):", new_arr, "type =", new_arr.dtype)

    print("\nOriginal:", arr, "type =", arr.dtype, "\n")

def main() -> None:
    """Main Function"""
    integer()
    string()
    sized_int()
    floating_point()
    conv_error()
    type_change()

if __name__ == "__main__":
    main()
