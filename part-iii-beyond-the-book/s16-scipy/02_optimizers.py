"""SciPy Optimizers"""

from math import cos
from scipy.optimize import root
from scipy.optimize import minimize
from numpy import ndarray

def x_plus_cos_x(x: int|float|ndarray[int|float]) -> int|float:
    """Compute x plus cos(x)"""
    if isinstance(x, ndarray):
        x = x[0]
    return x + cos(x)

def find_root() -> int|float:
    """Find the root of the equation x + cos(x) = 0"""
    r = root(x_plus_cos_x, 0)
    print(f"root of x + cos(x) = {r.x[0]:.2f}\n")

def x_squared_plus_x_plus_2(x: int|float|ndarray[int|float]) -> int|float:
    """Compute x² + x + 2"""
    if isinstance(x, ndarray):
        x = x[0]
    return x ** 2 + x + 2

def find_minimum() -> int|float:
    """Find the minimum of the equation x² + x + 2"""
    x = minimize(x_squared_plus_x_plus_2, 0, method="BFGS")
    y = x_squared_plus_x_plus_2(x.x[0])
    print(f"minimum of x² + x + 2 = ({x.x[0]:.2f}, {y})\n")

def main() -> None:
    """Main function"""
    find_root()
    find_minimum()

if __name__ == "__main__":
    main()
