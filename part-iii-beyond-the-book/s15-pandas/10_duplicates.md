## Cleaning Duplicate Data

Another common issue is duplicate data. Frequently raw data we receive prior to analysis may have duplicate rows inserted.

Pandas provides the `duplicated()` and `drop_duplicates()` functions to
identify and remove duplicate rows.

Looking at the same dataset we have been working with, we can see that the
data for 12/12/2020 occurs twice (on rows 11 and 12)

```
Obtained bad data:
    Duration          Date  Pulse  Maxpulse  Calories
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
18        45  '2020/12/18'     90       112       NaN
19        60  '2020/12/19'    103       123     323.0
```

Let's assume that we have already run the following to load the `DataFrame`

```python
import pandas as pd

df = pd.read_csv("./data/bad_data.csv")
```

---

### Identifying Duplicate Rows

By default, the `duplicated()` function returns any rows that contain the
same data in all columns (except ID).

```python
duplicates = df[df.duplicated()]
if duplicates.empty:
    print("No duplicate rows found.")
else:
    print("Duplicate rows found:")
    print(duplicates)
```

Output:

```
Duplicate rows found:
    Duration          Date  Pulse  Maxpulse  Calories
12        60  '2020/12/12'    100       120     250.7
```

Note: This assumes that the first instance is valid and only returns
additional instances as duplicates.

---

### Identifying Duplicates by Column

Sometimes, we may want to treat rows as duplicates, even if not all of the
columns match exactly. In our dataset, we know there should be one entry
per day, so we could check for duplicates by comparing only the date column
by adding the `subset` argument.

```python
duplicates = df[df.duplicated(subset=["Date"])]
if duplicates.empty:
    print("No duplicate date rows found.")
else:
    print("Duplicate date rows found:")
    print(duplicates)
```

Output:

```
Duplicate date rows found:
    Duration          Date  Pulse  Maxpulse  Calories
12        60  '2020/12/12'    100       120     250.7
```

---

### Removing Duplicates

Once identified, it is simple to remove the duplicates:

```python
df.drop_duplicates(inplace=True)
print("Duplicate rows dropped (in place):")
print(df.loc[10:20])
```

Output:

```
Duplicate rows dropped (in place):
    Duration          Date  Pulse  Maxpulse  Calories
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
18        45  '2020/12/18'     90       112       NaN
19        60  '2020/12/19'    103       123     323.0
20        45  '2020/12/20'     97       125     243.0
```

Note that the duplicate (row 12) is no longer in the dataset.

---
