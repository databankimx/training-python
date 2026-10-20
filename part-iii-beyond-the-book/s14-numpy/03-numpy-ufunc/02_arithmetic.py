"""Arithmetic `ufunc` Functions"""

import numpy as np
from numpy import ndarray

def add_arr(arr_x: ndarray, arr_y: ndarray):
    """Add two arrays"""
    print("Addition:")
    print(f"arr_x:                {arr_x}")
    print(f"arr_y:                {arr_y}")
    print(f"np.add(arr_x, arr_y): {np.add(arr_x, arr_y)}")
    print(f"arr_x + arr_y:        {arr_x + arr_y}\n")

def sub_arr(arr_x: ndarray, arr_y: ndarray):
    """Subtract two arrays"""
    print("Subtraction:")
    print(f"arr_x:                     {arr_x}")
    print(f"arr_y:                     {arr_y}")
    print(f"np.subtract(arr_x, arr_y): {np.subtract(arr_x, arr_y)}")
    print(f"arr_x - arr_y:             {arr_x - arr_y}\n")

def mult_arr(arr_x: ndarray, arr_y: ndarray):
    """Multiply two arrays"""
    print("Multiplication:")
    print(f"arr_x:                     {arr_x}")
    print(f"arr_y:                     {arr_y}")
    print(f"np.multiply(arr_x, arr_y): {np.multiply(arr_x, arr_y)}")
    print(f"arr_x * arr_y:             {arr_x * arr_y}\n")

def div_arr(arr_x: ndarray, arr_y: ndarray):
    """Divide two arrays"""
    print("Division:")
    print(f"arr_x:                   {arr_x}")
    print(f"arr_y:                   {arr_y}")
    print(f"np.divide(arr_x, arr_y): {np.divide(arr_x, arr_y)}")
    print(f"arr_x / arr_y:           {arr_x / arr_y}\n")

def int_div_arr(arr_x: ndarray, arr_y: ndarray):
    """Integer Divide two arrays"""
    print("Integer Division:")
    print(f"arr_x:                         {arr_x}")
    print(f"arr_y:                         {arr_y}")
    print(f"np.floor_divide(arr_x, arr_y): {np.floor_divide(arr_x, arr_y)}")
    print(f"arr_x // arr_y:                {arr_x // arr_y}\n")

def mod_arr(arr_x: ndarray, arr_y: ndarray):
    """Compute modulo on two arrays"""
    print("Remainder:")
    print(f"arr_x:                      {arr_x}")
    print(f"arr_y:                      {arr_y}")
    print(f"np.mod(arr_x, arr_y):       {np.mod(arr_x, arr_y)}")
    print(f"np.remainder(arr_x, arr_y): {np.remainder(arr_x, arr_y)}")
    print(f"arr_x % arr_y:              {arr_x % arr_y}\n")

def divmod_arr(arr_x: ndarray, arr_y: ndarray):
    """Compute integer division/modulo on two arrays"""
    print("Integer Division and Remainder:")
    print(f"arr_x:                   {arr_x}")
    print(f"arr_y:                   {arr_y}")
    # print(f"divmod(arr_x, arr_y):\n{np.divmod(arr_x, arr_y)}\n")
    print("np.divmod(arr_x, arr_y):", end=" ")
    for arr in np.divmod(arr_x, arr_y):
        print(arr, end=" ")
    print("\n")

def abs_arr(arr: ndarray):
    """Compute absolute values of arrays"""
    print("Absolute Values:")
    print(f"arr:              {arr}")
    print(f"np.abs(arr):      {np.abs(arr)}")
    print(f"np.absolute(arr): {np.absolute(arr)}\n")

def main() -> None:
    """Main function"""
    flt_fmt = "{:.2f}".format
    np.set_printoptions(formatter={"float_kind": flt_fmt})
    arr_x = np.array([10, 20, 30, 40, 50, 60])
    arr_y = np.array([4, 5, 6, 7, 8, 9])
    add_arr(arr_x, arr_y)
    sub_arr(arr_x, arr_y)
    mult_arr(arr_x, arr_y)
    div_arr(arr_x, arr_y)
    int_div_arr(arr_x, arr_y)
    mod_arr(arr_x, arr_y)
    divmod_arr(arr_x, arr_y)
    arr = np.array([-3, -2, -1, 0, 1, 2, 3])
    abs_arr(arr)

if __name__ == "__main__":
    main()
