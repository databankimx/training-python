"""Poisson Distribution"""

from numpy import random, ndarray, long
import matplotlib.pyplot as plt
import seaborn as sns

def poisson_kde(poi: ndarray[long]) -> None:
    """Plot a Poisson distribution's KDE curve"""
    sns.kdeplot(poi)
    plt.show()

def poisson_hist(poi: ndarray[long]) -> None:
    """Plot a Poisson distribution's histogram"""
    sns.histplot(poi)
    plt.show()

def poisson_compare(poi: ndarray[long], norm: ndarray[long]) -> None:
    """Compare a Poisson distribution to a normal distribution"""
    sns.kdeplot(poi, fill=True, color="blue", label="Poisson")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def main() -> None:
    """Main function"""
    rng = random.default_rng()
    poi = rng.poisson(lam=2, size=1000)
    poisson_kde(poi)
    poisson_hist(poi)
    norm = rng.normal(loc=2, scale=1, size=1000)
    poisson_compare(poi, norm)

if __name__ == "__main__":
    main()
