"""Logistic Distribution"""

from numpy import random, ndarray
import matplotlib.pyplot as plt
import seaborn as sns

def logistic_kde(log: ndarray) -> None:
    """Plot a logistic distribution's KDE curve"""
    sns.kdeplot(log)
    plt.show()

def logistic_hist(log: ndarray) -> None:
    """Plot a logistic distribution's histogram"""
    sns.histplot(log)
    plt.show()

def logistic_compare(log: ndarray, norm: ndarray) -> None:
    """Compare a logistic distribution to a normal distribution"""
    sns.kdeplot(log, fill=True, color="blue", label="Logistic")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def main() -> None:
    """Main Function"""
    rng = random.default_rng() #NOSONAR
    log = rng.logistic(size=1000)
    logistic_kde(log)
    logistic_hist(log)
    norm = rng.normal(size=1000)
    logistic_compare(log, norm)

if __name__ == "__main__":
    main()
