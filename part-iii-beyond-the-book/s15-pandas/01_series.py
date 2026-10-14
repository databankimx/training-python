"""Pandas Data Series"""

import pandas as pd

def create_series(data: list[int], named: bool=False,
                  names: list[str]=None) -> pd.Series:
    """Create a Series from a list"""
    if named:
        return pd.Series(data, index=names)
    print("Create a Series from a list:")
    print(f"List: {data}")
    series = pd.Series(data)
    print(f"Series:\n{series}\n")
    return series

def view_indices(series: pd.Series) -> None:
    """View the indices of a Series"""
    print("View the indices of a Series:")
    for i, val in enumerate(series):
        print(f"series[{i}] = {val}")
    print()

def view_named(series: pd.Series, names: list[str]) -> None:
    """View the values of a Series with named indices"""
    print("View the values of a Series with named indices:")
    for name in names:
        print(f"series[{name}] = {series[name]}")
    print()

def create_series_from_dict(data: dict[str,int],
                            sift: list["str"]=None) -> pd.Series:
    """Create a Series from a dictionary"""
    infix = "filtered " if sift else ""
    print(f"Create a {infix}Series from a dictionary:")
    print(f"Dictionary: {data}")
    if sift:
        print(f"Filter: {sift}")
    series = pd.Series(data) if not sift else pd.Series(data, index=sift)
    print(f"Series:\n{series}\n")
    return series

def main() -> None:
    """Main program"""
    data = [1, 2, 3, 4, 5]
    series = create_series(data)
    view_indices(series)
    names = ["a", "b", "c", "d", "e"]
    series = create_series(data, True, names)
    view_named(series, names)
    data_dict = dict(zip(names, data))
    series = create_series_from_dict(data_dict)
    sift = ["a", "c", "e"]
    series = create_series_from_dict(data_dict, sift)

if __name__ == "__main__":
    main()
