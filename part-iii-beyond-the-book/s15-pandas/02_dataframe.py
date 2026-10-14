"""Pandas DataFrame"""

import pandas as pd
import json

def simple_dataframe(data: dict[str,list[any]]) -> None:
    """Create and display a simple DataFrame"""
    print("Create a DataFrame:")
    print(f"Data: {json.dumps(data, indent=4)}")
    df = pd.DataFrame(data)
    print(f"DataFrame:\n{df}\n")

def locate_row(data: dict[str,list[any]]) -> None:
    """Locate a specific row in the DataFrame"""
    print("Locate DataFrame Row:")
    df = pd.DataFrame(data)
    row = df.loc[0]
    print(f"Row 0:\n{row}\n")

def multi_row(data: dict[str,list[any]]) -> None:
    """Locate multiple specific rows in the DataFrame"""
    print("Locate Multiple DataFrame Rows:")
    df = pd.DataFrame(data)
    rows = df.loc[[0, 2]]
    print(f"Rows 0 & 2:\n{rows}\n")

def label_rows(data: dict[str,list[any]]) -> None:
    """Label the DataFrame rows"""
    print("Label DataFrame Rows:")
    df = pd.DataFrame(data, index=["1st", "2nd", "3rd", "4th"])
    print(f"{df}\n")

def label_cols(data: dict[str,list[any]]) -> None:
    """Label the DataFrame columns"""
    df = pd.DataFrame(data)
    print("Label DataFrame Columns:")
    df.columns = ["Person", "Years", "Home"]
    print(df, "\n")

def main() -> None:
    """Main function"""
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [24, 30, 28, 26],
        "City": ["New York", "Tokyo", "New York", "London"]
    }
    simple_dataframe(data)
    locate_row(data)
    multi_row(data)
    label_rows(data)
    label_cols(data)

if __name__ == "__main__":
    main()
