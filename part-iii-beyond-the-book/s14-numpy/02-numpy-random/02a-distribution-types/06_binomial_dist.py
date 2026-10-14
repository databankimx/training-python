"""Binomial Distribution"""

from numpy import ndarray, long
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def binomial_kde(binom: ndarray[long]) -> None:
    """Plot a binomial distribution's KDE curve"""
    sns.kdeplot(binom, fill=True, color="blue")
    plt.show()

def binomial_hist(binom: ndarray[long]) -> None:
    """Plot a binomial distribution's histogram"""
    sns.histplot(binom)
    plt.show()

def binomial_vs_normal(binom: ndarray[long], norm: ndarray[long]) -> None:
    """Plot a binomial distribution compared with a normal distribution"""
    sns.kdeplot(binom, fill=True, color="blue", label="Binomial")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def main() -> None:
    """Main function"""
    my_rng = random.default_rng()
    binom = my_rng.binomial(n=10, p=0.5, size=1000)
    binomial_kde(binom)
    binomial_hist(binom)
    norm = my_rng.normal(loc=5, scale=1, size=1000)
    binomial_vs_normal(binom, norm)

if __name__ == "__main__":
    main()
