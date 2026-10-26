"""Linear algebra with SciPy"""

import numpy as np
from scipy import linalg

def solve_system() -> None:
    """Solve the linear system A x = b"""
    a = np.array([[3.0, 2.0], [1.0, 2.0]])
    b = np.array([5.0, 5.0])
    x = linalg.solve(a, b)
    print(f"Solution x = [{x[0]:.2f} {x[1]:.2f}]")

def determinant() -> None:
    """Compute the determinant of a matrix"""
    a = np.array([[3.0, 2.0], [1.0, 2.0]])
    print(f"Determinant = {linalg.det(a):.4f}")

def inverse() -> None:
    """Compute the inverse of a matrix"""
    a = np.array([[3.0, 2.0], [1.0, 2.0]])
    inv = linalg.inv(a)
    print(f"Inverse = [[{inv[0, 0]:.2f} {inv[0, 1]:.2f}]")
    print(f"           [{inv[1, 0]:.2f} {inv[1, 1]:.2f}]]")

def main() -> None:
    """Main function"""
    solve_system()
    determinant()
    inverse()

if __name__ == "__main__":
    main()
