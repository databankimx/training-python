"""Support functions for cleaning the bad_data.csv file"""

import pandas as pd

def load_from_csv(filepath: str, printout: bool = False) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath, quotechar="'", quoting=2)
    if printout:
        print("Obtained bad data:")
        print(df.tail(10), "\n")
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Return the DataFrame with duplicate rows removed"""
    return df.drop_duplicates()

def standardize_quotes(df: pd.DataFrame) -> None:
    """Remove any stray single quotes so every Date value is plain text"""
    df["Date"] = df["Date"].str.strip("'")

def format_dates(df: pd.DataFrame) -> None:
    """Format the Date column as datetime values"""
    standardize_quotes(df)
    df["Date"] = pd.to_datetime(df["Date"])

def add_missing_dates(df: pd.DataFrame) -> None:
    """Fill missing dates with the previous row's date plus one day"""
    df.fillna({"Date": df["Date"].shift() + pd.DateOffset(1)}, inplace=True)

def add_missing_calories(df: pd.DataFrame) -> None:
    """Fill missing calorie values with the average calories"""
    df.fillna({"Calories": round(df["Calories"].mean(), 2)}, inplace=True)

def fix_invalid_durations(df: pd.DataFrame) -> None:
    """Replace durations more than twice the average with the average"""
    avg_dur = df["Duration"].mean()
    max_dur = avg_dur * 2
    for i in df.index:
        if df.loc[i, "Duration"] > max_dur:
            df.loc[i, "Duration"] = round(avg_dur)

def clean_data_file(csv: str) -> pd.DataFrame:
    """Run every cleaning step on the CSV file and return the DataFrame"""
    df = load_from_csv(csv)
    df = drop_duplicates(df)
    format_dates(df)
    add_missing_dates(df)
    add_missing_calories(df)
    fix_invalid_durations(df)
    return df
