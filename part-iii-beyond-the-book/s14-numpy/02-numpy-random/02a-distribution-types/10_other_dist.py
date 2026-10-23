"""Other Distribution Types"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def multinomial() -> None:
    """Multinomial Distribution: count of one face over 1000 experiments of 6 rolls"""
    rng = random.default_rng() #NOSONAR
    counts = rng.multinomial(6, [1/6] * 6, size=1000)
    dist = counts[:, 0]
    norm = rng.normal(size=1000)
    sns.kdeplot(dist, fill=True, color="blue", label="Multinomial")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def exponential() -> None:
    """Exponential Distribution"""
    rng = random.default_rng() #NOSONAR
    dist = rng.exponential(size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(dist, fill=True, color="blue", label="Exponential")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def chi_square() -> None:
    """Chi Square Distribution"""
    rng = random.default_rng() #NOSONAR
    dist = rng.chisquare(df=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(dist, fill=True, color="blue", label="Chi Square")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def rayleigh() -> None:
    """Rayleigh Distribution"""
    rng = random.default_rng() #NOSONAR
    dist = rng.rayleigh(scale=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(dist, fill=True, color="blue", label="Rayleigh")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def pareto() -> None:
    """Pareto (Lomax, Pareto II) Distribution: NumPy's pareto() draws from this form"""
    rng = random.default_rng() #NOSONAR
    dist = rng.pareto(a=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(dist, fill=True, color="blue", label="Pareto")
    sns.kdeplot(norm, fill=True, color="red", label="Normal")
    plt.legend()
    plt.show()

def zipf() -> None:
    """Zipf Distribution"""
    rng = random.default_rng() #NOSONAR
    dist = rng.zipf(a=2, size=1000)
    norm = rng.normal(size=1000)
    sns.kdeplot(dist, fill=True, color="blue", label="Zipf")
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
