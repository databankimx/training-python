"""Empty Data"""

import pandas as pd
from utilities import file_path

def load_from_csv(filepath: str, printout: bool=False) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath)
    if printout:
        print("Obtained bad data:")
        print(df.tail(10), "\n")
    return df

def remove_rows(df: pd.DataFrame) -> None:
    """Remove rows with missing columns)"""
    new_df = df.dropna()
    print("Removed rows with missing columns (new DataFrame):")
    print(new_df.tail(10), "\n")

def remove_in_place(df: pd.DataFrame) -> None:
    """Remove rows with missing columns"""
    df.dropna(inplace=True)
    print("Removed rows with missing columns (in place):")
    print(df.tail(10), "\n")

def fill_rows(df: pd.DataFrame) -> None:
    """Fill missing column values"""
    new_df = df.fillna(130)
    print("Filled missing column values with 130 (new DataFrame):")
    print(new_df.tail(10), "\n")

def fill_in_place(df: pd.DataFrame) -> None:
    """Fill missing column values"""
    df.fillna(130, inplace=True)
    print("Filled missing column values with 130 (in place):")
    print(df.tail(10), "\n")

def fill_specific(df: pd.DataFrame) -> None:
    """Fill specific column values"""
    defaults = {
        "Calories": 130,
        "Date": "'2020/12/22'"
    }
    for col, val in defaults.items():
        # df[col].fillna(val, inplace=True)
        df.fillna({col: val}, inplace=True)
        print(f"Filled {col} values with {val} (in place):")
    print(f"----------\n{df.tail(10)}\n")

def fill_average(df: pd.DataFrame) -> None:
    """Fill specific column values with mean average"""
    defaults = {
        "Calories": round(df["Calories"].mean(), 2),
        "Date": "'2020/12/22'"
    }
    for col, val in defaults.items():
        df.fillna({col: val}, inplace=True)
        print(f"Filled {col} values with {val} (in place):")
    print(f"----------\n{df.tail(10)}\n")

def main() -> None:
    """Main program"""
    csv = file_path("bad_data.csv", "data")
    df = load_from_csv(csv, True)
    remove_rows(df)
    remove_in_place(df)
    df = load_from_csv(csv)
    fill_rows(df)
    fill_in_place(df)
    df = load_from_csv(csv)
    fill_specific(df)
    df = load_from_csv(csv)
    fill_average(df)

if __name__ == "__main__":
    main()
