"""Clean Data File"""

import pandas as pd
from utilities import file_path

def load_from_csv(filepath: str, printout: bool=False) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath, quotechar="'", quoting=2)
    if printout:
        print("Obtained bad data:")
        print(df.tail(10), "\n")
    return df

def drop_duplicates(df: pd.DataFrame) -> None:
    """Drop duplicate rows from the DataFrame"""
    df.drop_duplicates(inplace=True)

def add_missing_quotes(val: str) -> str:
    """Add missing quotes to string values"""
    if not val or not isinstance(val, str):
        return val
    pre = "" if val.startswith("'") else "'"
    post = "" if val.endswith("'") else "'"
    return f"{pre}{val}{post}"

def quote_date_strings(df: pd.DataFrame) -> None:
    """Quote string values in the Date column"""
    # pylint: disable=unnecessary-lambda
    df["Date"].apply(lambda d: add_missing_quotes(d))

def format_dates(df: pd.DataFrame) -> None:
    """Format date columns to datetime format"""
    quote_date_strings(df)
    df["Date"] = pd.to_datetime(df["Date"])

def add_missing_dates(df: pd.DataFrame) -> None:
    """Add missing date values by interpolating"""
    df.fillna({"Date": df["Date"].shift() + pd.DateOffset(1)}, inplace=True)

def add_missing_calories(df: pd.DataFrame) -> None:
    """Add missing calorie values by interpolating"""
    df.fillna({"Calories": round(df["Calories"].mean(), 2)}, inplace=True)

def fix_invalid_durations(df: pd.DataFrame) -> None:
    """Fix invalid durations in the DataFrame"""
    avg_dur = df["Duration"].mean()
    max_dur = avg_dur * 2
    for i in df.index:
        if df.loc[i, "Duration"] > max_dur:
            df.loc[i, "Duration"] = round(avg_dur)

def clean_data_file(csv: str) -> pd.DataFrame:
    """Clean data from a CSV file"""
    df = load_from_csv(csv)
    drop_duplicates(df)
    format_dates(df)
    add_missing_dates(df)
    add_missing_calories(df)
    fix_invalid_durations(df)
    return df

def main() -> None:
    """Main function"""
    filepath = file_path("bad_data.csv", "data")
    df = clean_data_file(filepath)
    print("Cleaned data:")
    print(df, "\n")

if __name__ == "__main__":
    main()
