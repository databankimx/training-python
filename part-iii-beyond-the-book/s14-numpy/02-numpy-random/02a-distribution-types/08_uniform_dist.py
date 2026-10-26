"""Uniform Distribution"""

from numpy import random, ndarray
import matplotlib.pyplot as plt
import seaborn as sns

def uniform_kde(uni: ndarray) -> None:
    """Plot a uniform distribution's KDE curve"""
    sns.kdeplot(uni)
    plt.show()

def uniform_hist(uni: ndarray) -> None:
    """Plot a uniform distribution's histogram"""
    sns.histplot(uni)
    plt.show()

def uniform_compare(uni: ndarray, norm: ndarray) -> None:
    """Compare a uniform distribution to a normal distribution"""
    sns.kdeplot(uni, fill=True, color="blue", label="Uniform")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def main() -> None:
    """Main function"""
    rng = random.default_rng() #NOSONAR
    uni = rng.uniform(size=1000)
    uniform_kde(uni)
    uniform_hist(uni)
    norm = rng.normal(size=1000)
    uniform_compare(uni, norm)

if __name__ == "__main__":
    main()
