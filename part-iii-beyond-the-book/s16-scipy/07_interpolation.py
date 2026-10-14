"""Interpolation with SciPy"""

import numpy as np
#pylint: disable=no-name-in-module
from scipy.interpolate import interp1d, UnivariateSpline, Rbf

def linear_interpolation() -> None:
    """Estimate values between known points using straight lines"""
    xs = np.arange(10)
    ys = 2 * xs + 1
    func = interp1d(xs, ys)
    new_xs = np.arange(2.1, 3, 0.1)
    print("Linear interpolation (y = 2x + 1):")
    for x, y in zip(new_xs[:3], func(new_xs[:3])):
        print(f"x = {x:.1f} -> y = {y:.1f}")
    print()

def spline_interpolation() -> None:
    """Fit a smooth curve through the known points"""
    xs = np.arange(10)
    ys = xs ** 2 + np.sin(xs) + 1
    func = UnivariateSpline(xs, ys)
    new_xs = np.arange(2.1, 3, 0.1)
    true_ys = new_xs ** 2 + np.sin(new_xs) + 1
    print("Spline interpolation:")
    print(f"Estimated: {np.round(func(new_xs), 2)}")
    print(f"Actual:    {np.round(true_ys, 2)}\n")

def rbf_interpolation() -> None:
    """Interpolate with radial basis functions"""
    xs = np.arange(10)
    ys = xs ** 2 + np.sin(xs) + 1
    func = Rbf(xs, ys)
    new_xs = np.arange(2.1, 3, 0.1)
    true_ys = new_xs ** 2 + np.sin(new_xs) + 1
    print("Radial basis function interpolation:")
    print(f"Estimated: {np.round(func(new_xs), 2)}")
    print(f"Actual:    {np.round(true_ys, 2)}\n")

def main() -> None:
    """Main function"""
    linear_interpolation()
    spline_interpolation()
    rbf_interpolation()

if __name__ == "__main__":
    main()
