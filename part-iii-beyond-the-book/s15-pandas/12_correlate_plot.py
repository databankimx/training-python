"""Pandas DataFrame Correlations and Plots"""

import pandas as pd
import matplotlib.pyplot as plt
from utilities import file_path

def load_from_csv(filepath: str, printout: bool=True) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath)
    if printout:
        print("Obtained data:")
        print(df.head(), "\n...\n")
    return df

def correlations(df: pd.DataFrame) -> None:
    """Calculate and display correlations between columns"""
    corr_matrix = df.corr()
    print("Correlations:")
    print(corr_matrix, "\n")

def plot_all(df: pd.DataFrame) -> None:
    """Plot all numerical columns in the DataFrame"""
    df.plot()
    plt.show()

def scatter_two_columns(df: pd.DataFrame, cols: list[str]) -> None:
    """Scatter plot two columns of the DataFrame"""
    df.plot.scatter(x=cols[0], y=cols[1], s=5)
    plt.show()

def hist_one_column(df: pd.DataFrame, col: str) -> None:
    """Histogram plot of one column of the DataFrame"""
    df[col].plot.hist()
    plt.show()

def main() -> None:
    """Main function"""
    filepath = file_path("data.csv", "data")
    df = load_from_csv(filepath)
    correlations(df)
    plot_all(df)
    scatter_two_columns(df, ["Duration", "Calories"])
    scatter_two_columns(df, ["Duration", "Maxpulse"])
    hist_one_column(df, "Duration")

if __name__ == "__main__":
    main()
