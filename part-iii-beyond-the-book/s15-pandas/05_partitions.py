"""Pandas DataFrame Partitions"""

import pandas as pd
from utilities import file_path

def load_from_json(filepath: str) -> pd.DataFrame:
    """Load data from a JSON file into a Pandas DataFrame"""
    return pd.read_json(filepath)

def show_info(df: pd.DataFrame) -> None:
    """Display information about the DataFrame"""
    print("DataFrame Info:")
    print(df.info(), "\n")

def top_rows(df: pd.DataFrame) -> None:
    """Display the first 5 rows of the DataFrame"""
    print("Top 5 rows:")
    print(df.head(), "\n")

def top_n_rows(df: pd.DataFrame, n: int=10) -> None:
    """Display the first n rows of the DataFrame"""
    print(f"Top {n} rows:")
    print(df.head(n), "\n")

def bottom_rows(df: pd.DataFrame) -> None:
    """Display the first 5 rows of the DataFrame"""
    print("Bottom 5 rows:")
    print(df.tail(), "\n")

def bottom_n_rows(df: pd.DataFrame, n: int=10) -> None:
    """Display the last n rows of the DataFrame"""
    print(f"Bottom {n} rows:")
    print(df.tail(n), "\n")

def main() -> None:
    """Main program"""
    filepath = file_path("data.json", "data")
    df = load_from_json(filepath)
    show_info(df)
    top_rows(df)
    top_n_rows(df, 10)
    bottom_rows(df)
    bottom_n_rows(df, 10)

if __name__ == "__main__":
    main()
