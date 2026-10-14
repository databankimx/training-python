## Cleaning Empty Cells

Probably the most common "bad data" scenario is missing values. When a row
is missing values in one or more columns, it can taint the validity of any
computations over the column or relationships between columns.

Pandas provides a couple of different approaches to handling missing data:

For each example, assume that we have already run the following code to
load a `DataFrame`:

```python
import pandas as pd

df = pd.read_csv("./data/bad_data.csv")
```

Recall that the tail of this `DataFrame` has a couple missing values:

```
22        45           NaN    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60    2020/12/26    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132       NaN
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
```

---

### Remove Rows with Missing Data

One strategy for dealing with missing data is to simply remove any rows 
that have `null` or empty columns.

It might seem that this is a bad choice, since it is removing otherwise
meaningful data. However, sing most data sets tend to be quite large, the
effect on overall computation is usually negligible.

We remove rows from the `DataFrame` using the `dropna()` method.

```python
new_df = df.dropna()
print("Removed rows with missing columns (new DataFrame):")
print(new_df.tail(10))
```

Output:

```
Removed rows with missing columns (new DataFrame):
    Duration          Date  Pulse  Maxpulse  Calories
20        45  '2020/12/20'     97       125     243.0
21        60  '2020/12/21'    108       131     364.2
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60    2020/12/26    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
```

We can see that rows 22 and 28 have been removed.

> Note: We can modify the existing `DataFrame` instead of creating a new 
> one by adding the `inplace=True` argument:
>
> ```python
> df.dropna(inplace=True)
> ```

---

### Replacing Missing Data

Another strategy for handling missing data is to fill in the empty cells
with default data:

```python
new_df = df.fillna(130)
print("Filled missing column values with 130 (new DataFrame):")
print(new_df.tail(10))
```

Output:

```
Filled missing column values with 130 (new DataFrame):
    Duration          Date  Pulse  Maxpulse  Calories
22        45           130    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60    2020/12/26    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132     130.0
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
```

This is a little problematic, since the data we inserted for `Date` in row
22 is invalid.

> Note: We can modify the existing `DataFrame` instead of creating a new 
> one by adding the `inplace=True` argument:
>
> ```python
> df.fillna(inplace=True)
> ```

---

### Replacing Missing Data by Column

We can also specify the column where we are replacing data to avoid the
issue we created in the previous attempt.

> Note: In the tutorial I followed, a slightly different syntax was used
> from what you'll see below in the example code.
>
> ```python
> df[col].fillna(val, inplace=True)
> ```
>
> But that method is deprecated and will not work in Pandas 3.0+: returns
> this warning:
>
> ```
> FutureWarning: A value is trying to be set on a copy of a DataFrame or 
> Series through chained assignment using an inplace method.
> The behavior will change in pandas 3.0. This inplace method will never
> work because the intermediate object on which we are setting values 
> always behaves as a copy.
> 
> For example, when doing 'df[col].method(val, inplace=True)', try using 
> 'df.method({col: value}, inplace=True)' or df[col] = df[col].method
> (value) instead, to perform the operation inplace on the original object.
> 
> df[col].fillna(val, inplace=True)
> ```

```python
defaults = {
    "Calories": 130,
    "Date": "'2020/12/22'"
}
for col, val in defaults.items():
    df.fillna({col: val}, inplace=True)
    print(f"Filled {col} values with {val} (in place):")
print(f"----------\n{df.tail(10)}")
```

Output:

```
Filled Calories values with 130 (in place):
Filled Date values with '2020/12/22' (in place):
----------
    Duration          Date  Pulse  Maxpulse  Calories
22        45  '2020/12/22'    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60    2020/12/26    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132     130.0
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
```

Now, we have properly inserted a date in the `Date` column and a number in
the `Calories` column.

---

### Replacing Missing Data with Average Value

It can be problematic to create default values to use when replacing 
missing data so a good strategy for replacing missing data in numeric
columns is to compute the mean average using the `df["col"].mean()` method
and use the resulting average value.

```python
defaults = {
    "Calories": round(df["Calories"].mean(), 2),
    "Date": "'2020/12/22'"
}
for col, val in defaults.items():
    df.fillna({col: val}, inplace=True)
    print(f"Filled {col} values with {val} (in place):")
print(f"----------\n{df.tail(10)}\n")
```

Output:

```
Filled Calories values with 304.68 (in place):
Filled Date values with '2020/12/22' (in place):
----------
    Duration          Date  Pulse  Maxpulse  Calories
22        45  '2020/12/22'    100       119    282.00
23        60  '2020/12/23'    130       101    300.00
24        45  '2020/12/24'    105       132    246.00
25        60  '2020/12/25'    102       126    334.50
26        60    2020/12/26    100       120    250.00
27        60  '2020/12/27'     92       118    241.00
28        60  '2020/12/28'    103       132    304.68
29        60  '2020/12/29'    100       132    280.00
30        60  '2020/12/30'    102       129    380.30
31        60  '2020/12/31'     92       115    243.00
```

---
