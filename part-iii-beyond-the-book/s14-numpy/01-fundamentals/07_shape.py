"""Array shape"""

import numpy as np

def shape_two_d() -> None:
    """Shape of a 2D array"""
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("array:")
    print(arr)
    print("shape", arr.shape, "\n")

def shape_error() -> None:
    """Error in shape of a 2D array"""
    try:
        arr_1 = np.array([1, 2, 3])
        print(f"{arr_1} has shape {arr_1.shape}")
        arr_2 = np.array([4, 5])
        print(f"{arr_2} has shape {arr_2.shape}")
        arr = np.array([arr_1, arr_2])
        print(f"{arr_2} has shape {arr.shape}")
    except ValueError as e:
        print("----------\nShape Error:", e, "\n----------\n")

def shape_higher() -> None:
    """Shapes of a 3+D arrays"""
    three_d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print("3D array:")
    print(three_d)
    print("shape", three_d.shape, "\n")

    five_d = np.array([1, 2, 3, 4], ndmin=5)
    print("5D array:")
    print(five_d)
    print("shape", five_d.shape, "\n")

def main() -> None:
    """Main function"""
    shape_two_d()
    shape_error()
    shape_higher()

if __name__ == "__main__":
    main()
