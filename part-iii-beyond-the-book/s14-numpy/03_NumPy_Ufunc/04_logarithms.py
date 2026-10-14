"""Logarithms in NumPy `ufunc` Functions"""

from math import log
import numpy as np

def log_calc() -> None:
    """Calculate Logarithms of an Array"""
    arr = np.arange(1, 11)
    print(f"Array: {arr}")
    print(f"Log₂:  {np.log2(arr)}")
    print(f"Log₁₀: {np.log10(arr)}")
    print(f"Logₑ:  {np.log(arr)}")

def log_any_base():
    """Calculate Logarithm to Any Base of an Array"""
    nplog = np.frompyfunc(log, 2, 1)
    arr = np.arange(1, 11)
    logs = nplog(arr, 3)
    print("Log₃: ", end=" [")
    for n in logs:
        print(f"{n:.2f}", end=" ")
    print("\b]")

def main():
    """Main Function"""
    flt_fmt = "{:.2f}".format
    np.set_printoptions(formatter={"float_kind": flt_fmt})
    log_calc()
    log_any_base()

if __name__ == "__main__":
    main()
