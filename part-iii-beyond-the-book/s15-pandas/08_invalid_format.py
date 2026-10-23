"""Invalid Data Format"""

import pandas as pd
from utilities import file_path

def load_from_csv(filepath: str, printout: bool = False) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath, quotechar="'", quoting=2)
    if printout:
        print("Obtained bad data:")
        print(df.tail(10), "\n")
    return df

def standardize_quotes(df: pd.DataFrame) -> None:
    """Remove any stray single quotes so every Date value is plain text"""
    df["Date"] = df["Date"].str.strip("'")
    print("Standardized the quotes in the Date column:")
    print(df.tail(10), "\n")

def format_dates(df: pd.DataFrame) -> None:
    """Format date columns to datetime format"""
    df["Date"] = pd.to_datetime(df["Date"])
    print("Formatted Date column to datetime format:")
    print(df.tail(10), "\n")

def add_missing_dates(df: pd.DataFrame) -> None:
    """Fill missing date values by shifting the previous date forward one day"""
    df.fillna({"Date": df["Date"].shift() + pd.DateOffset(1)}, inplace=True)
    print(df.tail(10), "\n")

def main() -> None:
    """Main function"""
    filepath = file_path("bad_data.csv", "data")
    df = load_from_csv(filepath, printout=True)
    standardize_quotes(df)
    format_dates(df)
    add_missing_dates(df)

if __name__ == "__main__":
    main()
