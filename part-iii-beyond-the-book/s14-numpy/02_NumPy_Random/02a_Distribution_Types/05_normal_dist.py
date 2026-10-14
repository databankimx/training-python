"""Normal Distribution"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def normal_small() -> None:
    """Generate a normal distribution with 20 values (σ = 1)"""
    # Old way - using NumPy's `random.normal()` function
    # arr = random.normal(scale=1, size=20)
    rng = random.default_rng()
    arr = rng.normal(size=20)
    print(arr)
    sns.displot(arr, kde=True)
    plt.show()

def normal_1d() -> None:
    """Generate a normal distribution with 1000 values (σ = 1)"""
    rng = random.default_rng()
    arr = rng.normal(size=1000)
    sns.displot(arr, kde=True)
    plt.show()

def normal_1d_ms() -> None:
    """Generate a normal distribution with 1000 values (σ = 2)"""
    rng = random.default_rng()
    arr = rng.normal(loc=1, scale=2, size=1000)
    sns.displot(arr, kde=True)
    plt.show()

def normal_2d() -> None:
    """Generate a normal distribution with 20x20 values (σ = 1)"""
    rng = random.default_rng()
    arr = rng.normal(size=(20, 20))
    sns.displot(arr, kde=True)
    plt.show()

def normal_2d_ms() -> None:
    """Generate a normal distribution with 20x20 values (σ = 2)"""
    rng = random.default_rng()
    arr = rng.normal(loc=1, scale=2, size=(20, 20))
    sns.displot(arr, kde=True)
    plt.show()

def main() -> None:
    """Main Function"""
    normal_small()
    normal_1d()
    normal_1d_ms()
    # normal_2d()
    # normal_2d_ms()

if __name__ == "__main__":
    main()
