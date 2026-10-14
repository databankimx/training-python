"""Pandas DataFrame with Duplicate Rows"""

import pandas as pd
from utilities import file_path

def load_from_csv(filepath: str, printout: bool=False) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath)
    if printout:
        print("Obtained bad data:")
        print(df.loc[10:19], "\n")
    return df

def check_duplicates(df: pd.DataFrame) -> None:
    """Check for duplicate rows in the DataFrame"""
    duplicates = df[df.duplicated()]
    if duplicates.empty:
        print("No duplicate rows found.")
    else:
        print("Duplicate rows found:")
        print(duplicates, "\n")

def check_duplicate_dates(df: pd.DataFrame) -> None:
    """Check for duplicate rows in the DataFrame"""
    duplicates = df[df.duplicated(subset=["Date"])]
    if duplicates.empty:
        print("No duplicate date rows found.")
    else:
        print("Duplicate date rows found:")
        print(duplicates, "\n")

def drop_duplicates(df: pd.DataFrame) -> None:
    """Drop duplicate rows from the DataFrame"""
    df.drop_duplicates(inplace=True)
    print("Duplicate rows dropped (in place):")
    print(df.loc[10:20], "\n")

def main() -> None:
    """Main function"""
    filepath = file_path("bad_data.csv", "data")
    df = load_from_csv(filepath, printout=True)
    check_duplicates(df)
    check_duplicate_dates(df)
    drop_duplicates(df)

if __name__ == "__main__":
    main()
