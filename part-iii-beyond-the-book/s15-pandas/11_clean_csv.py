"""Clean Data File"""

from utilities import file_path
from clean_csv import clean_data_file

def main() -> None:
    """Main function"""
    filepath = file_path("bad_data.csv", "data")
    df = clean_data_file(filepath)
    print("Cleaned data:")
    print(df, "\n")

if __name__ == "__main__":
    main()
