"""Creating NumPy Arrays"""

import numpy as np

def array_from_list(lst: list[int]) -> np.ndarray:
    """Creates a numpy array from a list"""
    return np.array(lst)

def array_from_tuple(tpl: tuple[int]) -> np.ndarray:
    """Creates a numpy array from a tuple"""
    return np.array(tpl)

def main() -> None:
    """Main Function"""
    lst = [1, 2, 3, 4, 5]
    arr = array_from_list(lst)
    print("List:", lst, type(lst))
    print("Array:", arr, type(arr), "\n")

    tpl = (1, 2, 3, 4, 5)
    arr = array_from_tuple(tpl)
    print("Tuple:", tpl, type(tpl))
    print("Array:", arr, type(arr), "\n")

if __name__ == "__main__":
    main()
