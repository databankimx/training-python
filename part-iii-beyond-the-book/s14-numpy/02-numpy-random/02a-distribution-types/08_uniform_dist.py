"""Uniform Distribution"""

from numpy import random, ndarray, float64, long
import matplotlib.pyplot as plt
import seaborn as sns

def uniform_kde(uni: ndarray[float64]) -> None:
    """Generate a uniform distribution with 1000 values"""
    sns.kdeplot(uni)
    plt.show()

def uniform_hist(uni: ndarray[float64]) -> None:
    """Generate a uniform distribution with 1000 values"""
    sns.histplot(uni)
    plt.show()

def uniform_compare(uni: ndarray[float64], norm: ndarray[long]) -> None:
    """Generate a uniform distribution with 1000 values"""
    sns.kdeplot(uni, fill=True, color="blue", label="Uniform")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.show()

def main() -> None:
    """Main function"""
    rng = random.default_rng()
    uni = rng.uniform(size=1000)
    uniform_kde(uni)
    uniform_hist(uni)
    norm = rng.normal(size=1000)
    uniform_compare(uni, norm)

if __name__ == "__main__":
    main()
