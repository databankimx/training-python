"""Numerical integration with SciPy"""

import math
from scipy.integrate import quad

def square(x: float) -> float:
    """Compute x squared"""
    return x ** 2

def integrate_square() -> None:
    """Integrate x squared from 0 to 1"""
    value, error = quad(square, 0, 1)
    print(f"Integral of x² from 0 to 1 = {value:.4f}")
    print(f"Estimated error is small: {error < 1e-10}")

def integrate_sine() -> None:
    """Integrate sin(x) from 0 to pi"""
    value, _ = quad(math.sin, 0, math.pi)
    print(f"Integral of sin(x) from 0 to π = {value:.4f}")

def main() -> None:
    """Main function"""
    integrate_square()
    integrate_sine()

if __name__ == "__main__":
    main()
