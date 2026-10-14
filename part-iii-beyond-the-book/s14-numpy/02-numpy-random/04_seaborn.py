"""Data Visualization using Seaborn"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def use_distplot(data: np.ndarray) -> None:
    """Plot a distribution using distplot"""
    sns.distplot(data)
    plt.show()

def use_distplot_no_hist(data: np.ndarray) -> None:
    """Plot a distribution using distplot"""
    sns.distplot(data, hist=False)
    plt.show()

def use_histplot(data: np.ndarray) -> None:
    """Plot a distribution using histplot"""
    sns.histplot(data)
    plt.show()

def use_kdeplot(data: np.ndarray) -> None:
    """Plot a distribution using distplot"""
    sns.kdeplot(data)
    plt.show()

def use_displot(data: np.ndarray) -> None:
    """Plot a distribution using displot"""
    sns.displot(data, kde=True)
    plt.show()

def main() -> None:
    """Main function"""
    data = np.random.normal(size=1000)
    use_distplot(data)
    use_distplot_no_hist(data)
    use_histplot(data)
    use_kdeplot(data)
    use_displot(data)

if __name__ == "__main__":
    main()
