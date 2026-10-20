"""Pandas DataFrame from CSV File"""

import pandas as pd
from utilities import file_path, clear_terminal, pause

def load_from_csv(filepath: str) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    filename = filepath.split("\\")[-1]
    print(f"Loading data from {filename}:")
    df = pd.read_csv(filepath)
    print(df, "\n")
    return df

def show_all(df: pd.DataFrame) -> None:
    """Show all rows and columns in the DataFrame"""
    print(df.to_string(), "\n")

def show_200_rows(df: pd.DataFrame) -> None:
    """Show the first 200 rows of the DataFrame"""
    pd.options.display.max_rows = 200
    print(df, "\n")

def main():
    """Main program"""
    filepath = file_path("data.csv", "data")
    df = load_from_csv(filepath)
    pause()
    clear_terminal()
    show_all(df)
    pause()
    clear_terminal()
    show_200_rows(df)

if __name__ == "__main__":
    main()
