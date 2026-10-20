"""Pandas DataFrame from JSON File"""

import pandas as pd
from utilities import file_path, clear_terminal, pause

def load_from_json(filepath: str) -> pd.DataFrame:
    """Load data from a JSON file into a Pandas DataFrame"""
    filename = filepath.split("\\")[-1]
    print(f"Loading data from {filename}:")
    df = pd.read_json(filepath)
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
    filepath = file_path("data.json", "data")
    df = load_from_json(filepath)
    pause()
    clear_terminal()
    show_all(df)
    pause()
    clear_terminal()
    show_200_rows(df)

if __name__ == "__main__":
    main()
