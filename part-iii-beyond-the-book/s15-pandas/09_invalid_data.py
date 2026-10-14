"""Invalid Data"""

import pandas as pd
from utilities import file_path

def load_from_csv(filepath: str, printout: bool=False) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    df = pd.read_csv(filepath)
    if printout:
        print("Obtained bad data:")
        print(df.head(10), "\n")
    return df

def drop_invalid_durations(df: pd.DataFrame) -> None:
    """Drop rows with invalid durations in the DataFrame"""
    df.drop(df[df["Duration"] > 100].index, inplace=True)
    print("Dropped invalid durations:")
    print(df.head(10), "\n")

def fix_invalid_durations(df: pd.DataFrame) -> None:
    """Fix invalid durations in the DataFrame"""
    avg_dur = df["Duration"].mean()
    max_dur = avg_dur * 2
    for i in df.index:
        if df.loc[i, "Duration"] > max_dur:
            df.loc[i, "Duration"] = round(avg_dur)
    print("Fixed invalid durations:")
    print(df.head(10), "\n")

def main() -> None:
    """Main function"""
    filepath = file_path("bad_data.csv", "data")
    df = load_from_csv(filepath, printout=True)
    drop_invalid_durations(df)
    df = load_from_csv(filepath)
    fix_invalid_durations(df)

if __name__ == "__main__":
    main()
