## Fully Clean the Data File

For our [bad_data.csv](./data/bad_data.csv) file, we now have the ammunition to clean the file in its entirety for data analysis.

---

### The Program

The fully [constructed program](./clean_csv.py) looks like this:

<details>
<summary>clean_csv.py</summary>

```python
import pandas as pd

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
```

</details>

---

### Testing with Our Data

We can test the program like this:

```python
from utility_functions import file_path
from clean_csv import clean_data_file

filepath = file_path("bad_data.csv", "data")
df = clean_data_file(filepath)
print("Cleaned data:")
print(df)
```

Output:

```
Cleaned data:
    Duration       Date  Pulse  Maxpulse  Calories
0       60.0 2020-12-01  110.0     130.0    409.10
1       60.0 2020-12-02  117.0     145.0    479.00
2       60.0 2020-12-03  103.0     135.0    340.00
3       45.0 2020-12-04  109.0     175.0    282.40
4       45.0 2020-12-05  117.0     148.0    406.00
5       60.0 2020-12-06  102.0     127.0    300.00
6       60.0 2020-12-07  110.0     136.0    374.00
7       69.0 2020-12-08  104.0     134.0    253.30
8       30.0 2020-12-09  109.0     133.0    195.10
9       60.0 2020-12-10   98.0     124.0    269.00
10      60.0 2020-12-11  103.0     147.0    329.30
11      60.0 2020-12-12  100.0     120.0    250.70
13      60.0 2020-12-13  106.0     128.0    345.30
14      60.0 2020-12-14  104.0     132.0    379.30
15      60.0 2020-12-15   98.0     123.0    275.00
16      60.0 2020-12-16   98.0     120.0    215.20
17      60.0 2020-12-17  100.0     120.0    300.00
18      45.0 2020-12-18   90.0     112.0    306.54
19      60.0 2020-12-19  103.0     123.0    323.00
20      45.0 2020-12-20   97.0     125.0    243.00
21      60.0 2020-12-21  108.0     131.0    364.20
22      45.0 2020-12-22  100.0     119.0    282.00
23      60.0 2020-12-23  130.0     101.0    300.00
24      45.0 2020-12-24  105.0     132.0    246.00
25      60.0 2020-12-25  102.0     126.0    334.50
26      60.0 2020-12-26  100.0     120.0    250.00
27      60.0 2020-12-27   92.0     118.0    241.00
28      60.0 2020-12-28  103.0     132.0    306.54
29      60.0 2020-12-29  100.0     132.0    280.00
30      60.0 2020-12-30  102.0     129.0    380.30
31      60.0 2020-12-31   92.0     115.0    243.00
```

We have handled:

* Missing Data
* Invalid Data Formatting
* Invalid Data Type
* Invalid Data
* Duplicate Data

Short of reprocessing the data from the source, this is as clean as we can make this data for further analysis.

---
