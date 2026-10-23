"""Probability distributions with scipy.stats"""

from scipy import stats

def normal_probabilities() -> None:
    """Use the normal distribution's pdf, cdf, and ppf"""
    print(f"Density at 0 (pdf): {stats.norm.pdf(0):.4f}")
    print(f"Probability below 0 (cdf): {stats.norm.cdf(0):.4f}")
    print(f"Probability below 1.96 (cdf): {stats.norm.cdf(1.96):.4f}")

def normal_quantile() -> None:
    """Find the value with a given probability below it (ppf)"""
    print(f"Value with 97.5% below it (ppf): {stats.norm.ppf(0.975):.4f}")

def shifted_normal() -> None:
    """Describe a normal distribution with a mean and standard deviation"""
    dist = stats.norm(loc=10, scale=2)
    print(f"Mean: {dist.mean():.1f}")
    print(f"Standard deviation: {dist.std():.1f}")
    print(f"Probability below 12 (cdf): {dist.cdf(12):.4f}")

def main() -> None:
    """Main function"""
    normal_probabilities()
    normal_quantile()
    shifted_normal()

if __name__ == "__main__":
    main()
