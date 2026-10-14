"""Statistical significance tests with SciPy"""

import numpy as np
#pylint: disable=no-name-in-module
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest

ALPHA = 0.05
rng = np.random.default_rng(42)

def report(p_value: float) -> None:
    """Compare the p-value with the alpha level"""
    if p_value <= ALPHA:
        print(f"p-value {p_value:.4f} <= alpha {ALPHA}: reject the null hypothesis\n")
    else:
        print(f"p-value {p_value:.4f} > alpha {ALPHA}: keep the null hypothesis\n")

def t_test() -> None:
    """Check whether two samples have the same mean"""
    print("T-test (do two samples share the same mean?)")
    v1 = rng.normal(size=100)
    v2 = rng.normal(size=100)
    res = ttest_ind(v1, v2)
    print(f"t-statistic: {res.statistic:.4f}")
    report(res.pvalue)

def ks_test() -> None:
    """Check whether a sample follows a normal distribution"""
    print("KS-test (does a sample follow the normal distribution?)")
    v = rng.normal(size=100)
    res = kstest(v, "norm")
    print(f"KS statistic: {res.statistic:.4f}")
    report(res.pvalue)

def describe_data() -> None:
    """Summarize a sample"""
    print("Statistical description:")
    v = rng.normal(size=100)
    desc = describe(v)
    print(f"Observations: {desc.nobs}")
    print(f"Min and max: {desc.minmax}")
    print(f"Mean: {desc.mean:.4f}")
    print(f"Variance: {desc.variance:.4f}")
    print(f"Skewness: {desc.skewness:.4f}")
    print(f"Kurtosis: {desc.kurtosis:.4f}\n")

def normality() -> None:
    """Check skewness, kurtosis, and the normality test"""
    print("Normality test (skewness and kurtosis):")
    v = rng.normal(size=100)
    print(f"Skewness: {skew(v):.4f}")
    print(f"Kurtosis: {kurtosis(v):.4f}")
    res = normaltest(v)
    print(f"Normality statistic: {res.statistic:.4f}")
    report(res.pvalue)

def main() -> None:
    """Main function"""
    t_test()
    ks_test()
    describe_data()
    normality()

if __name__ == "__main__":
    main()
