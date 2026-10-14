"""Other Distribution Types"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def multinomial() -> None:
    """Multinomial Distribution"""
    rng = random.default_rng()
    mult = rng.multinomial(6, [1/6] * 6, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(mult, fill=True, color="blue", label="Multinomial")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def exponential() -> None:
    """Exponential Distribution"""
    rng = random.default_rng()
    mult = rng.exponential(size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(mult, fill=True, color="blue", label="Exponential")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def chi_square() -> None:
    """Chi Square Distribution"""
    rng = random.default_rng()
    mult = rng.chisquare(df=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(mult, fill=True, color="blue", label="Chi Square")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def rayleigh() -> None:
    """Rayleigh Distribution"""
    rng = random.default_rng()
    mult = rng.rayleigh(scale=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(mult, fill=True, color="blue", label="Rayleigh")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def pareto() -> None:
    """Pareto Distribution"""
    rng = random.default_rng()
    mult = rng.pareto(a=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(mult, fill=True, color="blue", label="Pareto")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def zipf() -> None:
    """Zipf Distribution"""
    rng = random.default_rng()
    mult = rng.zipf(a=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(mult, fill=True, color="blue", label="Zipf")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def main() -> None:
    """Main Function"""
    multinomial()
    exponential()
    chi_square()
    rayleigh()
    pareto()
    zipf()

if __name__ == "__main__":
    main()
