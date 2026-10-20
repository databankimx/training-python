"""Clean DataFrame"""

import pandas as pd
from utilities import file_path

def load_from_csv(filepath: str) -> pd.DataFrame:
    """Load data from a CSV file into a Pandas DataFrame"""
    return pd.read_csv(filepath)

def main() -> None:
    """Main program"""
    df = load_from_csv(file_path("bad_data.csv", "data"))
    print("Obtained bad data:")
    print(df.tail(10), "\n")

if __name__ == "__main__":
    main()
