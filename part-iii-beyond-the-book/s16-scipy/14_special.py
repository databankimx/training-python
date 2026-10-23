"""Special functions with SciPy"""

from scipy import special

def combinations() -> None:
    """Count the ways to choose items from a group"""
    print(f"Ways to choose 2 items from 5: {special.comb(5, 2):.0f}")

def gamma_function() -> None:
    """Evaluate the gamma function"""
    print(f"Gamma(5) = {special.gamma(5):.1f}")

def error_function() -> None:
    """Evaluate the error function"""
    print(f"erf(0) = {special.erf(0):.1f}")
    print(f"erf(1) = {special.erf(1):.4f}")

def main() -> None:
    """Main function"""
    combinations()
    gamma_function()
    error_function()

if __name__ == "__main__":
    main()
