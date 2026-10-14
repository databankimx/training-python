## Cleaning Invalid Data Formats

Cleaning up data formats can be challenging, but Pandas provides functions
that assist with this process.

Reviewing the bad data that we loaded from the CSV, we have:

CSV Tail:

```
45,null,100,119,282.0
60,'2020/12/23',130,101,300.0
45,'2020/12/24',105,132,246.0
60,'2020/12/25',102,126,334.5
60,2020/12/26,100,120,250.0
60,'2020/12/27',92,118,241.0
60,'2020/12/28',103,132,null
60,'2020/12/29',100,132,280.0
60,'2020/12/30',102,129,380.3
60,'2020/12/31',92,115,243.0
```

`DataFrame` Tail

```
    Duration        Date  Pulse  Maxpulse  Calories
22      45.0         NaN  100.0     119.0     282.0
23      60.0  2020/12/23  130.0     101.0     300.0
24      45.0  2020/12/24  105.0     132.0     246.0
25      60.0  2020/12/25  102.0     126.0     334.5
26      60.0  2020/12/26  100.0     120.0     250.0
27      60.0  2020/12/27   92.0     118.0     241.0
28      60.0  2020/12/28  103.0     132.0       NaN
29      60.0  2020/12/29  100.0     132.0     280.0
30      60.0  2020/12/30  102.0     129.0     380.3
31      60.0  2020/12/31   92.0     115.0     243.0
```

Ignoring missing values, we have a couple of problems with the `Date` 
column format:

1. This column data is in the form of string, which need to be converted
   to datetime
2. Certain rows (row 26, e.g) are missing quotation marks, so they will
   not match the format of other rows when we convert the data type.
    * This needs to be addressed first.

Let's assume that we have already run the following to load the `DataFrame`

```python
import pandas as pd

df = pd.read_csv("./data/bad_data.csv", quotechar="'", quoting=2)
```

Note the addition of the `quotechar` attribute to specify that items are
delimited with single-quotes in our CSV file. This is necessary for the
first step in our cleanup below.

---

### Fix the Missing Quotation Marks

To perform a task on every item in a column, we use the Pandas `apply()`
method that takes a lambda as its argument.

First, we'll create a function to add single-quotes surrounding any 
non-null value that is missing them:

```python
def add_missing_quotes(val: str) -> str:
    """Add missing quotes to string values"""
    if not val or not isinstance(val, str):
        return val
    pre = "" if val.startswith("'") else "'"
    post = "" if val.endswith("'") else "'"
    return f"{pre}{val}{post}"
```

The we'll process the `Date` column:

```python
df["Date"].apply(lambda d: add_missing_quotes(d))
print("Quoted string values in the Date column:")
print(df.tail(10))
```

Output:

```
Quoted string values in the Date column:
    Duration        Date  Pulse  Maxpulse  Calories
22      45.0         NaN  100.0     119.0     282.0
23      60.0  2020/12/23  130.0     101.0     300.0
24      45.0  2020/12/24  105.0     132.0     246.0
25      60.0  2020/12/25  102.0     126.0     334.5
26      60.0  2020/12/26  100.0     120.0     250.0
27      60.0  2020/12/27   92.0     118.0     241.0
28      60.0  2020/12/28  103.0     132.0       NaN
29      60.0  2020/12/29  100.0     132.0     280.0
30      60.0  2020/12/30  102.0     129.0     380.3
31      60.0  2020/12/31   92.0     115.0     243.0
```

---

### Converting to Dates

Now that we have standardized strings `'yyyy-mm-dd'` for all our dates,
we can use the Pandas `to_datetime()` function to convert the `Date`
column.

```python
df["Date"] = pd.to_datetime(df["Date"])
print("Formatted Date column to datetime format:")
print(df.tail(10))
```

> Note: This would produce an error due to the mismatched string format if
> we had not previously standardized the quotation marks.

Output:

```
Formatted Date column to datetime format:
    Duration       Date  Pulse  Maxpulse  Calories
22      45.0        NaT  100.0     119.0     282.0
23      60.0 2020-12-23  130.0     101.0     300.0
24      45.0 2020-12-24  105.0     132.0     246.0
25      60.0 2020-12-25  102.0     126.0     334.5
26      60.0 2020-12-26  100.0     120.0     250.0
27      60.0 2020-12-27   92.0     118.0     241.0
28      60.0 2020-12-28  103.0     132.0       NaN
29      60.0 2020-12-29  100.0     132.0     280.0
30      60.0 2020-12-30  102.0     129.0     380.3
31      60.0 2020-12-31   92.0     115.0     243.0
```

---

### Filling in the Missing Dates

We still have at least one missing date in our data (see row 22).

We could certainly just remove it like this:

```python
df.dropna(subset=["Date"], inplace=True)
```

Or we could replace it with a static date:

```python
df.fillna({"Date": "'12/22/2024'"}, inplace=True)
```

But let's get a little clever, using the `shift()` function, which takes
the value at the previous row, and add one day to it.

```python
df.fillna({"Date": df["Date"].shift() + pd.DateOffset(1)}, inplace=True)
print(df.tail(10))
```

Output:

```
    Duration       Date  Pulse  Maxpulse  Calories
22      45.0 2020-12-22  100.0     119.0     282.0
23      60.0 2020-12-23  130.0     101.0     300.0
24      45.0 2020-12-24  105.0     132.0     246.0
25      60.0 2020-12-25  102.0     126.0     334.5
26      60.0 2020-12-26  100.0     120.0     250.0
27      60.0 2020-12-27   92.0     118.0     241.0
28      60.0 2020-12-28  103.0     132.0       NaN
29      60.0 2020-12-29  100.0     132.0     280.0
30      60.0 2020-12-30  102.0     129.0     380.3
31      60.0 2020-12-31   92.0     115.0     243.0
```

All our dates have now been standardized, converted to datetime objects, 
and filled in where missing.

---
